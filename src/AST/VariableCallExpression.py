from src.AST.Expression import Expression
from src.utils import *

class VariableCallExpression(Expression):
    """Node For VariableCallExpression in AST"""

    def __init__(self, symbol):
        """Call variable call with symbol(Symbol)"""
        Expression.__init__(self, None)
        self.symbol = symbol
        self.index = None
        self.basetype = symbol.basetype

    def __init__(self, symbol, index):
        """Call variable call with symbol(Symbol) and index(int)"""
        Expression.__init__(self, None)
        self.symbol = symbol
        self.index = index
        self.basetype = symbol.basetype

        if(index != None):
            #Call to element in array so change the basetype to the array's basetype
            self.basetype = symbol.basetype.basetype

    def __str__(self):
        out = "Call " + str(self.symbol.identifier)
        if(self.index != None):
            out += "[" + str(self.index) + "]"
        out += "\n"
        return out

    def compile(self):
        if(self.index == None):
            return "lod " + str(self.symbol.basetype.getPcode()) + " 0 " + str(self.symbol.address) + "\n"
        else:
            # Array
            code = "lda 0 " + str(self.symbol.address) + "\n"
            code += "conv a i\n"
            code += self.index.compile()
            code += "add i\n"
            code += "conv i a\n"
            code += "ind " + self.basetype.getPcode() + "\n"

        return code

    def serialize(self, level):
        if(self.index == None):
            return padding(level) + "VariableExpression(" + self.symbol.identifier + ")\n"
        else:
            return padding(level) + "VariableExpression(" + self.symbol.identifier + ", " + str(self.index) + ")\n"
