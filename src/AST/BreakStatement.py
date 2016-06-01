from src.AST.Statement import Statement
from src.utils import *

class BreakStatement(Statement):
    """Node For BreakStatement in AST"""

    def __init__(self):
        pass

    def __str__(self):
        return "Break\n"

    def compile(self):
        return "ujp" + self.sym.getEndLoop() + "\n"

    def serialize(self, level):
        out = padding(level) + "BreakStatement\n"

        return out
