# Class representing single parameter
class Parameter:
    """Parameter of function"""
    def __init__(self, expression):
        """initialize with expression(Expression)"""
        self.expression = expression

    def __str__(self):
        """String representation of parameter"""
        return str(self.expression)


class Argument:
    """Argument of a function"""
    def __init__(self, identifier, basetype):
        """initialize with identifier(string) and basetype(Type)"""
        self.identifier = identifier
        self.basetype = basetype

    def __str__(self):
        """String representation of parameter"""
        return "" + str(self.basetype) + ": " + str(self.identifier) + ""

    def __eq__(self, other):
        """Check if 2 parameters are equal"""
        return ((self.basetype == other.basetype))

# Class representing parameters list
class ParametersList:
    """List of paramters of a function"""
    def __init__(self):
        """Initializer"""
        self.parameters = []

    def add(self, parameter):
        """Add a parameter(Parameter), will check if identifiers are unique"""
        # Add
        self.parameters.append(parameter)

    def __str__(self):
        """String representation"""
        out = ""
        for parameter in self.parameters:
            out += str(parameter) + ", "
        return out

    def size(self):
        return len(self.parameters)

    def serialize(self, index):
        """Serialize paramaterList"""
        out = ""
        for parameter in self.parameters:
            out += str(parameter) + ", "
        return out

class ArgumentsList:
    """List of arguments of a function"""
    def __init__(self):
        """Initializer"""
        self.arguments = []

    def add(self, argument):
        """Add a argument(Argyment), will check if identifiers are unique"""
        for i in self.arguments:
            if(i.identifier == argument.identifier):
                raise RuntimeError("Invalid function statement: 2 arguments with same identifier")
                return False

        # Add
        self.arguments.append(argument)

    def __str__(self):
        """String representation"""
        out = ""
        for argument in self.arguments:
            out += str(argument) + ", "
        return out

    def size(self):
        return len(self.arguments)

    def __eq__(self, other):
        """Check if 2 argumentslists are the same"""
        if self.size() != other.size():
            return False

        indexCounter = 0
        while(indexCounter < self.size()):
            if(self.arguments[indexCounter] != other.arguments[indexCounter]):
                return False

            indexCounter += 1

        return True

    def checkCallParameters(self, parametersList):
        """Check if an list of parameters(Parameter) is an valid list of parameters for this argumentList"""
        if(parametersList.size() != self.size()):
            return False

        # Checking of types
        indexCounter = 0
        while(indexCounter < parametersList.size()):
            if(parametersList.parameters[indexCounter].expression.basetype != self.arguments[indexCounter].basetype):
                raise RuntimeError("Parameter " + str(type(parametersList.parameters[indexCounter].expression.basetype)) + " can not be used in argument " + str(type(self.arguments[indexCounter].basetype)))
                return False

            indexCounter += 1

        return True

    def serialize(self, index):
        """Serialize argumentList"""
        out = ""
        for argument in self.arguments:
            out += str(argument) + ", "
        return out
