from Statement import Statement

class IncludeStatement(Statement):

    def __init__(self, path):
        self.path = path

    def __str__(self):
        return "IncludeStatement"

    def compile(self):
        return ""
