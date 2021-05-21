class Solution:
    def climbStairs(self, n):
        """
        Function to determine how distinct ways one can climb n stairs in increments of 1 or 2 steps.
        https://leetcode.com/problems/climbing-stairs/
        :param n: Int representing number of stairs.
        :return: Int representing number of distinct ways one could climb in increments of 1 or 2.
        """

        fib = [1, 1]

        if n >= 2:
            for x in range(2, n + 1):
                print(fib)
                fib.append(fib[x - 2] + fib[x - 1])
                print(fib)

        return fib[-1]


test = 4
answer = Solution().climbStairs(test)

print(answer)
