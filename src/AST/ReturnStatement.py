from src.AST.Statement import Statement
from src.utils import *

class ReturnStatement(Statement):
    """Node For ReturnStatement in AST"""

    def __init__(self, expression):
        Statement.__init__(self)
        self.expression = expression

    def __str__(self):
        return "return: " + str(self.expression) + "\n"

    def compile(self):
        return "Todo: return \n"

    def serialize(self, level):
        out = padding(level) + "ReturnStatement\n"
        out += self.expression.serialize(level + 1)

        return out
