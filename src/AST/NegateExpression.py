from src.AST.Expression import Expression
from src.utils import *

class NegateExpression(Expression):
    """Node For NegateExpression in AST"""

    def __init__(self, expression):
        Expression.__init__(self, None)
        self.expression = expression

        self.basetype = self.expression.basetype

    def __str__(self):
        return "-" + str(self.expression)

    def compile(self):
        output = self.expression.compile()
        output += "neg " + self.basetype.getPcode() + "\n"

        return output

    def serialize(self, level):
        out = padding(level) + "NegateExpression\n"
        out += self.expression.serialize(level + 1)

        return out
