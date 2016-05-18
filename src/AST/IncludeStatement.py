from src.AST.Statement import Statement

class IncludeStatement(Statement):
    """Node For IncludeStatement in AST"""

    def __init__(self, path):
        Statement.__init__(self)
        self.path = path[1:-1]

    def __str__(self):
        return "IncludeStatement(" + self.path + ")"

    def compile(self):
        return ""

    def serialize(self, level):
        return "Include(" + self.path + ")\n"
