from src.Type.PrimitiveType import PrimitiveType

class CharacterType(PrimitiveType):
    """Address Type"""

    def __init__(self):
        PrimitiveType.__init__(self, 'c')

    def __str__(self):
        out = ""
        if(self.isConst):
            out += "const "
        return out + "char"

    def serialize(self, level):
        return "CharacterType"
