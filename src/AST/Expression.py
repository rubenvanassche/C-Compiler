from src.AST.Statement import Statement
from src.utils import *

class Expression(Statement):
    """Node For Expression in AST"""

    def __init__(self, basetype):
        Statement.__init__(self)
        self.basetype = basetype

    def __str__(self):
        return "Expression"

    def compile(self):
        return ""

    def serialize(self, level):
        return "Expression"
