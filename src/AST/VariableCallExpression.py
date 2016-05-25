from src.AST.Expression import Expression

class VariableCallExpression(Expression):
    """Node For VariableCallExpression in AST"""

    def __init__(self, symbol):
        Expression.__init__(self, None)
        self.symbol = symbol
        self.index = None

        self.basetype = self.sym.getSymbol(symbol).basetype

    def __init__(self, symbol, index):
        Expression.__init__(self, None)
        self.symbol = symbol
        self.index = index

        self.basetype = self.sym.getSymbol(symbol).basetype

    def __str__(self):
        out = "Call " + str(self.symbol)
        if(self.index != None):
            out += "[" + str(self.index) + "]"
        out += "\n"
        return out

    def compile(self):
        pass

    def serialize(self, level):
        out = str(self.symbol)
        if(self.index != None):
            out += "[" + str(self.index) + "]"
        return out
