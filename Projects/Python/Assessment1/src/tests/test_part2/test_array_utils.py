from typing import List
from unittest import TestCase

from src.main.part2.array_utils import ArrayUtils


class TestArrayUtils(TestCase):

    def test_get_nub_occurrences(self):
        value_to_check: int = 7
        expected: int = 3
        check_in: List[int] = [1, 2, 7, 8, 4, 5, 7, 0, 9, 8, 7]
        actual: int = ArrayUtils.get_num_occurrences(check_in, value_to_check)
        self.assertEqual(expected, actual)

    def test_remove_value(self):
        value_to_remove: int = 7
        expected: List[int] = [1, 2, 8, 4, 5, 0, 9, 8]
        test_list: List[int] = [1, 2, 7, 8, 4, 5, 7, 0, 9, 8, 7]
        actual: List[int] = ArrayUtils.remove_value(test_list, value_to_remove)
        self.assertEqual(expected, actual)

    def test_get_most_common(self):
        expected: int = 7
        test_list: List[int] = [1, 2, 7, 8, 4, 5, 7, 0, 9, 8, 7]
        actual: int = ArrayUtils.get_most_common(test_list)
        self.assertEqual(expected, actual)

    def test_get_least_common(self):
        expected: int = 2
        test_list: List[int] = [1, 1, 2, 3, 3, 3, 4, 4, 4, 4]
        actual: int = ArrayUtils.get_least_common(test_list)
        self.assertEqual(expected, actual)

    def test_merge_arrays(self):
        expected: List[int] = [1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4]
        array1: List[int] = [1, 1, 1, 2, 2, 2]
        array2: List[int] = [3, 3, 3, 4, 4, 4]
        actual: List[int] = ArrayUtils.merge(array1, array2)
        self.assertEqual(expected, actual)
