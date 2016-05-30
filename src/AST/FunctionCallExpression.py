from src.AST.Expression import Expression

class FunctionCallExpression(Expression):
    """Node For FunctionCallExpression in AST"""

    def __init__(self, identifier, returntype):
        Expression.__init__(self, None)
        self.identifier = identifier
        self.parameters = []

        self.basetype = returntype

    def __init__(self, identifier, returntype, parameters):
        Expression.__init__(self, None)
        self.identifier = identifier
        self.parameters = parameters

        self.basetype = returntype

    def __str__(self):
        out = "Call " + str(self.identifier) + "("
        out += str(self.parameters) + ")"
        return out

    def compile(self):
        return "Todo: function call\n"

    def serialize(self, level):
        out = "Call " + str(self.identifier) + "("
        out += str(self.parameters) + ")"

        return out
