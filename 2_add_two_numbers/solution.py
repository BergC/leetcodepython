class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverse_list(self, list_of_ints):
        """
        Reverse a list of ints and return the int value of joining the individual digits.
        :param list_of_ints: List of integers, non-zero, between 1_two_sum and 9_palindrome_number.
        :return: Int
        """

        list_to_iterable = [str(x) for x in list_of_ints]

        list_to_iterable.reverse()

        list_to_int = int(''.join(list_to_iterable))

        return list_to_int

    def create_list(self, sum_value):
        """

        :param sum_value: Int
        :return: List
        """

        sum_to_str = str(sum_value)

        str_to_list = [x for x in sum_to_str]

        str_to_list.reverse()

        return str_to_list

    def addTwoNumbers(self, l1: ListNode, l2: ListNode):
        """
        See desc.md. Receive 2_add_two_numbers non-empty linked lists in reverse order and return their sum as a list.
        :param l1: List of single digits, no negatives, no leading zeros.
        :param l2: List of single digits, no negatives, no leading zeros.
        :return: List of the sum of the reversed l1 and l2 arguments.
        """

        l1_reversed = self.reverse_list(l1)
        l2_reversed = self.reverse_list(l2)

        summed_numbers = l1_reversed + l2_reversed

        sum_as_list = self.create_list(
            summed_numbers)

        return sum_as_list


list_1 = [2, 4, 3]
list_2 = [5, 6, 4]

ret = Solution().addTwoNumbers(list_1, list_2)

print(ret)
