class Solution:
    def isPalindrome(self, x: int):
        if x < 0:
            return False

        reversed_x = int(str(x)[::-1])

        if reversed_x == x:
            return True

        return False

test = 121

ret = Solution().isPalindrome(test)

print(ret)