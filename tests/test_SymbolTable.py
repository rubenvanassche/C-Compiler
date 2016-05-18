import unittest
from src.SymbolTable import SymbolTable

class TestUM(unittest.TestCase):

    def setUp(self):
        pass

    def test_numbers_3_4(self):
        self.assertEqual( 'aaa', 'aaa')

    def test_strings_a_3(self):
        self.assertEqual( 'aa', 'aaa')

if __name__ == '__main__':
    unittest.main()
