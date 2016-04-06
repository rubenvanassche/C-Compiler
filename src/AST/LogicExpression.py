 from Expression import Expression

class LogicExpression(Expression):

    def __init__(self, operation,  leftExpression, rightExpression):
        self.operation = operation
        self.leftExpression = leftExpression
        self.rightExpression = rightExpression

    def __str__(self):
        return "LogicExpression"

    def compile(self):
        return ""
