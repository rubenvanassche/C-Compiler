from src.Type.Type import Type

class PrimitiveType(Type):
    """Primitive Type Base Class(integer, boolean, real, address, character)"""
    def __init__(self, code):
        """Initialize with p code of the type(string)"""
        Type.__init__(self, 1)
        self.code = code

    def __eq__(self, other):
        """Check if 2 types are the same"""
        if(not isinstance(other, PrimitiveType)):
            return False
        else:
            return self.code == other.code

    def __str__(self):
        """String representation"""
        return "PrimitiveType"

    def serialize(self, level):
        """Serialize Type"""
        return "PrimitiveType"
