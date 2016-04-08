class Solution:
    # @param A : integer
    # @return a strings
    def convertToTitle(self, A):
        name = []
        num  = A
        while num:
            digit = (num -1) % 26
            num = int((num-digit)/26)
            name.append(digit)
        name = name[::-1]
        name = [chr(i+65) for i in name]
        return ''.join(name)

s = Solution()
print s.convertToTitle(676)
print s.convertToTitle(980089)
print s.convertToTitle(52)