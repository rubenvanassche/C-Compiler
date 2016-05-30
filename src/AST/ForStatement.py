from src.AST.Statement import Statement
from src.Type.BooleanType import BooleanType

class ForStatement(Statement):
    """Node For ForStatement in AST"""

    def __init__(self, initExpression, checkExpression, updateExpression, statement):
        Statement.__init__(self)
        self.initExpression = initExpression
        self.checkExpression = checkExpression
        self.updateExpression = updateExpression
        self.statement = statement

    def __str__(self):
        out = "For(" + str(self.initExpression) + ", " + str(self.checkExpression) + ", " + str(self.updateExpression) + ")\n"
        out += "    " + str(self.statement)

        return out

    def compile(self):
        self.sym.openLoop()

        # Get begin and end label
        begin = self.sym.getBeginLoop()
        end = self.sym.getEndLoop()

        # compile the initial expression
        if(self.initExpression != None):
            pcode += self.initExpression.compile()

        # Mark begin of loop
        code = begin + ":\n"

        # Check if check is an boolean Expression
        if(type(self.checkExpression.basetype) != type(BooleanType())):
            raise RuntimeError("Check condition in for loop should be of boolean type")

        # Compile check
        code += "fjp " + end + "\n"

        # Compile the statement
        code += self.statement.compile()

        # compile the update
        code += self.updateExpression.compile()

        # Jump to begin with unconditional Jump
        code += "ujp " + begin + "\n"

        # Mark end of for loop
        code += end + ":\n"

        self.sym.closeLoop()

        return code
    

    def serialize(self, level):
        out = "For(" + self.initExpression.serialize(0) + ", " + self.checkExpression.serialize(0) + ", " + self.updateExpression.serialize(0) + ")\n"
        out += self.s(level) + self.statement(level + 1)

        return out
