# Class representing single parameter
class Parameter:
    """Paramter of function"""
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
        for i in self.parameters:
            if(i.identifier == parameter.identifier):
                raise RuntimeError("Invalid function statement: 2 parameters with same identifier")
                return False

        # Add
        self.parameters.append(parameter)

    def __str__(self):
        """String representation"""
        out = ""
        for parameter in self.parameters:
            out += str(parameter) + ", "
        return out

    def checkCallArguments(self, argumentsList):
        """Check if an list of arguments([Expression]) is an valid list of arguments for this paramaterList"""
        if(len(argumentsList) != len(self.parameters)):
            return False

        # TODO CHECKING OF TYPES
        return True

    def serialize(self, index):
        """Serialize paramaterList"""
        out = ""
        for parameter in self.parameters:
            out += str(parameter) + ", "
        return out
