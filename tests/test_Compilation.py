import unittest

from src.SymbolTable.SymbolTable import SymbolTable
from src.SymbolTable.Function import Function
from src.SymbolTable.Symbol import Symbol

from src.AST.FunctionStatement import FunctionStatement
from src.AST.ConstantExpression import ConstantExpression
from src.AST.VariableCallExpression import VariableCallExpression
from src.AST.VariableExpression import VariableExpression

from src.Type.Parameter import Parameter
from src.Type.Parameter import ParametersList
from src.Type.Parameter import Argument
from src.Type.Parameter import ArgumentsList

from src.Type.IntegerType import IntegerType
from src.Type.ArrayType import ArrayType

class TestUM(unittest.TestCase):

    def setUp(self):
        pass

    def test_compile_function_statement_no_arguments_no_statements(self):
        function = Function('main', IntegerType(), ArgumentsList(), 0, "main0")
        statement = FunctionStatement(function, [])

        self.assertEqual(function.getStaticSize(), 5)
        self.assertEqual(function.getParameterSize(), 0)
        self.assertEqual(statement.compile(), "main0:\nssp 5\nretp\n")

    def test_compile_function_arguments_no_statements(self):
        st = SymbolTable()

        integer = IntegerType()
        arrayinteger = ArrayType(integer, 3)

        # Create arguments
        argumentsList = ArgumentsList()
        argumentsList.add(Argument('a', integer))
        argumentsList.add(Argument('b', arrayinteger))

        # Create parameters
        parametersList = ParametersList()
        parametersList.add(Parameter(ConstantExpression(1, 'int')))
        parametersList.add(Parameter(VariableCallExpression(Symbol('b', arrayinteger, 0), None)))

        st.registerFunction('main', integer, argumentsList, 0)
        function = st.getFunction('main', parametersList)
        st.openFunctionScope(function)

        st.closeFunctionScope(function)


        statement = FunctionStatement(function, [])

        self.assertEqual(function.getStaticSize(), 5)
        self.assertEqual(function.getParameterSize(), 4)
        self.assertEqual(statement.compile(), "main0:\nssp 5\nretp\n")

    def test_compile_function_no_arguments_statements(self):
        st = SymbolTable()

        integer = IntegerType()
        arrayinteger = ArrayType(integer, 3)

        # Create arguments
        argumentsList = ArgumentsList()

        # Create parameters
        parametersList = ParametersList()

        st.registerFunction('main', integer, argumentsList, 0)
        function = st.getFunction('main', parametersList)
        st.openFunctionScope(function)


        st.closeFunctionScope(function)


        statement = FunctionStatement(function, [])

        self.assertEqual(function.getStaticSize(), 5)
        self.assertEqual(function.getParameterSize(), 0)
        self.assertEqual(statement.compile(), "main0:\nssp 5\nretp\n")

    def test_strings_a_3(self):
        self.assertEqual( 'aaa', 'aaa')

if __name__ == '__main__':
    unittest.main()
