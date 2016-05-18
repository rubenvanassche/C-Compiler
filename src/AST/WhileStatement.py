from src.AST.Statement import Statement

class WhileStatement(Statement):
    """Node For WhileStatement in AST"""

    def __init__(self, expression, statement):
        Statement.__init__(self)
        self.expression = expression
        self.statement = statement

    def __str__(self):
        out = "While(" + str(self.expression) + ")\n"
        out += "    " + str(self.statement) + "\n"

        return out
    def compile(self):
        self.expression.compile()

        self.sym.openLoop()

        self.statement.compile()

        begin = self.sym.getBeginLoop()
        end = self.sym.getEndLoop()

        self.sym.closeLoop()

    def serialize(self, level):
        out = "While(" + self.expression.serialize(0) + ")\n"
        out += self.s(level) + self.statement.serialize(level + 1) + "\n"
