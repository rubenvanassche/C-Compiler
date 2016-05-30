# ANTLR Imports
from antlr4 import *
from CLexer import CLexer
from CParser import CParser

# Symbol Table
from SymbolTable import SymbolTable

# AST Imports
from src.AST.AmpersandExpression import AmpersandExpression
from src.AST.ArithmeticExpression import ArithmeticExpression
from src.AST.AssignmentExpression import AssignmentExpression
from src.AST.BreakStatement import BreakStatement
from src.AST.ComparisonExpression import ComparisonExpression
from src.AST.CompoundStatement import CompoundStatement
from src.AST.ConstantExpression import ConstantExpression
from src.AST.ContinueStatement import ContinueStatement
from src.AST.DecrementerExpression import DecrementerExpression
from src.AST.Expression import Expression
from src.AST.ForStatement import ForStatement
from src.AST.FunctionCallExpression import FunctionCallExpression
from src.AST.FunctionStatement import FunctionStatement
from src.AST.IfelseStatement import IfelseStatement
from src.AST.IncludeStatement import IncludeStatement
from src.AST.IncrementerExpression import IncrementerExpression
from src.AST.LogicExpression import LogicExpression
from src.AST.NegateExpression import NegateExpression
from src.AST.NotExpression import NotExpression
from src.AST.Program import Program
from src.AST.ReturnStatement import ReturnStatement
from src.AST.StarExpression import StarExpression
from src.AST.Statement import Statement
from src.AST.TypedefStatement import TypedefStatement
from src.AST.VariableCallExpression import VariableCallExpression
from src.AST.VariableExpression import VariableExpression
from src.AST.WhileStatement import WhileStatement

# Types
from src.Type.AddressType import AddressType
from src.Type.ArrayType import ArrayType
from src.Type.BooleanType import BooleanType
from src.Type.CharacterType import CharacterType
from src.Type.IntegerType import IntegerType
from src.Type.RealType import RealType

from src.Type.Parameter import Parameter
from src.Type.Parameter import ParametersList
from src.Type.Parameter import Argument
from src.Type.Parameter import ArgumentsList

# Data
from src.Data.AddressData import AddressData

class ASTBuilder:
    """Class for building AST"""

    def __init__(self, filepath, symboltable):
        """Initialize with path to file(string)"""
        self.filepath = filepath
        self.AST = None

        self.sym = symboltable

    def build(self):
        """Build the AST"""
        input = FileStream(self.filepath)
        lexer = CLexer(input)
        stream = CommonTokenStream(lexer)
        parser = CParser(stream)
        tree = parser.program()

        # Add initial program node
        self.AST = Program(self.sym)



        # Add statements
        for i in range(tree.getChildCount()):
            self.AST.addStatement(self.buildStatement(tree.getChild(i)))

        return self.AST

    def serialize(self):
        print(self.AST)

    def buildStatement(self, tree):
        """Build Statement"""
        if(tree.getChildCount() == 0):
            raise RuntimeError("Invalid statement: '" + tree.getText() + "'")
        elif(tree.getChildCount() == 1):
            # SEMICOLON
            token = tree.getChild(0).getPayload()
            if(isinstance(token, Token) and token.type == CLexer.SEMICOLON):
                return Statement()

            # Otherwise something went wrong
            raise RuntimeError("Invalid statement: '" + tree.getText() + "'")
        else:
            # BREAK SEMICOLON
            # CONTINUE SEMICOLON
            # INCLUDE (CPATH|STRING)
            # expression SEMICOLON
            # LBRACE statement* RBRACE
            # WHILE LPAREN expression RPAREN statement
            # IF LPAREN expression RPAREN statement (ELSE statement)?
            # FOR LPAREN expression? SEMICOLON expression? SEMICOLON expression? RPAREN statement
            # TYPEDEF type IDENTIFIER (LSQUAREBRACKET NUM RSQUAREBRACKET)* SEMICOLON
            # type IDENTIFIER LPAREN (VOID|type IDENTIFIER? (COMMA type IDENTIFIER?)*)? RPAREN (SEMICOLON|LBRACE statement* RBRACE)
            token = tree.getChild(0).getPayload()
            if(isinstance(token, Token)):
                if(token.type == CLexer.BREAK):
                    if(isinstance(tree.getChild(1).getPayload(), Token) and tree.getChild(1).getPayload().type == CLexer.SEMICOLON):
                        return BreakStatement()
                    else:
                        raise RuntimeError("Invalid statement: '" + tree.getText() + "'")
                elif(token.type == CLexer.CONTINUE):
                    if(isinstance(tree.getChild(1).getPayload(), Token) and tree.getChild(1).getPayload().type == CLexer.SEMICOLON):
                        return ContinueStatement();
                    else:
                        raise RuntimeError("Invalid statement: '" + tree.getText() + "'")
                elif(token.type == CLexer.INCLUDE):
                    return self.buildIncludeStatement(tree)
                elif(token.type == CLexer.RETURN):
                    return self.buildReturnStatement(tree)
                elif(token.type == CLexer.LBRACE):
                    return self.buildCompoundStatement(tree)
                elif(token.type == CLexer.WHILE):
                    return self.buildWhileStatement(tree)
                elif(token.type == CLexer.IF):
                    return self.buildIfelseStatement(tree)
                elif(token.type == CLexer.FOR):
                    return self.buildForStatement(tree)
                elif(token.type == CLexer.TYPEDEF):
                    return self.buildTypeDefStatement(tree)
                else:
                    raise RuntimeError("Invalid statement: '" + tree.getText() + "'")
            else:
                token = tree.getChild(1).getPayload()
                if(not isinstance(token, Token)):
                    raise RuntimeError("Invalid statement: '" + tree.getText() + "'")

                if(token.type == CLexer.SEMICOLON):
                    return self.buildExpression(tree.getChild(0))
                elif(token.type == CLexer.IDENTIFIER):
                    return self.buildFunctionStatement(tree)
                else:
                    raise RuntimeError("Invalid statement: '" + tree.getText() + "'")

    def buildIncludeStatement(self, tree):
        """Build Include Statement"""
        # must have 2 children
        if(tree.getChildCount() != 2):
            raise RuntimeError("Invalid include statement: '" + tree.getText() + "'")

        path = tree.getChild(1).getText()
        # check if correct format
        if((path.startswith('"') and path.endswith('"')) or (path.startswith('<') and path.endswith('>'))):
            return IncludeStatement(path)
        else:
            raise RuntimeError("Invalid include statement: '" + tree.getText() + "'")

    def buildReturnStatement(self, tree):
        """Build Return Statement"""
        # must have 2 children
        if(tree.getChildCount() != 2):
            raise RuntimeError("Invalid Return statement: '" + tree.getText() + "'")

        token = tree.getChild(0).getPayload();
        if(not isinstance(token, Token) or token.type != CLexer.RETURN):
            raise RuntimeError("Invalid compund statement: '" + tree.getText() + "'")

        return ReturnStatement(self.buildExpression(tree.getChild(1)))

    def buildCompoundStatement(self, tree):
        """Build Compound Statement"""
        # expects at least 2 children
        if (tree.getChildCount() < 2):
            raise RuntimeError("Invalid compund statement: '" + tree.getText() + "'")

        # expects an RBRACE at the end
        token = tree.getChild(tree.getChildCount() - 1).getPayload();
        if(not isinstance(token, Token)):
            raise RuntimeError("Invalid compund statement: '" + tree.getText() + "'")
        if(token.type != CLexer.RBRACE):
            raise RuntimeError("Invalid compund statement: '" + tree.getText() + "'")

        # Open Scope
        self.sym.openScope()
        # Create list with statements
        statements = []
        for i in range(1, tree.getChildCount() - 1):
            statements.append(self.buildStatement(tree.getChild(i)))

        # Get the used space in this compound statement
        usedSpace = self.sym.getAllocatedSpace()

        # Close Scope
        self.sym.closeScope()

        return CompoundStatement(statements, usedSpace, self.sym)


    def buildFunctionStatement(self, tree):
        """Build Function Statement"""
        # basetype IDENTIFIER LPAREN (VOID|basetype IDENTIFIER? (COMMA basetype IDENTIFIER?)*)? RPAREN (SEMICOLON|LBRACE statement* RBRACE)

        # expects at least 4 children
        if (tree.getChildCount() < 5):
            raise RuntimeError("Invalid function statement: '" + tree.getText() + "'")

        returntype = self.buildType(tree.getChild(0))
        identifier = tree.getChild(1).getText()
        arguments = ArgumentsList()
        statements = []

        # check for LPAREN
        token = tree.getChild(2).getPayload()
        if(not isinstance(token, Token) or token.type != CLexer.LPAREN):
            raise RuntimeError("Invalid function statement: '" + tree.getText() + "'")

        childIndex = 3
        while(True):
            token = tree.getChild(childIndex).getPayload()
            if(isinstance(token, Token)):
                if(token.type == CLexer.RPAREN):
                    # end of parameters list
                    break
                elif(token.type == CLexer.VOID):
                    # Set the type to VOID
                    argumentBasetype = None
                    argumentIdentifier = tree.getChild(childIndex+1).getText()
                    if(argumentIdentifier == None):
                        raise RuntimeError("Invalid compund statement: '" + tree.getText() + "', no identifier for argument")


                    arguments.add(Argument(argumentIdentifier, argumentBasetype))
                    childIndex += 1
                elif(token.type == CLexer.COMMA):
                    # skip
                    childIndex += 1
                elif(token.type == CLexer.IDENTIFIER):
                    # skip
                    childIndex += 1
            else:
                argumentBasetype = self.buildType(tree.getChild(childIndex))
                argumentIdentifier = tree.getChild(childIndex+1).getText()
                if(argumentIdentifier == None):
                    raise RuntimeError("Invalid compund statement: '" + tree.getText() + "', no identifier for argument")


                arguments.add(Argument(argumentIdentifier, argumentBasetype))
                childIndex += 1

        # check for RPAREN
        token = tree.getChild(childIndex).getPayload()
        if(not isinstance(token, Token) or token.type != CLexer.RPAREN):
            raise RuntimeError("Invalid function statement: '" + tree.getText() + "'")

        # Register function in symbol table and open scope
        self.sym.registerFunction(identifier, returntype, arguments, 0)
        self.sym.openScope()
        self.sym.registerArguments(arguments)

        # Check if SEMICOLON(ready) or LBRACE(parse statements)
        childIndex += 1
        token = tree.getChild(childIndex).getPayload()
        if(not isinstance(token, Token)):
            raise RuntimeError("Invalid function statement: '" + tree.getText() + "'")
        else:
            if(token.type == CLexer.SEMICOLON):
                #ready
                pass
            elif(token.type == CLexer.LBRACE):
                # Parse statements
                childIndex += 1
                while(True):
                    token = tree.getChild(childIndex).getPayload()
                    if(isinstance(token, Token) and token.type == CLexer.RBRACE):
                        # end of CompoundStatement
                        break;
                    else:
                        statements.append(self.buildStatement(tree.getChild(childIndex)))
                        childIndex += 1
            else:
                raise RuntimeError("Invalid function statement: '" + tree.getText() + "'")

        # close scope
        self.sym.closeScope()

        return FunctionStatement(returntype, identifier, arguments, statements)

    def buildTypeDefStatement(self, tree):
        """Build Typedef Statement"""
        # expects at least 4 children
        if (tree.getChildCount() < 4):
            raise RuntimeError("Invalid typedef statement: '" + tree.getText() + "'")

        # Check if typedef at front
        token = tree.getChild(0).getPayload()
        if(not isinstance(token, Token) or token.type != CLexer.TYPEDEF):
            raise RuntimeError("Invalid typedef statement: '" + tree.getText() + "'")

        # Check for semicoln at end
        token = tree.getChild(3).getPayload()
        if(not isinstance(token, Token) or token.type != CLexer.SEMICOLON):
            raise RuntimeError("Invalid typedef statement: '" + tree.getText() + "'")

        basetype = self.buildType(tree.getChild(1))
        identifier = tree.getChild(2).getText()

        # Register in symbol Table
        self.sym.registerAlias(identifier, basetype)

        return TypedefStatement(basetype, identifier)

    def buildForStatement(self, tree):
        """Build For Statement"""
        # FOR LPAREN expression? SEMICOLON expression? SEMICOLON expression? RPAREN statement
        if (tree.getChildCount() < 6):
            raise RuntimeError("invalid FOR statement: `" + tree.getText() + "`")

        # Check if FOR at front
        token = tree.getChild(0).getPayload()
        if(not isinstance(token, Token) or token.type != CLexer.FOR):
            raise RuntimeError("Invalid FOR statement: '" + tree.getText() + "'")

        # Check if LPAREN at front
        token = tree.getChild(1).getPayload()
        if(not isinstance(token, Token) or token.type != CLexer.LPAREN):
            raise RuntimeError("Invalid FOR statement: '" + tree.getText() + "'")

        # Check for RPAREN
        token = tree.getChild(tree.getChildCount() - 2).getPayload()
        if(not isinstance(token, Token) or token.type != CLexer.RPAREN):
            raise RuntimeError("Invalid FOR statement: '" + tree.getText() + "'")

        childIndex = 2
        semicolonIndex = 0

        initExpression = Expression(None)
        checkExpression = Expression(None)
        updateExpression = Expression(None)

        while(True):
            token = tree.getChild(childIndex).getPayload()
            if(isinstance(token, Token)):
                if(token.type == CLexer.RPAREN):
                    break
                elif(token.type == CLexer.SEMICOLON):
                    semicolonIndex += 1
                    childIndex += 1

                    if(semicolonIndex > 2):
                        raise RuntimeError("Invalid FOR statement: '" + tree.getText() + "'")
                else:
                    raise RuntimeError("Invalid FOR statement: '" + tree.getText() + "'")
            else:
                if(semicolonIndex == 0):
                    initExpression = self.buildExpression(tree.getChild(childIndex))
                elif(semicolonIndex == 1):
                    checkExpression = self.buildExpression(tree.getChild(childIndex))
                else:
                    updateExpression = self.buildExpression(tree.getChild(childIndex))

                childIndex += 1

        statement = self.buildStatement(tree.getChild(tree.getChildCount() - 1))
        return ForStatement(initExpression, checkExpression, updateExpression, statement, self.sym)

    def buildIfelseStatement(self, tree):
        """Build If/Else Statement"""
        # IF LPAREN expression RPAREN statement (ELSE statement)?
        if (tree.getChildCount() < 5):
            raise RuntimeError("Invalid IFELSE statement: '" + tree.getText() + "'")

        # Check if IF at front
        token = tree.getChild(0).getPayload()
        if(not isinstance(token, Token) or token.type != CLexer.IF):
            raise RuntimeError("Invalid IFELSE statement: '" + tree.getText() + "'")

        # Check if LPAREN at front
        token = tree.getChild(1).getPayload()
        if(not isinstance(token, Token) or token.type != CLexer.LPAREN):
            raise RuntimeError("Invalid IFELSE statement: '" + tree.getText() + "'")

        # Check if RPAREN at end
        token = tree.getChild(3).getPayload()
        if(not isinstance(token, Token) or token.type != CLexer.RPAREN):
            raise RuntimeError("Invalid IFELSE statement: '" + tree.getText() + "'")

        if(tree.getChildCount() == 5):
            # Done, no else clause
            token = tree.getChild(4).getPayload()

            # Build statement
            statement = None
            if(token.getText() != ';'):
                self.sym.openScope()
                statement = self.buildCompoundStatement(tree.getChild(4))
                self.sym.closeScope()


            return IfelseStatement(self.buildExpression(tree.getChild(2)), statement, None, self.sym)

        # we're going on with the else clause, but then we're expecting 7 children
        if (tree.getChildCount() != 7):
            raise RuntimeError("Invalid IFELSE statement: '" + tree.getText() + "'")

        # Build statement
        self.sym.openScope()
        statement = self.buildCompoundStatement(tree.getChild(4))
        self.sym.closeScope()

        # Build alternative statement
        self.sym.openScope()
        alternativeStatement = self.buildCompoundStatement(tree.getChild(6))
        self.sym.closeScope()

        # Check if ELSE at end
        token = tree.getChild(5).getPayload()
        if(not isinstance(token, Token) or token.type != CLexer.ELSE):
            raise RuntimeError("Invalid IFELSE statement: '" + tree.getText() + "'")

        return IfelseStatement(self.buildExpression(tree.getChild(2)), statement, alternativeStatement, self.sym)

    def buildWhileStatement(self, tree):
        """Build While Statement"""
        if (5 != tree.getChildCount()):
            raise RuntimeError("Invalid While statement: '" + tree.getText() + "'")

        # Check if WHILE at front
        token = tree.getChild(0).getPayload()
        if(not isinstance(token, Token) or token.type != CLexer.WHILE):
            raise RuntimeError("Invalid IFELSE statement: '" + tree.getText() + "'")

        # Check if LPAREN at front
        token = tree.getChild(1).getPayload()
        if(not isinstance(token, Token) or token.type != CLexer.LPAREN):
            raise RuntimeError("Invalid IFELSE statement: '" + tree.getText() + "'")

        # Check if RPAREN at end
        token = tree.getChild(3).getPayload()
        if(not isinstance(token, Token) or token.type != CLexer.RPAREN):
            raise RuntimeError("Invalid IFELSE statement: '" + tree.getText() + "'")

        return WhileStatement(self.buildExpression(tree.getChild(2)), self.buildStatement(tree.getChild(4)), self.sym)

    def buildExpression(self, tree):
        """Build Expression"""
        if(tree.getChildCount() == 1):
            # IDENTIFIER
            # TRUE|FALSE|CHAR|NUM|REAL|STRING

            token = tree.getChild(0).getPayload()
            if(not isinstance(token, Token)):
                return self.buildVariableExpression(tree.getChild(0))
            else:
                return self.buildConstantExpression(tree)
        elif(tree.getChildCount() == 2):
            # (MINUS|NOT|AMPERSAND|STAR) expression
            # type IDENTIFIER
            token = tree.getChild(0).getPayload()

            if(isinstance(token, Token)):
                if(token.type == CLexer.MINUS):
                    return self.buildNegateExpression(tree)
                elif(token.type == CLexer.NOT):
                    return self.buildNotExpression(tree)
                elif(token.type == CLexer.AMPERSAND):
                    return self.buildAmpersandExpression(tree)
                elif(token.type == CLexer.STAR):
                    return self.buildStarExpression(tree)
                else:
                    raise RuntimeError("Invalid expression: '" + tree.getText() + "'")
            else:
                token = tree.getChild(1).getPayload();
                if(isinstance(token, Token) and token.type == CLexer.IDENTIFIER):
                    return self.buildVariableExpression(tree)
                else:
                    raise RuntimeError("Invalid expression: '" + tree.getText() + "'")
        elif(tree.getChildCount() == 3):

            token = tree.getChild(1).getPayload()
            token2 = tree.getChild(2).getPayload()
            if(isinstance(token, Token) and isinstance(token2, Token) and token.type == CLexer.PLUS and token2.type == CLexer.PLUS):
                # variable (PLUS PLUS)|(MINUS MINUS)
                return self.buildIncrementerExpression(tree)
            elif(isinstance(token, Token) and isinstance(token2, Token) and token.type == CLexer.MINUS and token2.type == CLexer.MINUS):
                # variable (PLUS PLUS)|(MINUS MINUS)
                return self.buildDecrementerExpression(tree)
            elif(isinstance(token, Token)):
                # IDENTIFIER ASSIGN expression
                # expression MULTIPLY expression
                # expression (ADDITION|SUBTRACTION) expression
                # expression (EQUAL|NOTEQUAL|LESSTHANOREQUAL|GREATERTHANOREQUAL|LESSTHAN|GREATERTHAN) expression
                # expression (AND|OR) expression
                if(token.type == CLexer.ASSIGN):
                    return self.buildAssignmentExpression(tree)
                elif(token.type == CLexer.STAR):
                    return self.buildArithmeticExpression(tree)
                elif(token.type == CLexer.PLUS):
                    return self.buildArithmeticExpression(tree)
                elif(token.type == CLexer.MINUS):
                    return self.buildArithmeticExpression(tree)
                elif(token.type == CLexer.SLASH):
                    return self.buildArithmeticExpression(tree)
                elif(token.type == CLexer.EQUAL):
                    return self.buildComparisonExpression(tree)
                elif(token.type == CLexer.NOTEQUAL):
                    return self.buildComparisonExpression(tree)
                elif(token.type == CLexer.LESSTHANOREQUAL):
                    return self.buildComparisonExpression(tree)
                elif(token.type == CLexer.GREATERTHANOREQUAL):
                    return self.buildComparisonExpression(tree)
                elif(token.type == CLexer.LESSTHAN):
                    return self.buildComparisonExpression(tree)
                elif(token.type == CLexer.GREATERTHAN):
                    return self.buildComparisonExpression(tree)
                elif(token.type == CLexer.AND):
                    return self.buildLogicExpression(tree)
                elif(token.type == CLexer.OR):
                    return self.buildLogicExpression(tree)
                elif(token.type == CLexer.LPAREN):
                    return self.buildFunctionCallExpression(tree)
                else:
                    raise RuntimeError("Invalid expression: '" + tree.getText() + "'")
            else:
                # LPAREN expression RPAREN
                # Check for expression in expresison
                token = tree.getChild(0).getPayload()
                if(not isinstance(token, Token) or token.type != CLexer.LPAREN):
                    raise RuntimeError("Invalid expression statement: '" + tree.getText() + "'")

                token = tree.getChild(2).getPayload()
                if(not isinstance(token, Token) or token.type != CLexer.RPAREN):
                    raise RuntimeError("Invalid expression statement: '" + tree.getText() + "'")

                return self.buildExpression(tree.getChild(1))
        else:
            # Check for function call - IDENTIFIER LPAREN (expression (COMMA expression)*)? RPAREN
            token = tree.getChild(1).getPayload()
            if(not isinstance(token, Token) or token.type != CLexer.LPAREN):
                raise RuntimeError("Invalid expression statement: '" + tree.getText() + "'")

            token = tree.getChild(tree.getChildCount() - 1).getPayload()
            if(not isinstance(token, Token) or token.type != CLexer.RPAREN):
                raise RuntimeError("Invalid expression statement: '" + tree.getText() + "'")

            return self.buildFunctionCallExpression(tree)

    def buildArithmeticExpression(self, tree):
        """Build Arithmetic Expression"""
        # expects 3 children
        if (3 != tree.getChildCount()):
            raise RuntimeError("Invalid ArithmeticExpression: '" + tree.getText() + "'")

        token = tree.getChild(1).getPayload();
        if(not isinstance(token, Token)):
            raise RuntimeError("Invalid ArithmeticExpression: '" + tree.getText() + "'")

        leftExpression = self.buildExpression(tree.getChild(0))
        rightExpression = self.buildExpression(tree.getChild(2))

        if(token.type == CLexer.STAR):
            return ArithmeticExpression(leftExpression, rightExpression, "*")
        elif(token.type == CLexer.SLASH):
            return ArithmeticExpression(leftExpression, rightExpression, "/")
        elif(token.type == CLexer.PLUS):
            return ArithmeticExpression(leftExpression, rightExpression, "+")
        elif(token.type == CLexer.MINUS):
            return ArithmeticExpression(leftExpression, rightExpression, "-")
        else:
            raise RuntimeError("Invalid ArithmeticExpression: '" + tree.getText() + "'")

    def buildComparisonExpression(self, tree):
        """Build Comparison Expression"""
        # expects 3 children
        if (3 != tree.getChildCount()):
            raise RuntimeError("Invalid ComparisonExpression: '" + tree.getText() + "'")

        token = tree.getChild(1).getPayload();
        if(not isinstance(token, Token)):
            raise RuntimeError("Invalid ComparisonExpression: '" + tree.getText() + "'")

        leftExpression = self.buildExpression(tree.getChild(0))
        rightExpression = self.buildExpression(tree.getChild(2))

        if(token.type == CLexer.EQUAL):
            return ComparisonExpression(leftExpression, rightExpression, "==")
        elif(token.type == CLexer.NOTEQUAL):
            return ComparisonExpression(leftExpression, rightExpression, "!=")
        elif(token.type == CLexer.LESSTHAN):
            return ComparisonExpression(leftExpression, rightExpression, "<")
        elif(token.type == CLexer.GREATERTHAN):
            return ComparisonExpression(leftExpression, rightExpression, ">")
        elif(token.type == CLexer.LESSTHANOREQUAL):
            return ComparisonExpression(leftExpression, rightExpression, "<=")
        elif(token.type == CLexer.GREATERTHANOREQUAL):
            return ComparisonExpression(leftExpression, rightExpression, ">=")
        else:
            raise RuntimeError("Invalid ComparisonExpression: '" + tree.getText() + "'")

    def buildLogicExpression(self, tree):
        """Build Logic Expression"""
        # expects 3 children
        if (3 != tree.getChildCount()):
            raise RuntimeError("Invalid LogicExpression: '" + tree.getText() + "'")

        token = tree.getChild(1).getPayload();
        if(not isinstance(token, Token)):
            raise RuntimeError("Invalid LogicExpression: '" + tree.getText() + "'")

        leftExpression = self.buildExpression(tree.getChild(0))
        rightExpression = self.buildExpression(tree.getChild(2))

        if(token.type == CLexer.AND):
            return LogicExpression(leftExpression, rightExpression, "&&")
        elif(token.type == CLexer.ORD):
            return LogicExpression(leftExpression, rightExpression, "||")
        else:
            raise RuntimeError("Invalid LogicExpression: '" + tree.getText() + "'")

    def buildConstantExpression(self, tree):
        """Build Constant Expression"""
        if (1 != tree.getChildCount()):
            raise RuntimeError("Invalid ConstantExpression: '" + tree.getText() + "'")

        token = tree.getChild(0).getPayload();
        if(not isinstance(token, Token)):
            raise RuntimeError("Invalid ConstantExpression: '" + tree.getText() + "'")

        if(token.type == CLexer.TRUE):
            return ConstantExpression(True, 'bool')
        elif(token.type == CLexer.FALSE):
            return ConstantExpression(False, 'bool')
        elif(token.type == CLexer.CHAR):
            return ConstantExpression(tree.getChild(0).getText()[0], 'char')
        elif(token.type == CLexer.NUM):
            return ConstantExpression(int(tree.getChild(0).getText()), 'int')
        elif(token.type == CLexer.REAL):
            return ConstantExpression(float(tree.getChild(0).getText()), 'float')
        elif(token.type == CLexer.STRING):
            return ConstantExpression(tree.getChild(0).getText()[1:-1], 'string')
        else:
            raise RuntimeError("Invalid ConstantExpression: '" + tree.getText() + "'")

    def buildIncrementerExpression(self, tree):
        """Build Incrementer Expression"""
        if (3 != tree.getChildCount()):
            raise RuntimeError("Invalid IncrementerExpression: '" + tree.getText() + "'")

        token = tree.getChild(1).getPayload()
        if(not isinstance(token, Token) or token.type != CLexer.PLUS):
            raise RuntimeError("Invalid IncrementerExpression: '" + tree.getText() + "'")

        token = tree.getChild(2).getPayload()
        if(not isinstance(token, Token) or token.type != CLexer.PLUS):
            raise RuntimeError("Invalid IncrementerExpression: '" + tree.getText() + "'")

        return IncrementerExpression(self.buildVariableExpression(tree.getChild(0)))

    def buildDecrementerExpression(self, tree):
        """Build Decrementer Expression"""
        if (3 != tree.getChildCount()):
            raise RuntimeError("Invalid DecrementerExpression: '" + tree.getText() + "'")

        token = tree.getChild(1).getPayload()
        if(not isinstance(token, Token) or token.type != CLexer.MINUS):
            raise RuntimeError("Invalid DecrementerExpression: '" + tree.getText() + "'")

        token = tree.getChild(2).getPayload()
        if(not isinstance(token, Token) or token.type != CLexer.MINUS):
            raise RuntimeError("Invalid DecrementerExpression: '" + tree.getText() + "'")

        return DecrementerExpression(self.buildVariableExpression(tree.getChild(0)))

    def buildNegateExpression(self, tree):
        """Build Negate Expression"""
        if (2 != tree.getChildCount()):
            raise RuntimeError("Invalid NegateExpression: '" + tree.getText() + "'")

        token = tree.getChild(0).getPayload()
        if(not isinstance(token, Token) or token.type != CLexer.MINUS):
            raise RuntimeError("Invalid NegateExpression: '" + tree.getText() + "'")

        return NegateExpression(self.buildExpression(tree.getChild(1)))

    def buildNotExpression(self, tree):
        """Build Not Expression"""
        if (2 != tree.getChildCount()):
            raise RuntimeError("Invalid NotExpression: '" + tree.getText() + "'")

        token = tree.getChild(0).getPayload()
        if(not isinstance(token, Token) or token.type != CLexer.NOT):
            raise RuntimeError("Invalid NotExpression: '" + tree.getText() + "'")

        return NotExpression(self.buildExpression(tree.getChild(1)))

    def buildStarExpression(self, tree):
        """Build Star Expression"""
        if (2 != tree.getChildCount()):
            raise RuntimeError("Invalid StarExpression: '" + tree.getText() + "'")

        token = tree.getChild(0).getPayload()
        if(not isinstance(token, Token) or token.type != CLexer.STAR):
            raise RuntimeError("Invalid StarExpression: '" + tree.getText() + "'")

        return StarExpression(self.buildExpression(tree.getChild(1)))

    def buildAmpersandExpression(self, tree):
        """Build Ampersand Expression"""
        if (2 != tree.getChildCount()):
            raise RuntimeError("Invalid AmpersandExpression: '" + tree.getText() + "'")

        token = tree.getChild(0).getPayload()
        if(not isinstance(token, Token) or token.type != CLexer.AMPERSAND):
            raise RuntimeError("Invalid AmpersandExpression: '" + tree.getText() + "'")

        return AmpersandExpression(self.buildExpression(tree.getChild(1)))

    def buildVariableExpression(self, tree):
        """Build Variable Expression"""
        if(tree.getChildCount() == 1):
            # Variable call
            symbol = tree.getChild(0).getText()
            # Check symbol Table if symbol exists
            variable = self.sym.getSymbol(symbol)

            return VariableCallExpression(symbol, variable.basetype,  None)
        elif(tree.getChildCount() == 2):
            # Variable Definition
            basetype = self.buildType(tree.getChild(0))
            symbol = tree.getChild(1).getText()
            # Register in Symbol Table
            self.sym.registerSymbol(symbol, basetype)

            return VariableExpression(basetype, symbol, None)
        elif(tree.getChildCount() == 4):
            # Array
            token = tree.getChild(1).getPayload()
            if(not isinstance(token, Token) or token.type != CLexer.LSQUAREBRACKET):
                raise RuntimeError("Invalid VariableExpression: '" + tree.getText() + "'")

            token = tree.getChild(3).getPayload()
            if(not isinstance(token, Token) or token.type != CLexer.RSQUAREBRACKET):
                raise RuntimeError("Invalid VariableExpression: '" + tree.getText() + "'")

            if(tree.getChild(0).getChildCount() == 1):
                # call
                symbol = tree.getChild(0).getChild(0).getText()
                index = self.buildExpression(tree.getChild(2))

                # Check symbol Table if symbol exists
                variable = self.sym.getSymbol(symbol)

                return VariableCallExpression(symbol, variable.basetype, index)
            elif(tree.getChild(0).getChildCount() == 2):
                # definition
                basetype = self.buildType(tree.getChild(0).getChild(0))
                symbol = tree.getChild(0).getChild(1).getText()
                arraySize = self.buildExpression(tree.getChild(2))
                # Register in Symbol Table
                self.sym.registerSymbol(symbol, basetype)
                return VariableExpression(basetype, symbol, arraySize)
            else:
                raise RuntimeError("Invalid VariableExpression: '" + tree.getText() + "'")
        else:
            raise RuntimeError("Invalid VariableExpression: '" + tree.getText() + "'")

    def buildAssignmentExpression(self, tree):
        """Build Assignment Expression"""
        if (3 != tree.getChildCount()):
            raise RuntimeError("Invalid AssignmentExpression: '" + tree.getText() + "'")

        token = tree.getChild(1).getPayload()
        if(not isinstance(token, Token) or token.type != CLexer.ASSIGN):
            raise RuntimeError("Invalid VariableExpression: '" + tree.getText() + "'")

        return AssignmentExpression(self.buildVariableExpression(tree.getChild(0)), self.buildExpression(tree.getChild(2)))

    def buildFunctionCallExpression(self, tree):
        """Build Functioncall Expression"""
        # IDENTIFIER LPAREN (expression (COMMA expression)*)? RPAREN
        if (3 > tree.getChildCount()):
            raise RuntimeError("Invalid FunctionCallExpression: '" + tree.getText() + "'")

        token = tree.getChild(1).getPayload()
        if(not isinstance(token, Token) or token.type != CLexer.LPAREN):
            raise RuntimeError("Invalid FunctionCallExpression statement: '" + tree.getText() + "'")

        token = tree.getChild(tree.getChildCount() - 1).getPayload()
        if(not isinstance(token, Token) or token.type != CLexer.RPAREN):
            raise RuntimeError("Invalid FunctionCallExpression statement: '" + tree.getText() + "'")



        # Function call
        childIndex = 2
        parameters = ParametersList()
        identifier = tree.getChild(0).getText()
        while(True):
            token = tree.getChild(childIndex).getPayload()
            if(isinstance(token, Token)):
                if(token.type == CLexer.RPAREN):
                    break
                elif(token.type == CLexer.COMMA):
                    childIndex += 1
                else:
                    raise RuntimeError("Invalid FunctionCallExpression statement: '" + tree.getText() + "'")
            else:
                parameter = Parameter(self.buildExpression(tree.getChild(childIndex)))
                parameters.add(parameter)
                childIndex += 1

        # Check symbol table
        function = self.sym.getFunction(identifier, parameters)

        return FunctionCallExpression(identifier, function.returntype, parameters)

    def buildType(self, tree):
        """Build Type"""
        token = None
        basetype = None

        if(tree.getChildCount() == 1):
            token = tree.getChild(0).getPayload();

            if(not isinstance(token, Token)):
                raise RuntimeError("Invalid type identifier: '" + tree.getText() + "'")

            if(token.type == CLexer.VOID):
                return None
            elif(token.type == CLexer.IDENTIFIER):
                if(tree.getChild(0).getText() == "bool"):
                    return BooleanType()
                elif(tree.getChild(0).getText() == "char"):
                    return CharacterType()
                elif(tree.getChild(0).getText() == "int"):
                    return IntegerType()
                elif(tree.getChild(0).getText() == "float"):
                    return RealType()
                elif(tree.getChild(0).getText() == "double"):
                    return RealType()
                else:
                    # Alias, check the symbol Table
                    return self.sym.getAlias(tree.getChild(0).getText()).basetype
            else:
                raise RuntimeError("Invalid type identifier: '" + tree.getText() + "'")
        elif(tree.getChildCount() == 2):
            token = tree.getChild(0).getPayload();

            # Const Type
            if(isinstance(token, Token) and token.type == CLexer.CONST):
                return self.buildType(tree.getChild(1)).setConst(True)

            token = tree.getChild(1).getPayload()
            if(not isinstance(token, Token)):
                raise RuntimeError("Invalid type identifier: '" + tree.getText() + "'")

            if(token.type == CLexer.STAR):
                return AddressType(self.buildType(tree.getChild(0)))
            elif(token.type == CLexer.CONST):
                return self.buildType(tree.getChild(0)).setConst(True)
            else:
                raise RuntimeError("Invalid type identifier: '" + tree.getText() + "'")
        else:
            raise RuntimeError("Invalid type identifier: '" + tree.getText() + "'")
