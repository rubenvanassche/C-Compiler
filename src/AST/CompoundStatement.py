from src.AST.Statement import Statement

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
        self.sym.openScope()
        for statement in self.statements:
            statement.compile()
        self.sym.closeScope()

    def serialize(self, level):
        out = ""
        for statement in self.statements:
            out += self.s(level) + statement.serialize(level + 1) + "\n"
        return out
