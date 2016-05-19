from src.AST.Expression import Expression

class NotExpression(Expression):
    """Node For NotExpression in AST"""

    def __init__(self, expression):
        Expression.__init__(self)
        self.expression = expression

    def __str__(self):
        return "!" + str(self.expression)

    def compile(self):
        return ""

    def serialize(self, level):
        return "!" + self.expression.serialize(0)