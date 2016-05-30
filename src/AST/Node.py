from src.SymbolTable import SymbolTable

class Node:
    """Node in AST"""

    def __init__(self):
        """Constructor for AST Node """

    def __str__(self):
        """String representation of AST Node"""
        return "Node"

    def compile(self):
        """Compile node to p-code"""
        return ""

    # generate padding
    def s(self, level):
        """Generate padding for serialize function"""
        out = ""
        for i in range(level):
            out += "    "
        return out

    def serialize(self, level):
        """Serialize this node, the level attribute specifies how much indentation is needed"""
        pass
