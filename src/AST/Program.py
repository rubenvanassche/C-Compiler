from src.AST.Node import Node

class Program(Node):
    """Node For Program in AST"""

    def __init__(self, sym):
        Node.__init__(self)
        self.statements = []
        self.sym = sym

    def __str__(self):
        out = ""
        for statement in self.statements:
            out += str(statement) + "\n"
        return out

    def compile(self):
        if(len(self.statements) == 0):
            return "hlt\n"

        # Add the initial code
        code = "mst 0\n"
        code += "cup 0 init\n"
        code += "init:\n"
        code += "ssp 5\n"
        code += "mst 0\n"
        code += "cup 0 main0\n"
        code += "hlt\n"


        for statement in self.statements:
            code += statement.compile()

        return code

    def addStatement(self, statement):
        self.statements.append(statement)

    def serialize(self, level):
        pass

    def serialize(self, level):
        out = "Program\n:"
        for statement in self.statements:
            out += self.s(1) + statement.serialize(1)
        return out
