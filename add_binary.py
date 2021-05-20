class Solution:
    def addBinary(self, a: str, b: str):
        """
        Given two binary strings, return their sum as a binary string.
        https://leetcode.com/problems/add-binary/
        :param a: String representation of a binary number.
        :param b: String representation of a binary number.
        :return: String representing of the binary number of the sum of a and b.
        """

        return format(int(a, 2) + int(b, 2), 'b')

test_a = '11'
test_b = '1'

answer = Solution().addBinary(test_a, test_b)

print(answer)