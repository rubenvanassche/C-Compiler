from src.AST.Expression import Expression

class AmpersandExpression(Expression):
    """Node For AmpersandExpression in AST"""
    def __init__(self, expression):
        Expression.__init__(self, None)
        self.expression = expression

        self.basetype = self.expression.basetype

    def __str__(self):
        return "Ampersand(" + str(self.expression) + ")"

    def serialize(self, level):
        return "ampersand(" + self.expression.serialize(0) + ")"

    def compile(self):
        return "ldc a"
