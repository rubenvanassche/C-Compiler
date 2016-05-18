from src.AST.Expression import Expression

class LogicExpression(Expression):
    """Node For LogicExpression in AST"""

    def __init__(self, operation, leftExpression, rightExpression):
        Expression.__init__(self)
        self.operation = operation
        self.leftExpression = leftExpression
        self.rightExpression = rightExpression

    def __str__(self):
        return str(self.leftExpression) + " " + str(self.operation) + " " + str(self.rightExpression)

    def compile(self):
        return ""

    def serialize(self, level):
        return self.leftExpression.serialize(0) + " " + self.operation + " " + self.rightExpression.serialize(0)
