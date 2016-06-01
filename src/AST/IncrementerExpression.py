from src.AST.Expression import Expression
from src.utils import *

class IncrementerExpression(Expression):
    """Node For IncrementerExpression in AST"""

    def __init__(self, variable):
        Expression.__init__(self, None)
        self.variable = variable

        self.basetype = self.variable.basetype

    def __str__(self):
        return str(self.variable) + "++"

    def compile(self):
        return "Todo:incrementer\n"

    def serialize(self, level):
        out = padding(level) + "IncrementerExpression\n"
        out += self.variable.serialize(level + 1)

        return out
