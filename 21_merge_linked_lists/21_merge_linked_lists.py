# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, l1, l2):
        dummy = ListNode(0)

        return dummy.next

answer = Solution().mergeTwoLists([], [])
print(answer)

import numpy

my_array = numpy.array(
    [
        [2, 5],
        [3, 7],
        [1, 3],
        [4, 0]
    ]
)

answer = max(numpy.min(my_array, axis=1))

print(answer)