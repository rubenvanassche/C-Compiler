import unittest
from src.SymbolTable import SymbolTable
from src.Exceptions.SymbolTable import *

from src.Type.IntegerType import IntegerType
from src.Type.AddressType import AddressType
from src.Type.ArrayType import ArrayType
from src.Type.BooleanType import BooleanType
from src.Type.CharacterType import CharacterType
from src.Type.RealType import RealType

class TestUM(unittest.TestCase):
    def setUp(self):
        self.st = SymbolTable()

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

        st.registerAlias('integer', integer)
        st.openScope()
if __name__ == '__main__':
    unittest.main()