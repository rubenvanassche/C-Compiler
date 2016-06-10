from src.Type.PrimitiveType import PrimitiveType
from src.Type.Type import Type

class VoidType(PrimitiveType):
    """Integer Type"""
    def __init__(self):
        PrimitiveType.__init__(self, '')

    def __str__(self):
        return "void"

    def getPcode(self):
        return ""

    def serialize(self, level):
        return "VoidType"

    def getSize(self):
        return 0
