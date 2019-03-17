from typing import List
from unittest import TestCase

from src.main.part1.integer_array_utils import IntegerArrayUtils


class IntegerArrayUtilsTest(TestCase):

    def test_get_sum(self):
        int_input: List[int] = [1, 2, 3, 4, 5]
        expected: int = 15
        actual: int = IntegerArrayUtils.get_sum(int_input)
        self.assertEqual(expected, actual)

    def test_get_product(self):
        int_input: List[int] = [1, 2, 3, 4, 5]
        expected: int = 120
        actual: int = IntegerArrayUtils.get_product(int_input)
        self.assertEqual(expected, actual)

    def test_get_average(self):
        int_input: List[int] = [1, 2, 3, 4, 5]
        expected: float = 3
        actual: int = IntegerArrayUtils.get_average(int_input)
        self.assertEqual(expected, actual)
