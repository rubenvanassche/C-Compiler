from src.AST.Statement import Statement

class Expression(Statement):
    """Node For Expression in AST"""

    def __init__(self):
        Statement.__init__(self)

    def __str__(self):
        return "Expression"

    def compile(self):
        return ""

    def serialize(self, level):
        pass
