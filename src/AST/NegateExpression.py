from src.AST.Expression import Expression

class NegateExpression(Expression):
    """Node For NegateExpression in AST"""

    def __init__(self, expression):
        Expression.__init__(self, None)
        self.expression = expression

    def __str__(self):
        return "-" + str(self.expression)

    def compile(self):
        return ""

    def serialize(self, level):
        return "-" + self.expression.serialize(0)
