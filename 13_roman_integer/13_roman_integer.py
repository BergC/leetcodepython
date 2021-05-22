class Solution:
    def romanToInt(self, s: str) -> int:
        """
        Convert a roman numeral to its integer value.
        https://leetcode.com/problems/roman-to-integer/
        :param s: String representing a roman numeral.
        :return: Integer value of the input.
        """

        roman_numerals = {
            'I': 1,
            'IV': 4,
            'V': 5,
            'IX': 9,
            'X': 10,
            'XL': 40,
            'L': 50,
            'XC': 90,
            'C': 100,
            'CD': 400,
            'D': 500,
            'CM': 900,
            'M': 1000
        }

        running_total = 0

        raw_values = [roman_numerals[char] for char in s]





test = 'XIV'
answer = Solution().romanToInt(test)

print(answer)
