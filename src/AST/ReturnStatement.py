from src.AST.Statement import Statement

class ReturnStatement(Statement):
    """Node For ReturnStatement in AST"""

    def __init__(self, expression):
        Statement.__init__(self)
        self.expression = expression

    def __str__(self):
        return "return: " + str(self.expression) + "\n"

    def compile(self):
        return ""

    def serialize(self, level):
        return "return(" + self.expression.serialize(0) + ")\n"
