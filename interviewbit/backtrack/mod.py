class Solution:
    # @param A : integer
    # @param B : integer
    # @param C : integer
    # @return an integer
    def Mod(self, A, B, C):
        if B == 0:
            return 1
        if B % 2 == 0:
            temp = self.Mod(A, B/2, C)
            return (temp**2)%C
        else:
            first = A%C
            second = self.Mod(A, B - 1, C)
            return (first*second)%C

import unittest
class SolutionTester(unittest.TestCase):
    def testCase1(self):
        s = Solution()
        self.assertEquals(s.Mod(-1, 1, 20), 19)

if __name__=="__main__":
    unittest.main()