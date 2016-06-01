from src.AST.Statement import Statement


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
        code = "TODO- Function statement\n"
        for statement in self.statements:
            code += statement.compile()

        return code

    def serialize(self, level):
        out = "Function " + self.function.identifier + "(" + str(self.function.parameters) + ") -> " + str(self.function.returntype)+" \n"
        out += self.s(level + 1) + self.statements.serialize(level + 1)

        return out
