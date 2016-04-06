from Statement import Statement

class IfelseStatement(Statement):
    def __init__(self, expression, statement):
        self.expression = expression
        self.statement = statement
        self.alternativeStatement = None

    def __init__(self, expression, statement, alternativeStatement):
        self.expression = expression
        self.statement = statement
        self.alternativeStatement = alternativeStatement

    def __str__(self):
        return "IfelseStatement"

    def compile(self):
        return ""
