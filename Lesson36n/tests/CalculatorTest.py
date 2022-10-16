import unittest
from Lesson36n.Lesson36n_1 import Calculator


class CalculationTestSuite(unittest.TestCase):
    def setUp(self) -> None:
        self.calc = Calculator()
        print(f'setUp called! self : {self}')

    def tearDown(self) -> None:
        print(f'tearDown called! self : {self}')

    def test_adding_two_integers(self):
        result = self.calc.addition(5, 5)
        self.assertEqual(result, 10)
        print('\t\nTest one is over\n')

    def test_adding_two_strings(self):
        result = self.calc.addition('5a', '5')
        self.assertEqual('Addition Error', result)
        print('\t\nTest two is over\n')
