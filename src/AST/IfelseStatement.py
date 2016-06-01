from src.AST.Statement import Statement
from src.Type.BooleanType import BooleanType
from src.utils import *

class IfelseStatement(Statement):
    """Node For IfelseStatement in AST"""

    def __init__(self, expression, statement, sym):
        Statement.__init__(self)
        self.expression = expression
        self.statement = statement
        self.alternativeStatement = None
        self.sym = sym

    def __init__(self, expression, statement, alternativeStatement, sym):
        Statement.__init__(self)
        self.expression = expression
        self.statement = statement
        self.alternativeStatement = alternativeStatement
        self.sym = sym

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
        self.sym.openScope()

        endif = self.sym.createLabel()
        endelse = self.sym.createLabel()

        # Compile expression and jump if needed
        code = self.expression.compile()
        code += "fjp " + str(endif) + "\n"

        # compile the statement to execute if existing
        if(self.statement != None):
            code += self.statement.compile()

        # need to jump to the end of ELSE if there's an alternative
        if(self.alternativeStatement != None):
            code += "ujp " + str(endelse) + "\n"

        # Mark end if code
        code += str(endif) + ":\n"

        # end scope if
        self.sym.closeScope()

        # Stop if no alternative statement
        if(self.alternativeStatement == None):
            return code

        # Compile alternative statement
        self.sym.openScope()
        code += self.alternativeStatement.compile()
        code += str(endelse) + ":\n"
        self.sym.closeScope()

        return code
    def serialize(self, level):
        out = ""
        if self.expression != None:
            out += padding(level) + "IF:\n"
            out += self.expression.serialize(level + 1)
        else:
            out += "IF\n"

        if self.statement != None:
            out += "THEN:\n"
            out += self.statement.serialize(level + 1)
        else:
            out += "THEN\n"

        if self.alternativeStatement != None:
            out += "ELSE:\n"
            out += self.alternativeStatement.serialize(level + 1)


        return out
