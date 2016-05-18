from src.AST.Statement import Statement

class IfelseStatement(Statement):
    """Node For IfelseStatement in AST"""

    def __init__(self, expression, statement):
        Statement.__init__(self)
        self.expression = expression
        self.statement = statement
        self.alternativeStatement = None

    def __init__(self, expression, statement, alternativeStatement):
        Statement.__init__(self)
        self.expression = expression
        self.statement = statement
        self.alternativeStatement = alternativeStatement

    def __str__(self):
        out =  "If(" + str(self.expression) + ")\n"
        out += "    " + str(self.statement) + "\n"
        if(self.alternativeStatement != None):
            out += "Else\n"
            out += "    " +  str(self.alternativeStatement) + "\n"

        return out

    def compile(self):
        self.sym.openScope()
        self.statement.compile()
        self.sym.closeScope()

        if(self.alternativeStatement != None):

            self.sym.openScope()
            self.alternativeStatement().compile()
            self.sym.closeScope()

    def serialize(self, level):
        out =  "If(" + self.expression.serialize(0) + ")\n:"
        out += statement.serialize(index) + "\n"
        if(self.alternativeStatement != None):
            out += "Else\n:"
            out += alternativeStatement.serialize(index) + "\n"

        return out
