from src.AST.Expression import Expression
from src.Type.BooleanType import BooleanType
from src.utils import *

class LogicExpression(Expression):
    """Node For LogicExpression in AST"""

    def __init__(self, leftExpression, rightExpression, operation):
        Expression.__init__(self, None)
        self.operation = operation
        self.leftExpression = leftExpression
        self.rightExpression = rightExpression

        # Determine the type of the expression
        # check if types of 2 expressions are the same
        if(self.leftExpression.basetype != self.rightExpression.basetype):
            raise RuntimeError("The two types of the expressions in the logic expression should be the same")

        if(not isinstance(self.leftExpression.basetype, BooleanType)):
            raise RuntimeError("Left side of logic expression should be a bool, now: " + str(type(self.leftExpression.basetype)))

        if(not isinstance(self.rightExpression.basetype, BooleanType)):
            raise RuntimeError("Right side of logic expression should be a bool, now: " + str(type(self.rightExpression.basetype)))


        # set the type of this expression
        self.basetype = BooleanType()

    def __str__(self):
        return str(self.leftExpression) + " " + str(self.operation) + " " + str(self.rightExpression)

    def compile(self):
        operations = {'&&' : 'and', '||' : 'or'}
        code = self.leftExpression.compile()
        code += self.rightExpression.compile()
        code += operations[self.operation] + "\n"

        return code

    def serialize(self, level):
        return self.leftExpression.serialize(0) + " " + self.operation + " " + self.rightExpression.serialize(0)
