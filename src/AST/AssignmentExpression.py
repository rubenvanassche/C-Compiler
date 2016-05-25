from src.AST.Expression import Expression

class AssignmentExpression(Expression):
    """Node For AssignmentExpression in AST"""

    def __init__(self, variable, expression):
        Expression.__init__(self, None)
        self.variable = variable
        self.expression = expression

    def __str__(self):
        return str(self.variable) + " = " + str(self.expression) + "\n"

    def compile(self):
        return self.variable.compile()

    def serialize(self, level):
        return "Assign " + self.expression.serialize(0) + " -> " + self.variable.serialize(0)
