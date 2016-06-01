import unittest
from src.SymbolTable import SymbolTable

from src.AST.FunctionStatement import FunctionStatement

class TestUM(unittest.TestCase):

    def setUp(self):
        pass

    def test_compile_function_basic(self):
        pass

    def test_strings_a_3(self):
        self.assertEqual( 'aaa', 'aaa')

if __name__ == '__main__':
    unittest.main()
