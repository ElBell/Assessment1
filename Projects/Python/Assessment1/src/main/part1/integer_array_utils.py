from functools import reduce
from typing import List


class IntegerArrayUtils:

    @staticmethod
    def get_sum(int_input: List[int]) -> int:
        return sum(int_input)

    @staticmethod
    def get_product(int_input: List[int]) -> int:
        return reduce((lambda x, y: x*y), int_input)

    @staticmethod
    def get_average(int_input: List[int]) -> float:
        return IntegerArrayUtils.get_sum(int_input)/len(int_input)
