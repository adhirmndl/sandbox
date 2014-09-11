import string
def toStr(num, base):
	convertString = "0123456789ABCDE"
	if num < base:
		return convertString[num]
	return toStr(num//base, base) + convertString[num%base]

def isPalindrome(word):
	# print word
	if len(word) <= 1:
		return True
	return (word[0] == word[-1]) and isPalindrome(word[1:-1])

def sanctify(word):
	exclude = set(string.punctuation)
	return ''.join((''.join(ch for ch in word if ch not in exclude)).lower().split())

if __name__ == "__main__":
	print toStr(8, 2)
	print isPalindrome(sanctify("radar"))
	print isPalindrome(sanctify("kayak"))
	print isPalindrome(sanctify("aibohphobia"))
	print isPalindrome(sanctify("Live not on evil"))
	print isPalindrome(sanctify("Reviled did I live, said I, as evil I did deliver"))
	print isPalindrome(sanctify("Go hang a salami; I'm a lasagna hog."))
	print isPalindrome(sanctify("Able was I ere I saw Elba"))
	print isPalindrome(sanctify("Kanakanak"))
	print isPalindrome(sanctify("Wassamassaw"))
