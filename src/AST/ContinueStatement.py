from src.AST.Statement import Statement

class ContinueStatement(Statement):
    """Node For ContinueStatement in AST"""

    def __init__(self):
        Statement.__init__(self)

    def __str__(self):
        return "Continue\n"

    def compile(self):
        self.sym.getBeginLoop()

    def serialize(self, level):
        return  self.s(level) + "continue \n"
