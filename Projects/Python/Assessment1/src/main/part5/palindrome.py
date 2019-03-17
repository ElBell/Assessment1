class Palindrome:
    @staticmethod
    def count_palindromes(string) -> int:
        count = 0
        substrings = [string[i:j + 1] for i in range(len(string)) for j in range(i, len(string))]
        for substring in substrings:
            if substring == substring[::-1]:
                count += 1
        return count
