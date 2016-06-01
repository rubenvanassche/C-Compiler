from src.AST.Statement import Statement
from src.Type.BooleanType import BooleanType
from src.utils import *

class WhileStatement(Statement):
    """Node For WhileStatement in AST"""

    def __init__(self, expression, statement, sym):
        Statement.__init__(self)
        self.expression = expression
        self.statement = statement
        self.sym = sym

    def __str__(self):
        out = "While(" + str(self.expression) + ")\n"
        out += "    " + str(self.statement) + "\n"

        return out
    def compile(self):
        # Check if expression is an boolean type
        if(type(self.expression.basetype) != type(BooleanType())):
            raise RuntimeError("Expression in while clause should be of an boolean type")

        self.sym.openLoop()

        begin = self.sym.getBeginLoop()
        end = self.sym.getEndLoop()

        # mark the begin of the WHILE statement
        code = str(begin) + ":\n"

        # compile the expression to evaluate
        code += self.expression.compile() + "fjp" + str(end) + "\n"

        # compile the statement to execute
        code += self.statement.compile()

        # end with an unconditional jump to the begin
        code += "ujp " + str(begin) + "\n"

        # mark the end of the WHILE statement
        code += str(end) + ":\n"

        self.sym.closeLoop()
        return code

    def serialize(self, level):
        out = ""
        if(self.expression != None):
            out += padding(level) + "WHILE:\n"
            out += padding(level + 1) + self.expression.serialize(0)
        else:
            out += "WHILE"

        if(self.statement != None):
            out += padding(level) + "THEN:\n"
            out +=  self.statement.serialize(level + 1)


        return out
