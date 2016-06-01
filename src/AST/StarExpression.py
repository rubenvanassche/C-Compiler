from src.AST.Expression import Expression
from src.utils import *

class StarExpression(Expression):
    """Node For StarExpression in AST"""

    def __init__(self, expression):
        Expression.__init__(self, None)
        self.expression = expression

        self.basetype = self.expression.basetype

    def __str__(self):
        return "Star(" + str(self.expression) + ")"

    def compile(self):
        return "ind a\n"

    def serialize(self, level):
        out = padding(level) + "StarExpression\n"
        out += self.expression.serialize(level + 1)

        return out
