from src.AST.Expression import Expression
from src.AST.VariableCallExpression import VariableCallExpression
from src.Type.AddressType import AddressType
from src.utils import *

class AmpersandExpression(Expression):
    """Node For AmpersandExpression in AST"""
    def __init__(self, expression):
        Expression.__init__(self, None)
        self.expression = expression
        self.basetype = AddressType(self.expression.basetype)

        if(not isinstance(self.expression, VariableCallExpression)):
            raise RuntimeError("Can only get the address of an variable")


    def __str__(self):
        return "Ampersand(" + str(self.expression) + ")"

    def serialize(self, level):
        out = padding(level) + "Ampersand\n"
        out += self.expression.serialize(level + 1)

        return out

    def compile(self):
        # So let's find out the address
        address = self.expression.symbol.address

        return "lda 0 " + str(address) +"\n"
