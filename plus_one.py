class Solution:
    def plusOne(self, digits):
        """
        Increment the number derived from joining the integers of a list and return a list of the digits.
        https://leetcode.com/problems/plus-one/
        :param digits: List of digits
        :return: List of digits
        """

        digits = [str(x) for x in digits]
        digit = int(''.join(digits))
        digit += 1

        incremented_digits = [int(x) for x in str(digit)]

        return incremented_digits

test = [9, 9, 9]
answer = Solution().plusOne(test)

print(answer)
