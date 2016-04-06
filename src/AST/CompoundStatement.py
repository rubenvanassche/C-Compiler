from Statement import Statement

class CompoundStatement(Statement):

    def __init__(self, statements):
        self.statements = statements

    def __str__(self):
        return "CompoundStatement"

    def compile(self):
        return ""
