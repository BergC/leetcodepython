import math


class Solution:
    def mySqrt(self, x: int):
        """
        Given non-negative integer return square root with decimal digits truncated.
        https://leetcode.com/problems/sqrtx/
        :param x: Integer to be square rooted.
        :return: Integer representing square root of x rounded down to whole number.
        """

        root = math.sqrt(x)

        return math.floor(root)

test = 8
answer = Solution().mySqrt(test)

print(answer)
