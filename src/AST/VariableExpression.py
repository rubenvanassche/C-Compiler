from src.AST.Expression import Expression
from src.Type.ArrayType import ArrayType

class VariableExpression(Expression):
    """Node For VariableExpression in AST"""

    def __init__(self, symbol):
        """Create variable call with symbol(Symbol)"""
        Expression.__init__(self, None)
        self.basetype = symbol.basetype
        self.symbol = symbol
        self.arraySize = None

        if(type(self.symbol) == type(ArrayType)):
            self.arraySize = self.symbol.basetype.getElementsCount()

    def __str__(self):
        out = "define " + str(self.basetype) + ":" + str(self.symbol.identifier)
        if(self.arraySize != None):
            out += "[" + str(self.arraySize) + "]"
        out += "\n"
        return out

    def compile(self):
        return "Todo: Variable expression\n"

    def serialize(self, level):
        out = "define()" + self.basetype.serialize(0) + ":" + str(self.symbol.identifier)
        if(self.arraySize != None):
            out += "[" + str(self.arraySize) + "]"
        out += ")\n"
        return out
