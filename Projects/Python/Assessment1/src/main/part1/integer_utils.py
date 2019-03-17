from functools import reduce


class IntegerUtils:

    @staticmethod
    def get_sum(input_int: int) -> int:
        return sum(range(input_int + 1))

    @staticmethod
    def get_product(input_int: int) -> int:
        return reduce((lambda x, y: x*y), range(1, input_int + 1))

    @staticmethod
    def reverse_digits(input_int: int) -> int:
        return int(str(input_int)[::-1])
