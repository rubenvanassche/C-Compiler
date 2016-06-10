from src.AST.Statement import Statement
from src.Type.BooleanType import BooleanType
from src.utils import *

class ForStatement(Statement):
    """Node For ForStatement in AST"""

    def __init__(self, initExpression, checkExpression, updateExpression, statement, sym):
        Statement.__init__(self)
        self.initExpression = initExpression
        self.checkExpression = checkExpression
        self.updateExpression = updateExpression
        self.statement = statement
        self.sym = sym

    def __str__(self):
        out = "For(" + str(self.initExpression) + ", " + str(self.checkExpression) + ", " + str(self.updateExpression) + ")\n"
        out += "    " + str(self.statement)

        return out

    def compile(self):
        self.sym.openLoop()

        # Get begin and end label
        begin = self.sym.getBeginLoop()
        end = self.sym.getEndLoop()

        code = ""

        # compile the initial expression
        if(self.initExpression != None):
            code += self.initExpression.compile()

        # Mark begin of loop
        code = str(begin) + ":\n"

        # Check if check is an boolean Expression
        if(type(self.checkExpression.basetype) != type(BooleanType())):
            raise RuntimeError("Check condition in for loop should be of boolean type")

        # Compile check
        code += self.checkExpression.compile()
        code += "fjp " + str(end) + "\n"

        # Compile the statement
        code += self.statement.compile()

        # compile the update
        code += self.updateExpression.compile()

        # Jump to begin with unconditional Jump
        code += "ujp " + str(begin) + "\n"

        # Mark end of for loop
        code += str(end) + ":\n"

        self.sym.closeLoop()

        return code


    def serialize(self, level):
        out = padding(level) + "ForStatement\n"
        if(self.initExpression != None):
            out += padding(level + 1) + "->init: \n" + self.initExpression.serialize(level + 1) + "\n"
        if(self.checkExpression != None):
            out += padding(level + 1) + "->check: \n" + self.checkExpression.serialize(level + 1) + "\n"
        if(self.updateExpression != None):
            out += padding(level + 1) + "->update: \n" + self.updateExpression.serialize(level + 1) + "\n"
        if(self.statement != None):
            out += padding(level + 1) + "->statements: \n" + self.statement.serialize(level + 1)

        return out
