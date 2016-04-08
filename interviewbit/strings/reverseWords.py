class Solution:
    # @param A : string
    # @return string
    def reverseWords(self, A):
    	words = []
    	currWord = ''
    	for i in A:
    		if i != ' ':
    			currWord += i
    		elif currWord != '':
    			words.append(currWord)
    			currWord = ''
    	if A[-1] != ' ':
    		words.append(currWord)
    	return ' '.join(words[::-1])

s = Solution()
print s.reverseWords("  this   is   a    test   string")
print s.reverseWords("  this   jamboree  ")
print s.reverseWords("j")
print s.reverseWords(" ")
