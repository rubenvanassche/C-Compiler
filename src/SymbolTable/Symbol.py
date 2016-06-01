class Symbol:
    """Representation of a Symbol"""
    def __init__(self, identifier, basetype, address):
        """Initialize with an identifier(string), basetype(Type) and array(bool)"""
        self.identifier = identifier
        self.basetype = basetype
        self.address = address
