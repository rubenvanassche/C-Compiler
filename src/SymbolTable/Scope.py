from src.Type.IntegerType import IntegerType
from src.Exceptions.SymbolTable import *
from src.utils import *

class Scope:
    """An Scope in the program"""
    def __init__(self, parentScope):
        """Initializer with allocated(int) which represents from where in the memory the scope can start allocating"""
        self.parentScope = parentScope
        self.allocated = 0
        self.symbols = []
        self.aliases = []
        self.functions = []
        self.scopes = []

    def openScope(self):
        newScope = Scope(self)
        self.scopes.append(newScope)

        return self.scopes[-1]

    def addSymbol(self, symbol):
        """Add a Symbol to the Scope"""
        self.symbols.append(symbol)

    def addAlias(self, alias):
        """Add an Alias to the Scope"""
        self.aliases.append(alias)

    def addFunction(self, function):
        """Add a Function to the Scope"""
        self.functions.append(function)

    def getAllocated(self):
        """Returns how many memory was allocated in this scope"""
        return self.allocated

    def getTotalAllocated(self):
        """Return how many memory was allocated in this scope and it's childs scopes"""
        output = self.allocated

        for scope in self.scopes:
            output += scope.getTotalAllocated()

        return output

    def isContainingSymbol(self, identifier):
        """Returns true if the scope has the symbol"""
        return False if self.getSymbol(identifier) == None else True

    def isContainingAlias(self, identifier):
        """Returns true if the scope has the alias"""
        return False if self.getAlias(identifier) == None else True

    def isContainingFunction(self, identifier, arguments):
        """Returns true if the scope has the function"""
        for function in self.functions:
            if function.identifier == identifier and arguments == function.arguments:
                return True

        return False

    def getSymbol(self, identifier):
        """Get the symbol in the scope"""
        for symbol in self.symbols:
            if symbol.identifier == identifier:
                return symbol

        return None

    def getAlias(self, identifier):
        """Get the alias in the scope"""
        for alias in self.aliases:
            if alias.identifier == identifier:
                return alias

        return None

    # parameters is Parameterslist
    def getFunction(self, identifier, parameters):
        """Get the function in the scope"""
        for function in self.functions:
            if function.identifier == identifier and function.arguments.checkCallParameters(parameters):
                return function

        return None

    def printer(self, level):
        output = padding(level) + "||SCOPE(" + str(self.allocated) + ")\n"

        # Symbols
        for symbol in self.symbols:
            output += padding(level) + "-> Symbol(" + symbol.identifier + ") : " + str(symbol.basetype) + "\n"

        # Aliases
        for alias in self.aliases:
            output += padding(level) + "-> Alias(" + alias.identifier + ") : " + str(alias.basetype) + "\n"

        # functions
        for function in self.functions:
            output += padding(level) + "-> Function: " + function.identifier + "(" + str(function.arguments) + ") :  " + str(function.returntype) + "\n"

        for scope in self.scopes:
            output += scope.printer(level + 1)

        return output
