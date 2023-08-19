import unittest
from app.roman_numerals import parse

class TestNumerals(unittest.TestCase):

    def test_i(self):
        result = parse('I')
        self.assertEqual(result, 1)

    def test_ii(self):
        result = parse('II')
        self.assertEqual(result, 2)

    def test_iii(self):
        result = parse('III')
        self.assertEqual(result, 3)

    def test_iv(self):
        result = parse('IV')
        self.assertEqual(result, 4)

    def test_v(self):
        result = parse('V')
        self.assertEqual(result, 5)

    def test_vi(self):
        result = parse('VI')
        self.assertEqual(result, 6)

    def test_vii(self):
        result = parse('VII')
        self.assertEqual(result, 7)

    def test_viii(self):
        result = parse('VIII')
        self.assertEqual(result, 8)
