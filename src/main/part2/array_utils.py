from typing import List, Any


class ArrayUtils:

    @staticmethod
    def get_num_occurrences(check_list: List[Any], check_for: Any) -> int:
        return check_list.count(check_for)

    @staticmethod
    def remove_value(check_list: List[Any], check_for: Any) -> List[Any]:
        while check_list.count(check_for) > 0:
            check_list.remove(check_for)
        return check_list

    @staticmethod
    def get_most_common(check_list: List[Any]) -> Any:
        return max(check_list, key=check_list.count)

    @staticmethod
    def get_least_common(check_list: List[Any]) -> Any:
        return min(check_list, key=check_list.count)

    @staticmethod
    def merge(array1: List[Any], array2: List[Any]) -> List[Any]:
        return array1 + array2
