from src.Type.PrimitiveType import PrimitiveType
from src.Type.Type import Type

class IntegerType(PrimitiveType):
    """Integer Type"""
    def __init__(self):
        PrimitiveType.__init__(self, 'i')

    def __str__(self):
        out = ""
        if(self.isConst):
            out += "const "
        return out + "int"

    def serialize(self, level):
        return "IntegerType"
