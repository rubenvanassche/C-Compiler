from src.AST.Expression import Expression
from src.utils import *

class NotExpression(Expression):
    """Node For NotExpression in AST"""

    def __init__(self, expression):
        Expression.__init__(self, None)
        self.expression = expression

        self.basetype = self.expression.basetype

    def __str__(self):
        return "!" + str(self.expression)

    def compile(self):
        return self.expression.compile() + "not\n"

    def serialize(self, level):
        out = padding(level) + "NotExpression\n"
        out += self.expression.serialize(level + 1)

        return out
