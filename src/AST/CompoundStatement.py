from src.AST.Statement import Statement

class CompoundStatement(Statement):
    """Node For CompoundStatement in AST"""

    def __init__(self, statements, usedSpace, sym):
        Statement.__init__(self)
        self.statements = statements
        self.usedSpace = usedSpace
        self.sym = sym

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

        return "ssp " + str(self.usedSpace) + "\n" + code + "ssp " +  str(self.sym.getAllocatedSpace()) + "\n"

    def serialize(self, level):
        out = ""
        for statement in self.statements:
            out += self.s(level) + statement.serialize(level + 1) + "\n"
        return out
