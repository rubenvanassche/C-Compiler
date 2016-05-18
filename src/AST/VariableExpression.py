from src.AST.Expression import Expression

class VariableExpression(Expression):
    """Node For VariableExpression in AST"""

    def __init__(self, basetype, symbol):
        Expression.__init__(self)
        self.basetype = basetype
        self.symbol = symbol
        self.arraySize = None

    def __init__(self, basetype, symbol, arraySize):
        Expression.__init__(self)
        self.basetype = basetype
        self.symbol = symbol
        self.arraySize = arraySize

    def __str__(self):
        out = "define " + str(self.basetype) + ":" + str(self.symbol)
        if(self.arraySize != None):
            out += "[" + str(self.arraySize) + "]"
        out += "\n"
        return out

    def compile(self):
        self.sym.registerSymbol(self.symbol, self.basetype)

    def serialize(self, level):
        out = "define()" + self.basetype.serialize(0) + ":" + str(self.symbol)
        if(self.arraySize != None):
            out += "[" + str(self.arraySize) + "]"
        out += ")\n"
        return out
