class Solution:
    def merge(self, nums1: list, m: int, nums2: list, n: int) -> None:
        """
        Merge two sorted arrays and sort the merged array in place.
        :param nums1: List of integers
        :param m: Number of integers to keep from nums1
        :param nums2: List of integer
        :param n: Number of integers in nums2 to be merged into nums1
        :return: None
        """

        index = m

        for num in nums2:
            nums1[index] = num
            index += 1

        nums1.sort()
        return nums1

test1 = [1, 2, 3, 0, 0, 0]
len1 = 3
test2 = [2, 5, 6]
len2 = 3

answer = Solution().merge(test1, len1, test2, len2)

print(answer)