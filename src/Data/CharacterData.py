from src.Data.Data import Data

class CharacterData(Data):
    """Represntatation of character """
    def __init__(self, character):
        super(Data, self).__init__()
        self.character = character

    def compile(self):
        return "ldc c " + str(self.character) + "\n"

    def __str__(self):
        return "character(" + str(self.character) + ")"
