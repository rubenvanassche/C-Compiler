from src.AST.Expression import Expression

class IncrementerExpression(Expression):
    """Node For IncrementerExpression in AST"""

    def __init__(self, variable):
        Expression.__init__(self, None)
        self.variable = variable

    def __str__(self):
        return str(self.variable) + "++"

    def compile(self):
        return ""

    def serialize(self, level):
        return "increment(" + self.variable.serialize(0) + ")"
