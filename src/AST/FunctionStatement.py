from src.AST.Statement import Statement
from src.utils import *


class FunctionStatement(Statement):
    """Node For FunctionStatement in AST"""

    def __init__(self, function, statements, implemented):
        """Create a function with a function(Function), statements([Statement]) and implemented(bool)"""
        Statement.__init__(self)
        self.function = function
        self.statements = statements
        self.implemented = implemented

    def __str__(self):
        imp = ""
        if(self.implemented == True):
            imp = "(i) "

        out = "Function "+ imp +str(self.function.identifier)+"("+str(self.function.arguments)+")-> "+str(self.function.returntype)+" \n"
        for statement in self.statements:
            out += str(statement)

        return out

    def compile(self):
        if(self.implemented == False):
            return ""

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
