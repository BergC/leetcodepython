class Solution:
    def removeDuplicates(self, nums):
        index = 0

        while index < len(nums) - 1:
            if nums[index] == nums[index + 1]:
                nums.pop(index + 1)
            else:
                index += 1

        return len(nums)


ret = Solution().removeDuplicates([1, 1, 1, 1])

print(ret)
