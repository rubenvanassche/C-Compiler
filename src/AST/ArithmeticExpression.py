from src.AST.Expression import Expression
from src.utils import *

from src.Type.IntegerType import IntegerType
from src.Type.RealType import RealType

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

        if(not isinstance(self.leftExpression.basetype, IntegerType) and not isinstance(self.leftExpression.basetype, RealType)):
            raise RuntimeError("Left side of arithmetic expression should be an integer or real, now: " + str(type(self.leftExpression.basetype)))

        if(not isinstance(self.rightExpression.basetype, IntegerType) and not isinstance(self.rightExpression.basetype, RealType)):
            raise RuntimeError("Right side of arithmetic expression should be an integer or real, now: " + str(type(self.rightExpression.basetype)))


        # set the type of this expression
        self.basetype = self.leftExpression.basetype


    def __str__(self):
        return str(self.leftExpression) + " " + str(self.operation) + " " + str(self.rightExpression)

    def compile(self):
        operations = {'+' : 'add', '-' : 'sub', '/' : 'div', '*' : 'mul'}
        code = self.leftExpression.compile()
        code += self.rightExpression.compile()
        code += operations[self.operation] + " " + self.basetype.getPcode() + "\n"

        return code

    def serialize(self, level):
        return self.leftExpression.serialize(0) + " " + str(self.operation) + " " + self.rightExpression.serialize(0)
