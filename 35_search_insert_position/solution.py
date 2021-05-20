class Solution:
    def searchInsert(self, nums, target):
        if target in nums:
            return nums.index(target)

        nums.insert(0, target)
        nums.sort()

        return nums.index(target)

answer = Solution().searchInsert([1, 3, 5, 6], 7)
print(answer)