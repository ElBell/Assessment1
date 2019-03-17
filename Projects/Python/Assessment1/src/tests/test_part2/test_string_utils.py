from typing import List
from unittest import TestCase

from src.main.part2.string_utils import StringUtils


class TestStringUtils(TestCase):

    def test_get_words(self):
        input_string: str = "The quick brown fox jumps"
        expected: List[str] = ["The", "quick", "brown", "fox", "jumps"]
        actual: List[str] = StringUtils.get_words(input_string)
        self.assertEqual(expected, actual)

    def test_get_first_word(self):
        input_string: str = "Quick Brown Fox"
        expected: str = "Quick"
        actual: str = StringUtils.get_first_word(input_string)
        self.assertEqual(expected, actual)

    def test_reverse_first_word(self):
        input_string: str = "Noel Hunter"
        expected: str = "leoN"
        actual: str = StringUtils.reverse_first_word(input_string)
        self.assertEqual(expected, actual)

    def test_reverse_first_camel(self):
        input_string: str = "noel Hunter"
        expected: str = "Leon"
        actual: str = StringUtils.reverse_first_camel(input_string)
        self.assertEqual(expected, actual)

    def test_remove_char_at_index(self):
        input_str: str = "Jumping"
        index: int = 2
        expected: str = "Juping"
        actual:str = StringUtils.remove_char_at_index(input_str, index)
        self.assertEqual(expected, actual)
