from src.AST.Expression import Expression

class FunctionCallExpression(Expression):
    """Node For FunctionCallExpression in AST"""

    def __init__(self, identifier):
        Expression.__init__(self, None)
        self.identifier = identifier
        self.parameters = []

        self.basetype = self.sym.getFunction(identifier, []).returntype

    def __init__(self, identifier, parameters):
        Expression.__init__(self, None)
        self.identifier = identifier
        self.parameters = parameters

        self.basetype = self.sym.getFunction(identifier, parameters).returntype

    def __str__(self):
        out = "Call " + str(self.identifier) + "("
        out += str(self.parameters) + ")"
        return out

    def compile(self):
        pass

    def serialize(self, level):
        out = "Call " + str(self.identifier) + "("
        out += str(self.parameters) + ")"

        return out
