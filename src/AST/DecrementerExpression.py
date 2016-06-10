from src.AST.Expression import Expression
from src.utils import *

class DecrementerExpression(Expression):
    """Node For DecrementerExpression in AST"""

    def __init__(self, variable):
        Expression.__init__(self, None)
        self.variable = variable

        self.basetype = self.variable.basetype

    def __str__(self):
        return str(self.variable) + "--"

    def compile(self):
        output = self.variable.compile()
        output += "dec " + self.basetype.getPcode() + " 1\n"

        return output

    def serialize(self, level):
        out = padding(level) + "DecrementerExpression\n"
        out += self.variable.serialize(level + 1)

        return out
