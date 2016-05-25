from src.AST.Expression import Expression

class StarExpression(Expression):
    """Node For StarExpression in AST"""

    def __init__(self, expression):
        Expression.__init__(self, None)
        self.expression = expression

    def __str__(self):
        return "Star(" + str(self.expression) + ")"

    def compile(self):
        return ""

    def serialize(self, level):
        return "star(" + self.expression.serialize(0) + ")"
