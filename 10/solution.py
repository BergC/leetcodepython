class Solution:
    def maxSubArray(self, nums):
        subarray = [nums[0]]

        for x in range(1, len(nums)):
            subarray.append(max(nums[x] + subarray[x - 1], nums[x]))

        return subarray


answer = Solution().maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4])
print(answer)

#
# def maxSubArray(self, nums: List[int]) -> int:
#     # DP
#     # T: O(N)
#     # S: O(N)
#
#     dp = [0] * len(nums)
#     dp[0] = nums[0]
#     for i in range(1, len(nums)):
#         dp[i] = max(nums[i] + dp[i - 1], nums[i])
#
#     return max(dp)
