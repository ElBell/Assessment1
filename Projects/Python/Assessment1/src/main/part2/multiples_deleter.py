from typing import List


class MultiplesDeleter:

    @staticmethod
    def delete_evens(array: List[int]) -> List[int]:
        return MultiplesDeleter.delete_multiples_of_n(array, 2)

    @staticmethod
    def delete_odds(array: List[int]) -> List[int]:
        return [number for number in array if number % 2 == 0]

    @staticmethod
    def delete_multiples_of_three(array: List[int]) -> List[int]:
        return MultiplesDeleter.delete_multiples_of_n(array, 3)

    @staticmethod
    def delete_multiples_of_n(array: List[int], multiple: int) -> List[int]:
        return [number for number in array if number % multiple != 0]
