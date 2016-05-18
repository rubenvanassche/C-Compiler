from src.Type.Type import Type

class ArrayType(Type):
    """Array Type"""

    # basetype: type and size:int
    def __init__(self, basetype, size):
        totalSize = '0' if basetype == None else size*basetype.getSize()
        super(Type, self).__init__(totalSize)

        self.basetype = basetype
        self.size = size

    def __eq__(self, other):
        if(not isinstance(other, ArrayType)):
            return false
        else:
            return (self.basetype == other.basetype and self.size == other.size)

    def getElementsType(self):
        return self.basetype

    def getElementsCount(self):
        return self.size

    def serialize(self, level):
        return "ArrayType"
