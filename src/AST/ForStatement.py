from Statement import Statement

class ForStatement(Statement):

    def __init__(self, initExpression, checkExpression, updateExpression, statement):
        self.initExpression = initExpression
        self.checkExpression = checkExpression
        self.updateExpression = updateExpression
        self.statement = statement

    def __str__(self):
        return "ForStatement"

    def compile(self):
        return ""
