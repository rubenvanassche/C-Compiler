from src.AST.Expression import Expression
from src.Type.BooleanType import BooleanType
from src.utils import *

class ComparisonExpression(Expression):
    """Node For ComparisonExpression in AST"""

    def __init__(self, leftExpression, rightExpression, operation):
        Expression.__init__(self, None)
        self.operation = operation
        self.leftExpression = leftExpression
        self.rightExpression = rightExpression

        # Determine the type of the expression
        # check if types of 2 expressions are the same
        if(self.leftExpression.basetype != self.rightExpression.basetype):
            raise RuntimeError("The two types of the expressions in the arithmetic expression should be the same")

        # set the type of this expression
        self.basetype = BooleanType()

    def __str__(self):
        return str(self.leftExpression) + " " + str(self.operation) + " " + str(self.rightExpression)

    def compile(self):
        operations = {'==' : 'equ', '!=' : 'neq', '>' : 'grt', '<' : 'les', '>=' : 'geq', '<=' : 'leq'}
        code = self.leftExpression.compile()
        code += self.rightExpression.compile()
        code += operations[self.operation] + " " + self.leftExpression.basetype.getPcode() + "\n"

        return code

    def serialize(self, level):
        return self.leftExpression.serialize(0) + " " + self.operation + " " + self.rightExpression.serialize(0)
