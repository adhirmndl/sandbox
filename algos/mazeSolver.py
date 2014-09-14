import turtle

PART_OF_PATH = 'x'
TRIED = '.'
OBSTACLE = '+'
DEAD_END = '-'

def searchFrom(maze, startRow, startCol):
	maze.updatePosition(startRow, startCol)
	# OBSTACLE
	if (maze[startRow][startCol] == OBSTACLE):
		return False
	# TRIED 
	if (maze[startRow][startCol] == TRIED):
		return False
	# EXIT
	if (maze.isExit(startRow, startCol)):
		maze.updatePosition(startRow, startCol, PART_OF_PATH)
		return True
	maze.updatePosition(startRow, startCol, TRIED)

	found = searchFrom(maze, startRow - 1, startCol) or \
			searchFrom(maze, startRow + 1, startCol) or \
			searchFrom(maze, startRow, startCol - 1) or \
			searchFrom(maze, startRow, startCol + 1)

	if found:
		maze.updatePosition(startRow, startCol, PART_OF_PATH)
	else:
		maze.updatePosition(startRow, startCol, DEAD_END)

	return found

class Maze:
	def __init__(self, mazefilename):
		f = open(mazefilename)
		self.rep = []
		self.ncols = 0
		self.nrows = 0

		for line in f:
			col = [e for e in line.rstrip('\n')]
			if 'S' in col:
				self.startRow = self.nrows
				self.startCol = col.index('S')
			self.rep.append(col)
			self.ncols = len(col)
			self.nrows += 1

	def updatePosition(self, row, col, pathType=None):
		if pathType:
			self.rep[row][col] = pathType 

	def isExit(self, row, col):
		return row == 0 or row == self.nrows - 1 or col == 0 or col == self.ncols -1

	def __getitem__(self, idx):
		return self.rep[idx]

	def __str__(self):
		mStr = 'rows: ' + str(self.nrows)	+ ' cols: ' + str(self.ncols)
		for row in self.rep:
			mStr += '\n' + ''.join(row) 
		return mStr

if __name__ == "__main__":
	m = Maze('maze1.dat')
	print m
	searchFrom(m, m.startRow, m.startCol)
	print m
