from src.AST.Expression import Expression
from src.Type.ArrayType import ArrayType
from src.Type.AddressType import AddressType
from src.Type.CharacterType import CharacterType
from src.Type.IntegerType import IntegerType
from src.Type.RealType import RealType
from src.Type.BooleanType import BooleanType
from src.utils import *

class VariableExpression(Expression):
    """Node For VariableExpression in AST"""

    def __init__(self, symbol):
        """Create variable call with symbol(Symbol)"""
        Expression.__init__(self, None)
        self.basetype = symbol.basetype
        self.symbol = symbol
        self.arraySize = None

        if(isinstance(self.symbol.basetype, ArrayType)):
            self.arraySize = self.symbol.basetype.getElementsCount()

    def __str__(self):
        out = "define " + str(self.basetype) + ":" + str(self.symbol.identifier)
        if(self.arraySize != None):
            out += "[" + str(self.arraySize) + "]"
        out += "\n"
        return out

    def compile(self):
        #code = "lod " + str(self.symbol.basetype.getPcode()) + " 0 " + str(self.symbol.address) + "\n"
        # Initialize
        if(self.arraySize != None):
            #address = self.variable.symbol.address + self.variable.index * self.variable.symbol.basetype.basetype.getSize()
            constant = None
            code = ""

            if(isinstance(self.basetype.basetype, IntegerType)):
                constant = "0"
            elif(isinstance(self.basetype.basetype, RealType)):
                constant = "0.0"
            elif(isinstance(self.basetype.basetype, AddressType)):
                constant = "0"
            elif(isinstance(self.basetype.basetype, CharacterType)):
                constant = "'a'"
            elif(isinstance(self.basetype.basetype, BooleanType)):
                constant = "f"
            else:
                constant = "0.0"

            for i in range(self.arraySize):
                code += "ldc " + self.basetype.basetype.getPcode() + " " + constant + "\n"
                address = self.symbol.address + i * self.symbol.basetype.basetype.getSize()
                code += "str " + str(self.symbol.basetype.getPcode()) + " 0 " + str(address) + "\n"

            return code

        return ""

    def serialize(self, level):
        out = padding(level) + "VariableExpression(" + self.symbol.identifier +")\n"

        return out
