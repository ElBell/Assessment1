from unittest import TestCase

from src.tests.test_part1.test_basic_string_utils import BasicStringUtils


class TestBasicStringUtils(TestCase):

    def test_camel_case(self):
        string_input: str = "the quick brown fox"
        expected: str = "The quick brown fox"
        actual: str = BasicStringUtils.camel_case(string_input)
        self.assertEqual(expected, actual)

    def test_reverse(self):
        string_input: str = "the quick brown fox"
        expected: str = "xof nworb kciuq eht"
        actual: str = BasicStringUtils.reverse(string_input)
        self.assertEqual(expected, actual)

    def test_reverse_then_camel(self):
        string_input: str = "the quick brown fox"
        expected: str = "Xof nworb kciuq eht"
        actual: str = BasicStringUtils.reverse_then_camel(string_input)
        self.assertEqual(expected, actual)

    def test_remove_first_and_last(self):
        string_input: str = "The quick brown"
        expected: str = "he quick brow"
        actual: str = BasicStringUtils.remove_first_and_last(string_input)
        self.assertEqual(expected, actual)

    def test_invert_casing1(self):
        string_input: str = "tHE quiCK brOwN"
        expected: str = "The QUIck BRoWn"
        actual: str = BasicStringUtils.invert_casing(string_input)
        self.assertEqual(expected, actual)

    def test_invert_casing2(self):
        expected: str = "tHE quiCK brOwN"
        actual: str = BasicStringUtils.invert_casing(BasicStringUtils.invert_casing(expected))
        self.assertEqual(expected, actual)
