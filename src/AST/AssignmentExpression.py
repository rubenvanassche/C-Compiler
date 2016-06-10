from src.AST.Expression import Expression
from src.Type.ArrayType import ArrayType
from src.utils import *

from src.AST.VariableExpression import VariableExpression
from src.AST.VariableCallExpression import VariableCallExpression


class AssignmentExpression(Expression):
    """Node For AssignmentExpression in AST"""

    def __init__(self, variable, expression):
        Expression.__init__(self, None)
        self.variable = variable
        self.expression = expression

        self.basetype = self.expression.basetype

    def __str__(self):
        return str(self.variable) + " = " + str(self.expression) + "\n"

    def compile(self):
        # Check if types are the same
        if(self.expression.basetype != self.variable.basetype):
            # Check if it is an ArrayType
            if(self.expression.basetype.isArray() and self.variable.basetype.isArray()):
                # int a[3] = b[3]
                if(self.expression.basetype.basetype != self.variable.basetype.basetype):
                    raise RuntimeError("Tried to assign two different types")
            elif(self.expression.basetype.isArray() or self.variable.basetype.isArray()):
                if(self.expression.basetype.isArray()):
                    # int a = c[3]
                    if(self.expression.basetype.basetype != self.variable.basetype):
                        raise RuntimeError("Tried to assign two different types")
                elif(self.variable.basetype.isArray()):
                    # int c[3] = a
                    if(self.expression.basetype != self.variable.basetype.basetype):
                        raise RuntimeError("Tried to assign two different types")
                else:
                    raise RuntimeError("Unknown fault #1")
            else:
                raise RuntimeError("Tried to assign two different types")

        code = self.expression.compile()
        if(type(self.variable) is VariableExpression):
            code += "str " + str(self.variable.symbol.basetype.getPcode()) + " 0 " + str(self.variable.symbol.address) + "\n"
        elif(type(self.variable) is VariableCallExpression):
            if(self.variable.index == None):
                code += "str " + str(self.variable.symbol.basetype.getPcode()) + " 0 " + str(self.variable.symbol.address) + "\n"
            else:
                print("tets")
                address = self.variable.symbol.address + self.variable.index * self.variable.symbol.basetype.basetype.getSize()
                code += "str " + str(self.variable.symbol.basetype.getPcode()) + " 0 " + str(address) + "\n"
        else:
            raise RuntimeError("Assignment can only be done with variablecall or variable")

        return code

    def serialize(self, level):
        return "Assign " + self.expression.serialize(0) + " -> " + self.variable.serialize(0)
