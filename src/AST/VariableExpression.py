from Expression import Expression

class VariableExpression(Expression):

    def __init__(self,  symbol):
        self.symbol = symbol

    def __init__(self, basetype, symbol):
        self.basetype = basetype
        self.symbol = symbol

    def __str__(self):
        return "VariableExpression"

    def compile(self):
        return ""
