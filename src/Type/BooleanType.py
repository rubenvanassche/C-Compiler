from src.Type.PrimitiveType import PrimitiveType

class BooleanType(PrimitiveType):
    """Boolean Type"""

    def __init__(self):
        PrimitiveType.__init__(self, 'b')

    def __str__(self):
        out = ""
        if(self.isConst):
            out += "const "
        return out + "bool"

    def getPcode(self):
        return "b"

    def serialize(self, level):
        return "BooleanType"
