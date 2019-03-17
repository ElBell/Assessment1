
class BasicStringUtils:

    @staticmethod
    def camel_case(string_input: str) -> str:
        return string_input[0].upper() + string_input[1:]

    @staticmethod
    def reverse(string_input: str) -> str:
        return string_input[::-1]

    @staticmethod
    def reverse_then_camel(string_input: str) -> str:
        return BasicStringUtils.camel_case(BasicStringUtils.reverse(string_input))

    @staticmethod
    def remove_first_and_last(string_input: str) -> str:
        return string_input[1:-1]

    @staticmethod
    def invert_casing(string_input: str) -> str:
        return string_input.swapcase();
