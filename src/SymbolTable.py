from src.Type.IntegerType import IntegerType
from src.Exceptions.SymbolTable import *

class Scope:
    """An Scope in the program"""
    def __init__(self, allocated):
        """Initializer with allocated(int) which represents from where in the memory the scope can start allocating"""

        self.allocated = allocated
        self.symbols = []
        self.aliases = []
        self.functions = []

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
        """Returns from where this scope can start allocating"""
        return self.allocated

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

class Symbol:
    """Representation of a Symbol"""
    def __init__(self, identifier, basetype, address):
        """Initialize with an identifier(string), basetype(Type) and adress(int)"""
        self.identifier = identifier
        self.basetype = basetype
        self.address = address

class Alias:
    """Representation of an Alias"""
    def __init__(self, identifier, basetype):
        """Initialize with an identifier(string) and basetype(Type)"""
        self.identifier = identifier
        self.basetype = basetype

class Function:
    """Representation of a Function"""
    def __init__(self, identifier, returntype, arguments, address):
        """Initialize with an identifier(string), returnType(Type), argument(argumentList) and adress(int)"""
        self.identifier = identifier
        self.returntype = returntype
        self.arguments = arguments
        self.address = address

class Loop:
    """Representation of a Loop"""
    def __init__(self, begin, end):
        """initialize with begin(int) address and end(int) address of loop"""
        self.begin = begin
        self.end = end


class SymbolTable:
    """Representation of a Symbol Table"""

    def __init__(self):
        """Initializer, will also open the global scope"""
        self.scopes = []
        self.aliases = []
        self.loops = []
        self.labels = 0

        # Open the global scope
        self.scopes.append(Scope(0))

    def openScope(self):
        """Open a scope"""
        newScope = Scope(self.scopes[-1].getAllocated())
        self.scopes.append(newScope)

    def closeScope(self):
        """Close Scope"""
        if(len(self.scopes) == 1):
            raise ScopeError("No scope opened previously")

        self.scopes.pop()

    def registerSymbol(self, identifier, basetype):
        """Register a Symbol in the current scope with an identifier(string) and basetype(Type)"""
        if(self.scopes[-1].isContainingSymbol(identifier)):
            raise SymbolAlreadyRegisteredError("Symbol '"+ identifier +"' already registered in scope")

        if(basetype.getSize() == 0):
            raise TypeError("Type should have a size greater then 0")

        symbol = Symbol(identifier, basetype, self.scopes[-1].getAllocated())
        self.scopes[-1].addSymbol(symbol)

        # raise the allocated count
        self.scopes[-1].allocated += basetype.getSize()

    def registerAlias(self, identifier, basetype):
        """Register an Alias in the current scope with an identifier(string) and basetype(Type)"""
        if(self.scopes[-1].isContainingAlias(identifier)):
            raise AliasAlreadyRegisteredError("Alias '"+ identifier +"' already registered in scope")

        self.scopes[-1].addAlias(Alias(identifier, basetype))

    def registerFunction(self, identifier, returntype, arguments, address):
        """Register a Function in the current scope with an identifier(string), returntype(Type), arguments(ArgumentsList) and address(int)"""
        if(self.scopes[-1].isContainingFunction(identifier, arguments)):
            raise FunctionAlreadyRegisteredError("Function '"+ identifier +"' already registered in scope")

        self.scopes[-1].addFunction(Function(identifier, returntype, arguments, address))

    def registerArguments(self, arguments):
        """Register the symbols in an arguments(ArgumentsList)"""
        for argument in arguments.arguments:
            self.registerSymbol(argument.identifier, argument.basetype)

    def getSymbol(self, identifier):
        """Get a symbol from the Symbol Table with an identifier(string)"""
        for scope in reversed(self.scopes):
            symbol = scope.getSymbol(identifier)

            if(symbol != None):
                return symbol

        raise SymbolNotRegisteredError("Symbol '"+ identifier +"' not registered")

    def getAlias(self, identifier):
        """Get an alias from the Symbol Table with an identifier(string)"""
        for scope in reversed(self.scopes):
            alias = scope.getAlias(identifier)

            if(alias != None):
                return alias

        raise AliasNotRegisteredError("Alias '"+ identifier +"' not registered")

    # Parameters is [] and not ParametersList
    def getFunction(self, identifier, parameters):
        """Get a function from the Symbol Table with an identifier(string) and parameters(ParametersList)"""
        for scope in reversed(self.scopes):
            function = scope.getFunction(identifier, parameters)

            if(function != None):
                return function

        raise FunctionNotRegisteredError("Function '"+ identifier +"' not registered")

    def openLoop(self):
        """Open a loop"""
        loop = Loop(self.labels + 1, self.labels + 2)
        self.labels += 2

        self.loops.append(loop)
        self.openScope()

    def closeLoop(self):
        """Close a loop"""
        if(len(self.loops) == 0):
            raise ScopeError("No loops opened")

        self.loops.pop()
        self.closeScope()

    def getBeginLoop(self):
        """Get the start label of the loop"""
        return self.loops[-1].begin

    def getEndLoop(self):
        """Get the end label of the loop"""
        return self.loops[-1].end

    def createLabel(self):
        """Create a label"""
        self.labels += 1
        return int(self.labels)


    def getAllocatedSpace(self):
        """Get the size of the address space in use"""
        return self.scopes[-1].allocated

    def __str__(self):
        """String Representation"""
        out = "Symbol Table\n"
        out += "------------\n\n"

        counter = 0
        for scope in self.scopes:
            out += "scope(" + str(counter) + ") - allocated: " + str(scope.getAllocated()) +"\n"
            out += "    Symbols: "
            for symbol in scope.symbols:
                out += symbol.identifier + ","
            out += "\n"
            out += "    Aliases: "
            for alias in scope.aliases:
                out += alias.identifier + ","
            out += "\n"
            out += "    Functions: "
            for function in scope.functions:
                out += function.identifier + ","
            out += "\n"

            counter += 1

        return out
