from src.Type.Type import Type

class ArrayType(Type):
    """Array Type"""

    # basetype: type and size:int
    def __init__(self, basetype, size):
        totalSize = '0' if basetype == None else size * basetype.getSize()
        Type.__init__(self, totalSize)

        self.basetype = basetype
        self.size = size

    def __eq__(self, other):
        if(not isinstance(other, ArrayType)):
            return False
        else:
            if(self.size == -1 or other.size == -1):
                # Clause no len specified
                return (self.basetype == other.basetype)
            else:
                return (self.basetype == other.basetype and self.size == other.size)

    def getPcode(self):
        return self.basetype.getPcode()

    def getElementsType(self):
        return self.basetype

    def getElementsCount(self):
        return self.size

    def serialize(self, level):
        return "ArrayType"

    def getSize(self):
        return self.size*self.basetype.getSize()

    def isArray(self):
        return True
