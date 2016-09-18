'''
Given a digit string, return all possible letter combinations that the number could represent.

A mapping of digit to letters (just like on the telephone buttons) is given below.

The digit 0 maps to 0 itself.
The digit 1 maps to 1 itself.

Input: Digit string "23"
Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
Make sure the returned strings are lexicographically sorted.
'''

class Solution:
	def __init__(self):
		self.digitmap = { 0 : "0"
           , 1 : list("1")
           , 2 : list("abc")
           , 3 : list("def")
           , 4 : list("ghi")
           , 5 : list("jkl")
           , 6 : list("mno")
           , 7 : list("pqrs")
           , 8 : list("tuv")
           , 9 : list("wxyz")
           }

	# @param A : string
	# @return a list of strings
	def letterCombinations(self, A):
		if len(A) == 1:
			return self.digitmap[int(A)]
		prefix = self.digitmap[int(A[0])]
		suffix = self.letterCombinations(A[1:])
		result = []
		for pre in prefix:
			for suf in suffix:
				res = pre + suf
				result.append(res)
		return result

import unittest
class SolutionTester(unittest.TestCase):
	def testCase1(self):
		expected = ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]
		s = Solution()
		self.assertEquals(s.letterCombinations("23"), expected)

	def testCase2(self):
		expected = ["dgj", "dgk", "dgl", "dhj", "dhk", "dhl", "dij", "dik", "dil",
		"egj", "egk", "egl", "ehj", "ehk", "ehl", "eij", "eik", "eil", "fgj", 
		"fgk", "fgl", "fhj", "fhk", "fhl", "fij", "fik", "fil"]
		s = Solution()
		self.assertEquals(s.letterCombinations("345"), expected)

if __name__ == "__main__":
	unittest.main()