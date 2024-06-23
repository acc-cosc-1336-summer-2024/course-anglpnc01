import unittest

from src.homework.d_repetition.repetition import get_factorial_for
from src.homework.d_repetition.repetition import sum_odd_numbers

class Test_Config(unittest.TestCase):

    def test_get_factorial_1(self):
        self.assertEqual(24, get_factorial_for(4))
        self.assertEqual(120, get_factorial_for(5))
        self.assertEqual(720, get_factorial_for(6))

    def test_sum_odd_numbers_1(self):
        self.assertEqual(16, sum_odd_numbers(7))
        self.assertEqual(25, sum_odd_numbers(9))
        self.assertEqual(25, sum_odd_numbers(10))

    