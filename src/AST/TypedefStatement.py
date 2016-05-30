from src.AST.Statement import Statement

class TypedefStatement(Statement):
    """Node For TypedefStatement in AST"""

    def __init__(self, basetype, identifier):
        Statement.__init__(self)
        self.basetype = basetype
        self.identifier = identifier

    def __str__(self):
        return "Typedef " + str(self.basetype) + " -> " + str(self.identifier) + "\n"

    def compile(self):
        return "Todo: TYpedef"

    def serialize(self, level):
        return "Typedef " + self.basetype.serialize(0) + " -> " + str(self.identifier) + "\n"
