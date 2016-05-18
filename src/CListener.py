# Generated from C.g4 by ANTLR 4.5.3
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .CParser import CParser
else:
    from CParser import CParser

# This class defines a complete listener for a parse tree produced by CParser.
class CListener(ParseTreeListener):

    # Enter a parse tree produced by CParser#program.
    def enterProgram(self, ctx:CParser.ProgramContext):
        pass

    # Exit a parse tree produced by CParser#program.
    def exitProgram(self, ctx:CParser.ProgramContext):
        pass


    # Enter a parse tree produced by CParser#statement.
    def enterStatement(self, ctx:CParser.StatementContext):
        pass

    # Exit a parse tree produced by CParser#statement.
    def exitStatement(self, ctx:CParser.StatementContext):
        pass


    # Enter a parse tree produced by CParser#expression.
    def enterExpression(self, ctx:CParser.ExpressionContext):
        pass

    # Exit a parse tree produced by CParser#expression.
    def exitExpression(self, ctx:CParser.ExpressionContext):
        pass


    # Enter a parse tree produced by CParser#variable.
    def enterVariable(self, ctx:CParser.VariableContext):
        pass

    # Exit a parse tree produced by CParser#variable.
    def exitVariable(self, ctx:CParser.VariableContext):
        pass


    # Enter a parse tree produced by CParser#basetype.
    def enterBasetype(self, ctx:CParser.BasetypeContext):
        pass

    # Exit a parse tree produced by CParser#basetype.
    def exitBasetype(self, ctx:CParser.BasetypeContext):
        pass


