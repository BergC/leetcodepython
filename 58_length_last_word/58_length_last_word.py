class Solution:
    def lengthOfLastWord(self, s):
        """
        Given string return length of last word. If no word exists then return 0.
        https://leetcode.com/problems/length-of-last-word/
        :param s: String
        :return: Int
        """

        s_no_whitespace = s.strip()
        length = 0

        if len(s_no_whitespace) == 0:
            return 0

        words = s_no_whitespace.split(' ')

        return len(words[-1])

test_str = 'Hello World'
answer = Solution().lengthOfLastWord(test_str)
print(answer)
