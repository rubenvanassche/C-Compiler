from src.AST.Expression import Expression

class FunctionCallExpression(Expression):
    """Node For FunctionCallExpression in AST"""

    def __init__(self, identifier):
        Expression.__init__(self)
        self.identifier = identifier
        self.parameters = []

    def __init__(self, identifier, parameters):
        Expression.__init__(self)
        self.identifier = identifier
        self.parameters = parameters

    def __str__(self):
        out = "Call " + str(self.identifier) + "("
        out += str(self.parameters) + ")"
        return out

    def compile(self):
        self.sym.getFunction(self.identifier, self.parameters)

    def serialize(self, level):
        out = "Call " + str(self.identifier) + "("
        out += str(self.parameters) + ")"

        return out
