from src.Type.PrimitiveType import PrimitiveType

class RealType(PrimitiveType):
    """Real Type"""

    def __init__(self):
        PrimitiveType.__init__(self, 'r')

    def __str__(self):
        out = ""
        if(self.isConst):
            out += "const "
        return out + "real"

    def getPcode(self):
        return "r"

    def serialize(self, level):
        return "RealType"
