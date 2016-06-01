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

class Symbol:
    """Representation of a Symbol"""
    def __init__(self, identifier, basetype, address):
        """Initialize with an identifier(string), basetype(Type) and array(bool)"""
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
    def __init__(self, identifier, returntype, arguments, staticsize, label):
        """Initialize with an identifier(string), returnType(Type), argument(argumentList), staticsize(int) and label(string)"""
        self.identifier = identifier
        self.returntype = returntype
        self.arguments = arguments
        self.staticsize = staticsize
        self.label = label

    def getStaticSize(self):
        """Get the static size required for the SSP command"""
        size = 5

        return size

    def getParameterSize(self):
        """Get the parameter size required for the cup command"""
        size = 0

        for argument in self.arguments.arguments:
            size += argument.basetype.getSize()

        return size
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
        self.table = None
        self.scope = None
        self.loops = []
        self.labels = 0
        self.functionLabels = {}

        # Open the global scope
        self.table = Scope(None)
        self.scope = self.table

    def openScope(self):
        """Open a scope"""
        self.scope = self.scope.openScope()

    def closeScope(self):
        """Close Scope"""
        if(self.scope.parentScope == None):
            raise ScopeError("No scope opened previously")

        self.scope = self.scope.parentScope

    def registerSymbol(self, identifier, basetype):
        """Register a Symbol in the current scope with an identifier(string) and basetype(Type) is an array(bool)"""
        if(self.scope.isContainingSymbol(identifier)):
            raise SymbolAlreadyRegisteredError("Symbol '"+ identifier +"' already registered in scope")

        if(basetype.getSize() == 0):
            raise TypeError("Type should have a size greater then 0")

        symbol = Symbol(identifier, basetype, self.scope.getAllocated())
        self.scope.addSymbol(symbol)

        # raise the allocated count
        self.scope.allocated += basetype.getSize()

        return symbol

    def registerAlias(self, identifier, basetype):
        """Register an Alias in the current scope with an identifier(string) and basetype(Type)"""
        if(self.scope.isContainingAlias(identifier)):
            raise AliasAlreadyRegisteredError("Alias '"+ identifier +"' already registered in scope")

        alias = Alias(identifier, basetype)
        self.scope.addAlias(alias)

        return alias

    def registerFunction(self, identifier, returntype, arguments, staticsize):
        """Register a Function in the current scope with an identifier(string), returntype(Type), arguments(ArgumentsList) and staticsize(int)"""
        if(self.scope.isContainingFunction(identifier, arguments)):
            raise FunctionAlreadyRegisteredError("Function '"+ identifier +"' already registered in scope")

        #get a label
        label = self.createFunctionLabel(identifier)

        function = Function(identifier, returntype, arguments, staticsize, label)

        self.scope.addFunction(function)

        return function

    def registerArguments(self, arguments):
        """Register the symbols in an arguments(ArgumentsList)"""
        for argument in arguments.arguments:
            self.registerSymbol(argument.identifier, argument.basetype)

    def getSymbol(self, identifier):
        """Get a symbol from the Symbol Table with an identifier(string)"""
        searchScope = self.scope

        while(True):
            symbol = searchScope.getSymbol(identifier)

            if(symbol != None):
                return symbol
            else:
                searchScope = searchScope.parentScope
                if(searchScope == None):
                    # Stop in main scope
                    break

        raise SymbolNotRegisteredError("Symbol '"+ identifier +"' not registered")

    def getAlias(self, identifier):
        """Get an alias from the Symbol Table with an identifier(string)"""
        searchScope = self.scope

        while(True):
            alias = searchScope.getAlias(identifier)

            if(alias != None):
                return alias
            else:
                searchScope = searchScope.parentScope
                if(searchScope == None):
                    # Stop in main scope
                    break

        raise AliasNotRegisteredError("Alias '"+ identifier +"' not registered")

    # Parameters is [] and not ParametersList
    def getFunction(self, identifier, parameters):
        """Get a function from the Symbol Table with an identifier(string) and parameters(ParametersList)"""
        searchScope = self.scope

        while(True):
            function = searchScope.getFunction(identifier, parameters)

            if(function != None):
                return function
            else:
                searchScope = searchScope.parentScope
                if(searchScope == None):
                    # Stop in main scope
                    break

        raise FunctionNotRegisteredError("Function '"+ identifier +"' not registered")

    def openLoop(self):
        """Open a loop"""
        loop = Loop(self.labels + 1, self.labels + 2)
        self.labels += 2

        self.loops.append(loop)

    def closeLoop(self):
        """Close a loop"""
        if(len(self.loops) == 0):
            raise ScopeError("No loops opened")

        self.loops.pop()

    def getBeginLoop(self):
        """Get the start label of the loop"""
        return "bl" + str(self.loops[-1].begin)

    def getEndLoop(self):
        """Get the end label of the loop"""
        return "el" + str(self.loops[-1].end)

    def createLabel(self):
        """Create a label"""
        self.labels += 1
        return "l" + str(self.labels)

    def createFunctionLabel(self, name):
        """Create a label for a function with given name"""
        if name in self.functionLabels:
            self.functionLabels[name] += 1
        else:
            self.functionLabels[name] = 0

        return name + str(self.functionLabels[name])

    def getAllocatedSpace(self):
        """Get the size of the address space in use"""
        return self.scope.allocated

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
