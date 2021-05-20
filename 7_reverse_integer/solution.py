class Solution:
    def reverse(self, x: int):
        """
        Reverse the provided signed 32-bit integer.
        :param x: Int
        :return: Int
        """

        x_str = str(x)

        if x_list[len(x_list) - 1] == '-':
            x_list = x_list[0:len(x_list) - 1]
            x_list.insert(0, '-')

        reversed_int = int(''.join(x_list))

        if reversed_int >= (-2 ** 31) and reversed_int <= ((2 ** 31) - 1):
            return reversed_int

        return 0


ret = Solution().reverse(123)

print(ret)