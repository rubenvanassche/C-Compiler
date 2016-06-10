from src.AST.Expression import Expression
from src.utils import *

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

        # Load parameters
        for parameter in self.parameters.parameters:
            code += parameter.expression.compile()

        code += "cup " + str(self.function.getParameterSize()) + " " + self.function.label + "\n"

        return code

    def serialize(self, level):
        return padding(level) + "FunctionCallExpression(" + self.function.identifier +")\n"
