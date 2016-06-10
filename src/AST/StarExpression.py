from src.AST.Expression import Expression
from src.utils import *

from src.Type.AddressType import AddressType

class StarExpression(Expression):
    """Node For StarExpression in AST"""

    def __init__(self, expression):
        Expression.__init__(self, None)
        self.expression = expression

        if(not isinstance(expression.basetype, AddressType)):
            raise RuntimeError("Tried to dereference non address type: " + str(type(self.expression.basetype)))

        self.basetype = self.expression.basetype.addressee

    def __str__(self):
        return "Star(" + str(self.expression) + ")"

    def compile(self):
        output = self.expression.compile()
        output += "ind " + self.expression.basetype.addressee.getPcode() + "\n"
        return output

    def serialize(self, level):
        out = padding(level) + "StarExpression\n"
        out += self.expression.serialize(level + 1)

        return out
