from Expression import Expression

class ComparisonExpression(Expression):

    def __init__(self, operation, leftExpression, rightExpression):
        self.operation = operation
        self.leftExpression = leftExpression
        self.rightExpression = rightExpression

    def __str__(self):
        return "ComparisonExpression"

    def compile(self):
        return ""
