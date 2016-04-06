from Statement import Statement

class WhileStatement(Statement):

    def __init__(self, expression, statement):
        self.expression = expression
        self.statement = statement

    def __str__(self):
        return "WhileStatement"

    def compile(self):
        return ""
