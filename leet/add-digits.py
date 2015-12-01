"""
Given a non-negative integer num,
repeatedly add all its digits until the result has only one digit.

For example:

Given num = 38,
the process is like: 3 + 8 = 11, 1 + 1 = 2.
Since 2 has only one digit, return it.

Follow up:
Could you do it without any loop/recursion in O(1) runtime?
"""
class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        if num == 0: return 0
        if num % 9 == 0: return 9
        return num % 9

if __name__ == '__main__':
    sol = Solution()
    print sol.addDigits(152)
    print sol.addDigits(898)
    print sol.addDigits(428)
    print sol.addDigits(9)
    print sol.addDigits(1)
    print sol.addDigits(8)
