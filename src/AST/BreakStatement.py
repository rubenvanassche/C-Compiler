from src.AST.Statement import Statement

class BreakStatement(Statement):
    """Node For BreakStatement in AST"""

    def __init__(self):
        pass

    def __str__(self):
        return "Break\n"

    def compile(self):
        self.sym.getEndLoop()


    def serialize(self, level):
        return  self.s(level) + "break \n"
