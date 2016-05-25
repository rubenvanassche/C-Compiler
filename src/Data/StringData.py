from src.Data.Data import Data

class StringData(Data):
    """Represntatation of string """
    def __init__(self, string):
        super(Data, self).__init__()
        self.string = string

    def compile(self):
        return "TODO: String data"

    def __str__(self):
        return "string(" + str(self.string) + ")"
