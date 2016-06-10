from src.AST.Statement import Statement
from src.utils import *

class CompoundStatement(Statement):
    """Node For CompoundStatement in AST"""

    def __init__(self, statements):
        Statement.__init__(self)
        self.statements = statements


    def __str__(self):
        out = ""
        for statement in self.statements:
            out += "   " + str(statement) + "\n"

        return out

    def compile(self):
        if(len(self.statements) == 0):
            return ""

        code = ""
        for statement in self.statements:
            code += statement.compile()

        return code

    def serialize(self, level):
        out = ""
        for statement in self.statements:
            out += padding(level) + statement.serialize(level + 1) + "\n"
        return out
