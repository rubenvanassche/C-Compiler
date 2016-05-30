from src.AST.Statement import Statement
from src.Type.BooleanType import BooleanType

class IfelseStatement(Statement):
    """Node For IfelseStatement in AST"""

    def __init__(self, expression, statement, symbolTable):
        Statement.__init__(self)
        self.expression = expression
        self.statement = statement
        self.alternativeStatement = None
        self.symbolTable = symbolTable

    def __init__(self, expression, statement, alternativeStatement, symbolTable):
        Statement.__init__(self)
        self.expression = expression
        self.statement = statement
        self.alternativeStatement = alternativeStatement
        self.symbolTable = symbolTable

    def __str__(self):
        out =  "If(" + str(self.expression) + ")\n"
        out += "    " + str(self.statement) + "\n"
        if(self.alternativeStatement != None):
            out += "Else\n"
            out += "    " +  str(self.alternativeStatement) + "\n"

        return out

    def compile(self):
        # Check if expression is an boolean type
        if(type(self.expression.basetype) != type(BooleanType())):
            raise RuntimeError("The expression in the if clause should be of an boolean type")

        # Open scope
        self.symbolTable.openScope()

        endif = self.sym.createLabel()
        endelse = self.sym.createLabel()

        # Compile expression and jump if needed
        code = self.expression.compile()
        code += "fjp " + endif + "\n"

        # compile the statement to execute
        code += self.statement.compile()

        # need to jump to the end of ELSE if there's an alternative
        if(self.alternativeStatement != None):
            code += "ujp " + endelse + "\n"

        # Mark end if code
        code += endif + ":\n"

        # end scope if
        self.symboltable.closeScope()

        # Stop if no alternative statement
        if(self.alternativeStatement == None):
            return code

        # Compile alternative statement
        self.symbolTable.openScope()
            code += self.alternative.compile()
            code += endelse + ":\n"
        self.symbolTable.closeScope()

        return code
    def serialize(self, level):
        out =  "If(" + self.expression.serialize(0) + ")\n:"
        out += statement.serialize(index) + "\n"
        if(self.alternativeStatement != None):
            out += "Else\n:"
            out += alternativeStatement.serialize(index) + "\n"

        return out
