from src.AST.Statement import Statement
from src.utils import *

class TypedefStatement(Statement):
    """Node For TypedefStatement in AST"""

    def __init__(self, basetype, identifier):
        Statement.__init__(self)
        self.basetype = basetype
        self.identifier = identifier

    def __str__(self):
        return "Typedef " + str(self.basetype) + " -> " + str(self.identifier) + "\n"

    def compile(self):
        return ""

    def serialize(self, level):
        out = padding(level) + "Typedef(" + self.identifier + ")\n"
        out += self.basetype.serialize(level + 1)

        return out
