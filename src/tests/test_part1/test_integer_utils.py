from unittest import TestCase

from src.main.part1.integer_utils import IntegerUtils


class TestIntegerUtils(TestCase):

    def test_get_sum(self):
        input_int: int = 5
        expected: int = 15
        actual: int = IntegerUtils.get_sum(input_int)
        self.assertEqual(expected, actual)

    def test_get_product(self):
        input_int: int = 5
        expected: int = 120
        actual: int = IntegerUtils.get_product(input_int)
        self.assertEqual(expected, actual)

    def test_reverse_digits_test(self):
        input_int: int = 12345
        expected: int = 54321
        actual: int = IntegerUtils.reverse_digits(input_int)
        self.assertEqual(expected, actual)
