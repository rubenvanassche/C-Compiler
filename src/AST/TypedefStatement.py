from Statement import Statement

class TypedefStatement(Statement):

    def __init__(self, basetype, alias):
        self.basetype = basetype
        self.alias = alias

    def __str__(self):
        return "TypedefStatement"

    def compile(self):
        return ""
