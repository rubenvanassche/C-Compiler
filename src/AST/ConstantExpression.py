from src.AST.Expression import Expression

class ConstantExpression(Expression):
    """Node For ConstantExpression in AST"""

    def __init__(self, value):
        Expression.__init__(self)
        self.value = value

    def __str__(self):
        return "constant(" + str(self.value) + ")"

    def compile(self):
        return ""

    def serialize(self, level):
        return "value(" + str(self.value) + ")"
