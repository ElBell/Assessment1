from typing import List


class StringUtils:

    @staticmethod
    def get_words(input_string: str) -> List[str]:
        return input_string.split()

    @staticmethod
    def get_first_word(input_string: str) -> str:
        return StringUtils.get_words(input_string)[0]

    @staticmethod
    def reverse_first_word(input_string: str) -> str:
        return StringUtils.get_first_word(input_string)[::-1]

    @staticmethod
    def reverse_first_camel(input_string: str) -> str:
        first_word = StringUtils.reverse_first_word(input_string)
        return first_word[0].upper() + first_word[1:]

    @staticmethod
    def remove_char_at_index(input_str, index) -> str:
        return input_str[:index] + input_str[index + 1:]
