from Statement import Statement

class FunctionStatement(Statement):

    def __init__(self, returnType, identifier, arguments, statement):
        self.returnType = returnType
        self.identifier = identifier
        self.arguments = arguments
        self.statement = statement

    def __str__(self):
        return "FunctionStatement"

    def compile(self):
        return ""
