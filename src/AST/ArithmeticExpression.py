from src.AST.Expression import Expression
from src.utils import *

class ArithmeticExpression(Expression):
    """Node For ArithmeticExpression in AST"""

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
        self.basetype = self.leftExpression.basetype


    def __str__(self):
        return str(self.leftExpression) + " " + str(self.operation) + " " + str(self.rightExpression)

    def compile(self):
        operations = {'+' : 'add', '-' : 'sub', '/' : 'div', '*' : 'mul'}
        code = self.leftExpression.compile()
        code += self.rightExpression.compile()
        code += operations[self.operation] + self.basetype.getPcode() + "\n"

        return code

    def serialize(self, level):
        return self.leftExpression.serialize(0) + " " + str(self.operation) + " " + self.rightExpression.serialize(0)
