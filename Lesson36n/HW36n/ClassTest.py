import unittest
from Class import SetCalculator

proper_test_set = {-1, 0, 2, 99}
wrong_test_set = {1, 2, 'q'}
wrong_input = [1, 2, 3]


class CalculationTestSuite(unittest.TestCase):
    def setUp(self) -> None:
        self.calc = SetCalculator()
        print(f'setUp called! self : {self}')

    def tearDown(self) -> None:
        print(f'tearDown called! self : {self}')

    # adding
    def test_adding_integers(self):
        result = self.calc.addition(proper_test_set)
        self.assertEqual(result, 100)
        print('\t\nTest 1 is over\n')

    def test_adding_strings(self):
        result = self.calc.addition(wrong_test_set)
        self.assertEqual("Error: wrong input.", result)
        print('\t\nTest 2 is over\n')

    def test_adding_list(self):
        result = self.calc.addition(wrong_input)
        self.assertEqual('Error: input is not a set.', result)
        print('\t\nTest 3 is over\n')

    # average
    def test_average_integers(self):
        result = self.calc.average(proper_test_set)
        self.assertEqual(result, 25)
        print('\t\nTest 4 is over\n')

    def test_average_strings(self):
        result = self.calc.average(wrong_test_set)
        self.assertEqual("Error: wrong input.", result)
        print('\t\nTest 5 is over\n')

    def test_average_list(self):
        result = self.calc.average(wrong_input)
        self.assertEqual('Error: input is not a set.', result)
        print('\t\nTest 6 is over\n')

    # maximum
    def test_maximum_integers(self):
        result = self.calc.set_maximum(proper_test_set)
        self.assertEqual(result, 99)
        print('\t\nTest 7 is over\n')

    def test_maximum_strings(self):
        result = self.calc.set_maximum(wrong_test_set)
        self.assertEqual("Error: wrong input.", result)
        print('\t\nTest 8 is over\n')

    def test_maximum_list(self):
        result = self.calc.set_maximum(wrong_input)
        self.assertEqual('Error: input is not a set.', result)
        print('\t\nTest 9 is over\n')

    # minimum
    def test_minimum_integers(self):
        result = self.calc.set_minimum(proper_test_set)
        self.assertEqual(result, -1)
        print('\t\nTest 10 is over\n')

    def test_minimum_strings(self):
        result = self.calc.set_minimum(wrong_test_set)
        self.assertEqual("Error: wrong input.", result)
        print('\t\nTest 11 is over\n')

    def test_minimum_list(self):
        result = self.calc.set_minimum(wrong_input)
        self.assertEqual('Error: input is not a set.', result)
        print('\t\nTest 12 is over\n')
