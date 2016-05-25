from src.Data.Data import Data

class BooleanData(Data):
    """Represntatation of boolean """
    def __init__(self, boolean):
        super(Data, self).__init__()
        self.boolean = boolean

    def compile(self):
        if(self.boolean == True):
            return "ldc b t\n"
        else:
            return "ldc b f\n"

    def __str__(self):
        return "boolean(" + str(self.boolean) + ")"
