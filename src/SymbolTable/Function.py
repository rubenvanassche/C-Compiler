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
        size = 5 + self.staticsize - self.getParameterSize()

        return size

    def getParameterSize(self):
        """Get the parameter size required for the cup command"""
        size = 0

        for argument in self.arguments.arguments:
            size += argument.basetype.getSize()

        return size
