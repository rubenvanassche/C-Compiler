from Expression import Expression

class ConstantExpression(Expression):

    def __init__(self, value):
        self.value = value

    def __str__(self):
        return "ConstantExpression"

    def compile(self):
        return ""
