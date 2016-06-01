from src.Data.Data import Data

class RealData(Data):
    """Represntatation of real number """
    def __init__(self, real):
        super(Data, self).__init__()
        self.real = real

    def compile(self):
        return "ldc r " + str(self.real) + "\n"

    def __str__(self):
        return  str(self.real) 
