import unittest
from src.SymbolTable.SymbolTable import SymbolTable
from src.SymbolTable.Function import Function
from src.SymbolTable.Symbol import Symbol
from src.Exceptions.SymbolTable import *

from src.Type.IntegerType import IntegerType
from src.Type.AddressType import AddressType
from src.Type.ArrayType import ArrayType
from src.Type.BooleanType import BooleanType
from src.Type.CharacterType import CharacterType
from src.Type.RealType import RealType

from src.Type.Parameter import ParametersList
from src.Type.Parameter import Parameter
from src.Type.Parameter import ArgumentsList
from src.Type.Parameter import Argument

from src.AST.ConstantExpression import ConstantExpression
from src.AST.VariableCallExpression import VariableCallExpression

class TestUM(unittest.TestCase):
    def setUp(self):
        pass

    def test_close_main_scope(self):
        # Should crash
        st = SymbolTable()
        self.assertRaises(ScopeError, lambda: st.closeScope())

    def test_close_too_much_scopes(self):
        st = SymbolTable()
        st.openScope()
        st.closeScope()
        self.assertRaises(ScopeError, lambda: st.closeScope())

    def test_open_and_close_scope(self):
        st = SymbolTable()
        st.openScope()
        st.closeScope()

    def test_register_symbols(self):
        st = SymbolTable()
        integer = IntegerType()
        real = RealType()
        boolean = BooleanType()
        address = AddressType(integer)
        character = CharacterType()
        array = ArrayType(integer, 10)

        st.registerSymbol('int', integer)
        st.registerSymbol('float', real)
        st.registerSymbol('bool', boolean)
        st.registerSymbol('char', character)

        st.registerSymbol('ptr', address)
        st.registerSymbol('array', array)

    def test_register_symbols_nested(self):
        st = SymbolTable()
        integer = IntegerType()
        real = RealType()
        boolean = BooleanType()
        character = CharacterType()

        st.registerSymbol('a', integer)

        st.openScope()
        st.registerSymbol('a', real)

        st.openScope()
        st.registerSymbol('a', boolean)

        st.openScope()
        st.registerSymbol('a', character)

        # Check
        self.assertEqual(type(st.getSymbol('a').basetype), CharacterType)

        st.closeScope()

        self.assertEqual(type(st.getSymbol('a').basetype), BooleanType)

        st.closeScope()

        self.assertEqual(type(st.getSymbol('a').basetype), RealType)

        st.closeScope()

        self.assertEqual(type(st.getSymbol('a').basetype), IntegerType)
    def test_symbol_call(self):
        st = SymbolTable()
        integer = IntegerType()
        real = RealType()
        boolean = BooleanType()
        character = CharacterType()

        st.registerSymbol('a', integer)

        # call in scope
        self.assertEqual(type(st.getSymbol('a').basetype), IntegerType)

        # call in nested scope
        st.openScope()
        self.assertEqual(type(st.getSymbol('a').basetype), IntegerType)

        # define in nested scope
        st.registerSymbol('a', character)

        # call in nested scope
        self.assertEqual(type(st.getSymbol('a').basetype), CharacterType)

        # call original in main scope
        st.closeScope()
        self.assertEqual(type(st.getSymbol('a').basetype), IntegerType)

    def test_double_symbol_definition(self):
        st = SymbolTable()
        integer = IntegerType()

        st.registerSymbol('integer', integer)
        self.assertRaises(SymbolAlreadyRegisteredError, lambda: st.registerSymbol('integer', integer))

    def test_scope_allocated(self):
        st = SymbolTable()

        integer = IntegerType()
        real = RealType()
        boolean = BooleanType()
        character = CharacterType()
        address = AddressType(integer)

        array = ArrayType(integer, 10)

        st.registerSymbol('a', integer)
        st.registerSymbol('b', real)
        st.registerSymbol('c', boolean)
        st.registerSymbol('d', character)
        st.registerSymbol('e', address)

        self.assertEqual(st.scope.allocated, 5)
        self.assertEqual(st.scope.getTotalAllocated(), 5)

        st.openScope()
        st.registerSymbol('a', integer)
        st.registerSymbol('b', real)
        st.registerSymbol('c', boolean)
        st.registerSymbol('d', character)
        st.registerSymbol('e', address)

        self.assertEqual(st.scope.allocated, 5)
        self.assertEqual(st.scope.getTotalAllocated(), 5)
        st.closeScope()

        self.assertEqual(st.scope.allocated, 5)
        self.assertEqual(st.scope.getTotalAllocated(), 10)
        st.registerSymbol('f', array)

        self.assertEqual(st.scope.allocated, 15)
        self.assertEqual(st.scope.getTotalAllocated(), 20)

    def test_not_registered_symbol_call(self):
        st = SymbolTable()
        integer = IntegerType()

        self.assertRaises(SymbolNotRegisteredError, lambda: st.getSymbol('a'))

        # open scope and register
        st.openScope()
        st.registerSymbol('a', integer)
        st.closeScope()

        self.assertRaises(SymbolNotRegisteredError, lambda: st.getSymbol('a'))

    def test_alias_register(self):
        st = SymbolTable()
        integer = IntegerType()

        st.registerAlias('integer', integer)
        self.assertEqual(type(st.getAlias('integer').basetype), IntegerType)

        # call unknown alias
        self.assertRaises(AliasNotRegisteredError, lambda: st.getAlias('a'))

    def test_double_alias(self):
        st = SymbolTable()
        integer = IntegerType()

        st.registerAlias('integer', integer)
        self.assertRaises(AliasAlreadyRegisteredError, lambda: st.registerAlias('integer', integer))

    def test_nested_alias(self):
        st = SymbolTable()
        integer = IntegerType()
        real = RealType()
        boolean = BooleanType()
        character = CharacterType()

        st.registerAlias('a', integer)

        # call in scope
        self.assertEqual(type(st.getAlias('a').basetype), type(IntegerType()))

        # call in nested scope
        st.openScope()
        self.assertEqual(type(st.getAlias('a').basetype), type(IntegerType()))

        # define in nested scope
        st.registerAlias('a', character)

        # call in nested scope
        self.assertEqual(type(st.getAlias('a').basetype), type(CharacterType()))

        # call original in main scope
        st.closeScope()
        self.assertEqual(type(st.getAlias('a').basetype), type(IntegerType()))

    def test_function_register_and_get_no_arguments(self):
        st = SymbolTable()
        integer = IntegerType()
        real = RealType()
        boolean = BooleanType()
        character = CharacterType()


        # Register basic function, no arguments
        st.registerFunction('hello', integer, ArgumentsList(), 0)

        # register function again, shouldn't work
        self.assertRaises(FunctionAlreadyRegisteredError, lambda: st.registerFunction('hello', integer, ArgumentsList(), 0))

        # register function again with other return type, shouldn't work
        self.assertRaises(FunctionAlreadyRegisteredError, lambda: st.registerFunction('hello', boolean, ArgumentsList(), 0))

        # get basic function
        self.assertEqual(type(st.getFunction('hello', ParametersList())), Function)

        # get not known function, should not work
        self.assertRaises(FunctionNotRegisteredError, lambda: st.getFunction('add', ParametersList()))

    def test_function_register_and_get_with_arguments(self):
        st = SymbolTable()
        integer = IntegerType()
        real = RealType()
        boolean = BooleanType()
        character = CharacterType()

        # Create arguments
        argumentsList = ArgumentsList()
        argumentsList.add(Argument('a', integer))
        argumentsList.add(Argument('b', real))

        # Create parameters
        parametersList = ParametersList()
        parametersList.add(Parameter(ConstantExpression(1, 'int')))
        parametersList.add(Parameter(ConstantExpression(3.14, 'float')))

        # fake ParametersList, has one parameters less
        fakeParametersList = ParametersList()
        fakeParametersList.add(Parameter(ConstantExpression(1, 'int')))

        # Register basic function,  arguments
        st.registerFunction('add', integer, argumentsList, 0)

        # register function again, shouldn't work
        self.assertRaises(FunctionAlreadyRegisteredError, lambda: st.registerFunction('add', integer, argumentsList, 0))

        # register function again with other return type, shouldn't work
        self.assertRaises(FunctionAlreadyRegisteredError, lambda: st.registerFunction('add', boolean, argumentsList, 0))

        # get basic function
        self.assertEqual(type(st.getFunction('add', parametersList)), Function)

        # get not known function, should not work
        self.assertRaises(FunctionNotRegisteredError, lambda: st.getFunction('hello', parametersList))

        # get the function with no arguments, shouldn't work
        self.assertRaises(FunctionNotRegisteredError, lambda: st.getFunction('add', ParametersList()))

        # get the function with wrong arguments, shouldn't work
        self.assertRaises(FunctionNotRegisteredError, lambda: st.getFunction('add', fakeParametersList))

    def test_function_scoped(self):
        st = SymbolTable()
        integer = IntegerType()
        real = RealType()
        boolean = BooleanType()
        character = CharacterType()

        # Create arguments
        argumentsList = ArgumentsList()
        argumentsList.add(Argument('a', integer))
        argumentsList.add(Argument('b', real))

        # Create parameters
        parametersList = ParametersList()
        parametersList.add(Parameter(ConstantExpression(1, 'int')))
        parametersList.add(Parameter(ConstantExpression(3.14, 'float')))

        # Register basic function, no arguments
        st.registerFunction('add', integer, argumentsList, 0)

        # Call function in main scope
        self.assertEqual(type(st.getFunction('add', parametersList)), Function)

        # open scope and get function again
        st.openScope()
        self.assertEqual(type(st.getFunction('add', parametersList)), Function)

        # register function in scope
        st.registerFunction('divide', integer, argumentsList, 0)

        # call new function in scope
        self.assertEqual(type(st.getFunction('add', parametersList)), Function)

        # close scope and call new created function, shouldn't work
        st.closeScope()
        self.assertRaises(FunctionNotRegisteredError, lambda:st.getFunction('divide', parametersList) )

        # open scope and register add again
        st.openScope()
        st.registerFunction('add', integer, argumentsList, 0)
        self.assertEqual(type(st.getFunction('add', parametersList)), Function)
        self.assertRaises(FunctionAlreadyRegisteredError, lambda:st.registerFunction('add', integer, argumentsList, 0) )
        st.closeScope()

        # register function in higher scope and call in lower scope
        st.registerFunction('multiply', integer, argumentsList, 0)
        st.openScope()
        self.assertEqual(type(st.getFunction('multiply', parametersList)), Function)
        self.assertRaises(FunctionNotRegisteredError, lambda:st.getFunction('multiplynotexisting', parametersList) )
        st.closeScope

    def test_function_label(self):
        st = SymbolTable()
        integer = IntegerType()
        real = RealType()
        boolean = BooleanType()
        character = CharacterType()

        # Create arguments
        argumentsList = ArgumentsList()
        argumentsList.add(Argument('a', integer))
        argumentsList.add(Argument('b', real))

        # Create parameters
        parametersList = ParametersList()
        parametersList.add(Parameter(ConstantExpression(1, 'int')))
        parametersList.add(Parameter(ConstantExpression(3.14, 'float')))

        # Register basic function, no arguments
        st.registerFunction('add', integer, argumentsList, 0)

        # Check for label
        self.assertEqual(st.getFunction('add', parametersList).label, 'add0')

        # Check for label in scope
        st.openScope()
        st.registerFunction('add', integer, argumentsList, 0)
        self.assertEqual(st.getFunction('add', parametersList).label, 'add1')
        st.closeScope()

    def test_function_parameter_size_array_one_element(self):
        st = SymbolTable()
        integer = IntegerType()
        arrayinteger = ArrayType(integer, 3)

        # Create arguments
        argumentsList = ArgumentsList()
        argumentsList.add(Argument('a', integer))
        argumentsList.add(Argument('b', integer))

        # Create array
        st.registerSymbol('b', arrayinteger)

        # Create parameters
        parametersList = ParametersList()
        parametersList.add(Parameter(ConstantExpression(1, 'int')))
        parametersList.add(Parameter(VariableCallExpression(st.getSymbol('b'), 1)))

        # Register basic function, no arguments
        st.registerFunction('add', integer, argumentsList, 0)
        function = st.getFunction('add', parametersList)

        self.assertEqual(function.getParameterSize(), 2)

    def test_function_parameter_size_array_full(self):
        st = SymbolTable()
        integer = IntegerType()
        arrayinteger = ArrayType(integer, 3)

        # Create arguments
        argumentsList = ArgumentsList()
        argumentsList.add(Argument('a', integer))
        argumentsList.add(Argument('b', arrayinteger))

        # Create array
        st.registerSymbol('b', arrayinteger)

        # Create parameters
        parametersList = ParametersList()
        parametersList.add(Parameter(ConstantExpression(1, 'int')))
        parametersList.add(Parameter(VariableCallExpression(st.getSymbol('b'), None)))

        # Register basic function, no arguments
        st.registerFunction('add', integer, argumentsList, 0)
        function = st.getFunction('add', parametersList)

        self.assertEqual(function.getParameterSize(), 4)

    def test_symbol_address_in_function(self):
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
        st.registerSymbol('a', integer)
        self.assertEqual(st.getSymbol('a').address, 5)
        st.registerSymbol('b', arrayinteger)
        self.assertEqual(st.getSymbol('b').address, 6)
        st.registerSymbol('c', integer)
        self.assertEqual(st.getSymbol('c').address, 9)
        st.closeFunctionScope(function)


        self.assertEqual(function.getStaticSize(), 10)
        self.assertEqual(function.getParameterSize(), 0)

    def test_symbol_address_in_function_with_arguments(self):
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
        st.registerSymbol('c', integer)
        self.assertEqual(st.getSymbol('c').address, 9)
        st.registerSymbol('d', arrayinteger)
        self.assertEqual(st.getSymbol('d').address, 10)
        st.registerSymbol('e', integer)
        self.assertEqual(st.getSymbol('e').address, 13)
        st.closeFunctionScope(function)


        self.assertEqual(function.getStaticSize(), 10)
        self.assertEqual(function.getParameterSize(), 4)



if __name__ == '__main__':
    unittest.main()
