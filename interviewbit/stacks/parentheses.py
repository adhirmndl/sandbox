class Solution:
    # @param A : string
    # @return an integer
    def isValid(self, A):
        brackets = {'(': ')', '{': '}', '[': ']'}
        stack = []
        for c in A:
            if c in brackets.keys():
                stack.append(c)
            else:
                if not stack or brackets[stack.pop()] != c:
                    return 0
        if stack:
            return 0
        return 1

s = Solution()
print s.isValid("()[]{}")
print s.isValid("]}")
