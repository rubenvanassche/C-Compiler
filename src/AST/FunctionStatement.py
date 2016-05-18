from src.AST.Statement import Statement


class FunctionStatement(Statement):
    """Node For FunctionStatement in AST"""

    def __init__(self, returntype, identifier, parameters, statements):
        Statement.__init__(self)
        self.returntype = returntype
        self.identifier = identifier
        self.parameters = parameters
        self.statements = statements

    def __str__(self):
        out = "Function "+str(self.identifier)+"("+str(self.parameters)+")-> "+str(self.returntype)+" \n"
        for statement in self.statements:
            out += str(statement)

        return out

    def compile(self):
        self.sym.registerFunction(self.identifier, self.returntype, self.parameters, 0)

        self.sym.openScope()

        # Register parameters in symbol table
        self.sym.registerParameters(self.parameters)

        for statement in self.statements:
            statement.compile()
        self.sym.closeScope()

    def serialize(self, level):
        out = "Function " + self.identifier + "(" + str(self.parameters) + ") -> " + str(self.returntype)+" \n"
        out += self.s(level + 1) + self.statements.serialize(level + 1)

        return out
