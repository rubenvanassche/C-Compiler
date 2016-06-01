from src.Type.IntegerType import IntegerType
from src.Exceptions.SymbolTable import *
from src.utils import *

from src.SymbolTable.Alias import Alias
from src.SymbolTable.Function import Function
from src.SymbolTable.Loop import Loop
from src.SymbolTable.Scope import Scope
from src.SymbolTable.Symbol import Symbol

class SymbolTable:
    """Representation of a Symbol Table"""

    def __init__(self):
        """Initializer, will also open the global scope"""
        self.table = None
        self.scope = None
        self.loops = []
        self.labels = 0
        self.functionLabels = {}

        # For function scope
        self.functionAddress = 0
        self.functionScope = False

        # Open the global scope
        self.table = Scope(None)
        self.scope = self.table

    def openScope(self):
        """Open a scope"""
        self.scope = self.scope.openScope()

    def openFunctionScope(self, function):
        """Open a scope for a function, will record addresses"""
        self.functionAddress = 5 + function.getParameterSize()
        self.functionScope = True
        self.scope = self.scope.openScope()

        #Register the symbols in an arguments(ArgumentsList)
        for argument in function.arguments.arguments:
            if(self.scope.isContainingSymbol(argument.identifier)):
                raise SymbolAlreadyRegisteredError("Symbol '"+ argument.identifier +"' already registered in scope")

            if(argument.basetype.getSize() == 0):
                raise TypeError("Type should have a size greater then 0")

            symbol = Symbol(argument.identifier, argument.basetype, self.scope.getAllocated())
            self.scope.addSymbol(symbol)


    def closeScope(self):
        """Close Scope"""
        if(self.scope.parentScope == None):
            raise ScopeError("No scope opened previously")

        self.scope = self.scope.parentScope

    def closeFunctionScope(self, function):
        """Close a scope for functions"""
        # Save the static data size to the function object
        function.staticsize = self.scope.getTotalAllocated()

        # Close scope
        if(self.scope.parentScope == None):
            raise ScopeError("No scope opened previously")

        self.scope = self.scope.parentScope

        self.functionAddress = 0
        self.functionScope = False

    def registerSymbol(self, identifier, basetype):
        """Register a Symbol in the current scope with an identifier(string) and basetype(Type) is an array(bool)"""
        if(self.scope.isContainingSymbol(identifier)):
            raise SymbolAlreadyRegisteredError("Symbol '"+ identifier +"' already registered in scope")

        if(basetype.getSize() == 0):
            raise TypeError("Type should have a size greater then 0")

        symbol = None
        if(self.functionScope == True):
            symbol = Symbol(identifier, basetype, int(self.functionAddress))
            self.functionAddress += basetype.getSize()
        else:
            symbol = Symbol(identifier, basetype, self.scope.getAllocated())

        self.scope.addSymbol(symbol)

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
        out += "--------------------------------------\n"
        out += self.scope.printer(0) + "\n"
        out += "--------------------------------------\n"

        return out
