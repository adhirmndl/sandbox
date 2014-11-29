def isanagram(word1, word2):
	if len(word1) != len(word2):
		return falseZ
	check = 0
	for e in word1:
		check ^= ord(e)
	for e in word2:
		check ^= ord(e)
	return check == 0

# if __name__ == "__main__":
# 	print isanagram('asad', 'dasa')

class HashTable:
	def __init__(self):
		size = 10
		baseTable = []
		for i in range (size):
			baseTable.append([])
			
	def hashF(self, n):
		return n% self.size

	def put(self, key, value):
		baseTable[hashF(key)].append((key, value))

	def __str__(self):
		return str(baseTable)
if __name__ == "__main__":
	hT = HashTable()
