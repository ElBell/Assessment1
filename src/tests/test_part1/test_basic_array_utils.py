from typing import List
from unittest import TestCase

from src.main.part1.basic_array_utils import BasicArrayUtils


class TestBasicArrayUtils(TestCase):

    def test_get_first(self):
        expected: str = "The"
        input_array:  List[str] = ["The", "quick", "brown"]
        actual: str = BasicArrayUtils.get_first_element(input_array)
        self.assertEqual(expected, actual)

    def test_get_second(self):
        expected: str = "quick"
        input_array:  List[str] = ["The", "quick", "brown"]
        actual: str = BasicArrayUtils.get_second_element(input_array)
        self.assertEqual(expected, actual)

    def test_get_last(self):
        expected: str = "brown"
        input_array:  List[str] = ["The", "quick", "brown"]
        actual: str = BasicArrayUtils.get_last_element(input_array)
        self.assertEqual(expected, actual)

    def test_get_second_to_last(self):
        expected: str = "brown"
        input_array:  List[str] = ["The", "quick", "brown", "fox"]
        actual: str = BasicArrayUtils.get_second_to_last_element(input_array)
        self.assertEqual(expected, actual)
