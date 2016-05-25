from src.Data.Data import Data

class IntegerData(Data):
    """Represntatation of integer """
    def __init__(self, integer):
        super(Data, self).__init__()
        self.integer = integer

    def compile(self):
        return "ldc i " + str(self.integer) + "\n"

    def __str__(self):
        return "integer(" + str(self.integer) + ")"
