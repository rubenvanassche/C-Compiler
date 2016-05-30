from src.AST.Expression import Expression

class NegateExpression(Expression):
    """Node For NegateExpression in AST"""

    def __init__(self, expression):
        Expression.__init__(self, None)
        self.expression = expression

        self.basetype = self.expression.basetype

    def __str__(self):
        return "-" + str(self.expression)

    def compile(self):
        return "Todo:negate expresison \n"

    def serialize(self, level):
        return "-" + self.expression.serialize(0)
