from typing import List
from unittest import TestCase

from src.main.part2.multiples_deleter import MultiplesDeleter


class TestMultiplesDeleter(TestCase):

    def test_delete_evens(self):
        array: List[int] = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        expected: List[int] = [1, 3, 5, 7, 9]
        actual: List[int] = MultiplesDeleter.delete_evens(array)
        self.assertEqual(expected, actual)

    def test_delete_odds(self):
        array: List[int] = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        expected: List[int] = [2, 4, 6, 8, 10]
        actual: List[int] = MultiplesDeleter.delete_odds(array)
        self.assertEqual(expected, actual)

    def test_delete_multiples_of_3(self):
        array: List[int] = [3, 6, 9, 12, 15, 4, 7, 10, 13, 16]
        expected: List[int] = [4, 7, 10, 13, 16]
        actual: List[int] = MultiplesDeleter.delete_multiples_of_three(array)
        self.assertEqual(expected, actual)

    def test_delete_multiples_of_n(self):
        multiple: int = 6
        array: List[int] = [6, 12, 18, 24, 30, 4, 7, 10, 13, 16]
        expected: List[int] = [4, 7, 10, 13, 16]
        actual: List[int] = MultiplesDeleter.delete_multiples_of_n(array, multiple)
        self.assertEqual(expected, actual)
