from src.AST.Expression import Expression
from src.utils import *

# Data
from src.Data.AddressData import AddressData
from src.Data.IntegerData import IntegerData
from src.Data.BooleanData import BooleanData
from src.Data.CharacterData import CharacterData
from src.Data.RealData import RealData
from src.Data.StringData import StringData

# Types
from src.Type.AddressType import AddressType
from src.Type.ArrayType import ArrayType
from src.Type.BooleanType import BooleanType
from src.Type.CharacterType import CharacterType
from src.Type.IntegerType import IntegerType
from src.Type.RealType import RealType

class ConstantExpression(Expression):
    """Node For ConstantExpression in AST"""

    def __init__(self, value, basetype):
        Expression.__init__(self, None)
        if(basetype == "bool"):
            self.basetype = BooleanType()
            self.value = BooleanData(value)
        elif(basetype == "char"):
            self.basetype = CharacterType()
            self.value = CharacterData(value)
        elif(basetype == "int"):
            self.basetype = IntegerType()
            self.value = IntegerData(value)
        elif(basetype == "float"):
            self.basetype = RealType()
            self.value = RealData(value)
        elif(basetype == "string"):
            self.basetype = ArrayType(CharacterType(), len(value))
            self.value = StringData(value)
        else:
            raise RuntimeError("Trying to create constantexpession with unkown type")

    def __str__(self):
        out = padding(level) + "ConstantExpression\n"
        out += self.basetype.serialize(level + 1)

        return out

    def compile(self):
        return self.value.compile()

    def serialize(self, level):
        return self.basetype.getPcode() + ": " + str(self.value)
