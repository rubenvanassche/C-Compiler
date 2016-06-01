from src.AST.Statement import Statement
from src.utils import *


class FunctionStatement(Statement):
    """Node For FunctionStatement in AST"""

    def __init__(self, function, statements):
        """Create a function with a function(Function) and statements([Statement])"""
        Statement.__init__(self)
        self.function = function
        self.statements = statements

    def __str__(self):
        out = "Function "+str(self.function.identifier)+"("+str(self.function.arguments)+")-> "+str(self.function.returntype)+" \n"
        for statement in self.statements:
            out += str(statement)

        return out

    def compile(self):
        code = self.function.label + ":\n"
        code += "ssp " + str(self.function.getStaticSize()) + "\n"
        for statement in self.statements:
            code += statement.compile()

        code += "retp\n"

        return code

    def serialize(self, level):
        out =  padding(level) + "FunctionStatement("+ self.function.identifier +")\n"
        for statement in self.statements:
            out += padding(level + 1) + statement.serialize(level + 1)

        return out
