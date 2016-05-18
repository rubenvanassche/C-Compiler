from src.AST.Expression import Expression

class DecrementerExpression(Expression):
    """Node For DecrementerExpression in AST"""

    def __init__(self, variable):
        Expression.__init__(self)
        self.variable = variable

    def __str__(self):
        return str(self.variable) + "--"

    def compile(self):
        return ""

    def serialize(self, level):
        return "decrement(" + self.variable.serialize(0) + ")"
