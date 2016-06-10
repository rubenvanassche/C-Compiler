from src.Type.PrimitiveType import PrimitiveType

class AddressType(PrimitiveType):
    """Address Type"""

    # Addressee is the type of the addressee
    def __init__(self, addressee):
        PrimitiveType.__init__(self, 'a')
        self.addressee = addressee

    def __eq__(self, other):
        if(not isinstance(other, AddressType)):
            return False
        else:
            if(self.addressee == None):
                return self.addressee == other.addressee
            else:
                return self.addressee == other.addressee

    def getPcode(self):
        return "a"

    def getSize(self):
        return 1

    def __str__(self):
        out = ""
        if(self.isConst):
            out += "const "
        return out + "ptr("+ str(self.addressee) + ")"

    def serialize(self, level):
        return "AddressType"
