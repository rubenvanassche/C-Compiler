from Expression import Expression

class AmpersandExpression(Expression):
    def __init__(self, expression):
        self.expression = expression

    def __str__(self):
        return "AmpersandExpression"
