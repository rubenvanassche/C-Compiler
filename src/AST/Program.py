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
        for statement in self.statements:
            statement.compile()

    def addStatement(self, statement):
        self.statements.append(statement)

    def serialize(self, level):
        pass

    def serialize(self, level):
        out = "Program\n:"
        for statement in self.statements:
            out += self.s(1) + statement.serialize(1)
        return out
