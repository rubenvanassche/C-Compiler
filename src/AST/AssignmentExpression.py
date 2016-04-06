from Expression import Expression

class AssignmentExpression(Expression):

    def __init__(self, variable, expression):
        self.variable = variable
        self.expression = expression

    def __str__(self):
        return "AssignmentExpression"

    def compile(self):
        return ""
