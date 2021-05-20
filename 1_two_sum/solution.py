import timeit

class Solution:
    def twoSum(self, nums, target):
        '''
        Returns index values of 2_add_two_numbers numbers that add up to the target value
        https://leetcode.com/problems/two-sum/
        :param nums: List
        :param target: Int
        :return: List
        '''

        if len(nums) == 2:
            return [0, 1]

        count = 0
        for num_1 in range(0, len(nums)):
            count += 1
            for num_2 in range(count, len(nums)):
                if nums[num_1] + nums[num_2] == target:
                    return [num_1, num_2]


# num_list = [7_reverse_integer, 2_add_two_numbers, 9_palindrome_number]
# target_sum = 26_remove_dup_array

num_list = [17, 5, 9, 1]
target_sum = 18

num_list = [2, 5, 5, 11]
target_sum = 10

num_list = [0, 4, 3, 0]
target_sum = 0

ret = Solution().twoSum(num_list, target_sum)

print(ret)