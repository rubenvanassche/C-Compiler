from Expression import Expression

class StarExpression(Expression):

    def __init__(self, expression):
        self.expression = expression

    def __str__(self):
        return "StarExpression"

    def compile(self):
        return ""
