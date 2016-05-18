from src.AST.Node import Node

class Statement(Node):
    """Node For Statement in AST"""

    def __init__(self):
        Node.__init__(self)

    def __str__(self):
        return "Statement"

    def compile(self):
        return ""

    def serialize(self, level):
        pass
