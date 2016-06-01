# Symbol Table
from src.SymbolTable.SymbolTable import SymbolTable

# AST Imports
from src.AST.AmpersandExpression import AmpersandExpression
from src.AST.ArithmeticExpression import ArithmeticExpression
from src.AST.AssignmentExpression import AssignmentExpression
from src.AST.BreakStatement import BreakStatement
from src.AST.ComparisonExpression import ComparisonExpression
from src.AST.CompoundStatement import CompoundStatement
from src.AST.ConstantExpression import ConstantExpression
from src.AST.ContinueStatement import ContinueStatement
from src.AST.DecrementerExpression import DecrementerExpression
from src.AST.Expression import Expression
from src.AST.ForStatement import ForStatement
from src.AST.FunctionCallExpression import FunctionCallExpression
from src.AST.FunctionStatement import FunctionStatement
from src.AST.IfelseStatement import IfelseStatement
from src.AST.IncludeStatement import IncludeStatement
from src.AST.IncrementerExpression import IncrementerExpression
from src.AST.LogicExpression import LogicExpression
from src.AST.NegateExpression import NegateExpression
from src.AST.NotExpression import NotExpression
from src.AST.Program import Program
from src.AST.ReturnStatement import ReturnStatement
from src.AST.StarExpression import StarExpression
from src.AST.Statement import Statement
from src.AST.TypedefStatement import TypedefStatement
from src.AST.VariableCallExpression import VariableCallExpression
from src.AST.VariableExpression import VariableExpression
from src.AST.WhileStatement import WhileStatement

# Types
from src.Type.AddressType import AddressType
from src.Type.ArrayType import ArrayType
from src.Type.BooleanType import BooleanType
from src.Type.CharacterType import CharacterType
from src.Type.IntegerType import IntegerType
from src.Type.RealType import RealType

from src.Type.Parameter import Parameter
from src.Type.Parameter import ParametersList
from src.Type.Parameter import Argument
from src.Type.Parameter import ArgumentsList

# Data
from src.Data.AddressData import AddressData

class SemanticCheck:
"""Check a program semanticly"""

    def __init__(self, program):
        """Initiate with program(Program)"""
        self.program = program

    def checkMain(self):
        """Check's if a main function is available"""
        pass
