class Solution:
    def longestCommonPrefix(self, strs: list) -> str:
        """
        Method should find longest common prefix amongst list of strings, otherwise return "".
        https://leetcode.com/problems/longest-common-prefix/
        :param strs: List of strings.
        :return: String representing longest common prefix.
        """

        # Constraints allow for only one word in strs, in which case that word would be the longest prefix.
        if len(strs) == 1:
            return strs[0]
        elif len(strs) == 0:
            return ''

        longest_possible_prefix = min(strs, key=len)

        longest_prefix = ""

        for num in range(len(longest_possible_prefix)):
            observed_letter = strs[0][num]

            if all([word[num] == observed_letter for word in strs]):
                longest_prefix += observed_letter
            else:
                break

        return longest_prefix


test = ["flower","flow","flight"]
answer = Solution().longestCommonPrefix(test)

print(answer)
