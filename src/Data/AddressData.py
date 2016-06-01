from src.Data.Data import Data

class AddressData(Data):
    """Represntatation of address """
    def __init__(self, address):
        super(Data, self).__init__()
        self.address = address

    def compile(self):
        if(self.address < 0):
            raise RuntimeError("Address should be positive")

        return "ldc a " + str(self.address) + "\n"

    def __str__(self):
        return str(self.address)
