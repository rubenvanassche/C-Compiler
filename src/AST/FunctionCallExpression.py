from src.AST.Expression import Expression

class FunctionCallExpression(Expression):
    """Node For FunctionCallExpression in AST"""
    def __init__(self, function, parameters):
        Expression.__init__(self, None)
        self.function = function
        self.parameters = parameters

        self.basetype = function.returntype

    def __str__(self):
        out = "Call " + str(self.function.identifier) + "("
        out += str(self.parameters) + ")"
        return out

    def compile(self):
        code = "mst 0\n"
        code += "cup " + str(self.function.getParameterSize()) + " " + self.function.label + "\n"
        
        return code

    def serialize(self, level):
        out = "Call " + str(self.function.identifier) + "("
        out += str(self.parameters) + ")"

        return out
