from src.AST.Statement import Statement
from src.utils import *

from src.Type.VoidType import VoidType

class ReturnStatement(Statement):
    """Node For ReturnStatement in AST"""

    def __init__(self, expression):
        Statement.__init__(self)
        self.expression = expression

        if(type(self.expression) != type(VoidType())):
            self.basetype = self.expression.basetype
        else:
            self.basetype = self.expression

    def __str__(self):
        return "return: " + str(self.expression) + "\n"

    def compile(self):
        if(type(self.basetype) != type(VoidType())):
            code = self.expression.compile()
            code += "str " + self.basetype.getPcode() + " 0 0\n"
            code += "retf\n"
            code += "retp\n"
            return code
        else:
            return "retp\n"

    def serialize(self, level):
        out = padding(level) + "ReturnStatement\n"
        out += self.expression.serialize(level + 1)

        return out
