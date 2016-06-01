class Type:
    """Representation of Type Node in AST"""
    def __init__(self):
        """Initialize, size = 1"""
        self.const = False
        self.size = 1

    def __init__(self, size):
        """Initializer with size(int)"""
        self.const = False
        self.size = size

    def getSize(self):
        """Returns the size of the type"""
        return self.size

    def isConst(self):
        """Check if type is constant"""
        return self.const

    def setConst(self, const):
        """Set the constness of the type(bool)"""
        self.const = const
        return self

    def serialize(self, level):
        """serialize Type"""
        return "BaseType"

    def isArray(self):
        """Returns true if type is an array"""
        return False

    def __str__(self):
        """String representation"""
        return "BaseType"
