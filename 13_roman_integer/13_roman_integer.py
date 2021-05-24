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
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

        raw_values = [roman_numerals[char] for char in s]

        running_total = raw_values[0]

        last_value = raw_values[0]

        for curr_value in raw_values[1:]:
            if curr_value > last_value:
                running_total -= last_value * 2
                running_total += curr_value
            else:
                running_total += curr_value

            last_value = curr_value

        return running_total


test = 'MCMXCIV'
answer = Solution().romanToInt(test)

print(answer)
