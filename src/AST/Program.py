from src.AST.Node import Node

class Program(Node):
    """Node For Program in AST"""

    def __init__(self):
        Node.__init__(self)
        self.statements = []

    def __str__(self):
        out = ""
        for statement in self.statements:
            out += str(statement) + "\n"
        return out

    def compile(self):
        if(len(self.statements) == 0):
            return "hlt\n"

        code = ""
        for statement in self.statements:
            code += statement.compile()

        return "ssp " +  self.sym.getAllocated() + "\n" + code + "hlt\n"

    def addStatement(self, statement):
        self.statements.append(statement)

    def serialize(self, level):
        pass

    def serialize(self, level):
        out = "Program\n:"
        for statement in self.statements:
            out += self.s(1) + statement.serialize(1)
        return out
