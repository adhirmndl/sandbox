class LogicGate:
	def __init__(self, n):
		self.label = n
		self.output = None

	def getLabel(self):
		return self.label

	def getOutput(self):
		self.output = self.performGateLogic()
		return self.output

class BinaryGate(LogicGate):
	def __init__(self, n):
		LogicGate.__init__(self, n)

		self.pinA = None
		self.pinB = None

	def getInputA(self):
		if self.pinA == None:
			return int(input("Enter pin A input for gate " + self.getLabel() + " --> "))
		else:
			return self.pinA.getFrom().getOutput()

	def getInputB(self):
		if self.pinB == None:
			return int(input("Enter pin B input for gate " + self.getLabel() + " --> "))
		else:
			return self.pinB.getFrom().getOutput()

	def setNextPin(self, conn):
		if self.pinA == None:
			self.pinA = conn
		else:
			if self.pinB == None:
				self.pinB = conn 
			else:
				raise RunTimeError("Error: NO EMPTY PINS")

class UnaryGate(LogicGate):
	def __init__(self, n):
		LogicGate.__init__(self, n)

		self.pinA = None

	def getInput(self):
		if self.pinA == None:
			return int(input("Enter pin input for gate " + self.getLabel() + " --> "))
		else:
			return self.pinA.getFrom().getOutput()

	def setNextPin(self, conn):
		if self.pinA == None:
			self.pinA = conn
		else:
			raise RunTimeError("Error: NO EMPTY PINS")

class AndGate(BinaryGate):
	def __init__(self, n):
		BinaryGate.__init__(self, n)

	def performGateLogic(self):
		a = self.getInputA()
		b = self.getInputB()

		if a == 1 and b == 1:
			return 1
		else:
			return 0

class OrGate(BinaryGate):
	def __init__(self, n):
		BinaryGate.__init__(self, n)

	def performGateLogic(self):
		a = self.getInputA()
		b = self.getInputB()

		if a == 0 and b == 0:
			return 0
		else:
			return 1

class NotGate(UnaryGate):
	def __init__(self, n):
		UnaryGate.__init__(self, n)

	def performGateLogic(self):
		a = self.getInput()

		if a == 0:
			return 1
		else:
			return 0

class Connector:
	def __init__(self, fromGate, toGate):
		self.fromGate = fromGate
		self.toGate = toGate

		toGate.setNextPin(self)

	def getFrom(self):
		return self.fromGate

	def getTo(self):
		return self.toGate

class NorGate(BinaryGate):
	def __init__(self, n):
		BinaryGate.__init__(self, n)

	def performGateLogic(self):
		gOR = OrGate(self.label)
		gNOT = NotGate(self.label)
		Connector(gOR, gNOT)

		return gNOT.performGateLogic()

class NandGate(BinaryGate):
	def __init__(self, n):
		BinaryGate.__init__(self, n)

	def performGateLogic(self):
		gAND = AndGate(self.label)
		gNOT = NotGate(self.label)
		Connector(gAND, gNOT)

		return gNOT.performGateLogic()


if __name__ == "__main__":

	g1 = AndGate("A and B")
	g2 = AndGate("C and D")
	g1org2 = OrGate("AnB or CnD")

	lhs = NotGate("LHS")

	Connector(g1, g1org2)
	Connector(g2, g1org2)
	Connector(g1org2, lhs)

	g1 = NandGate("A and B") 
	g2 = NandGate("C and D") 

	rhs = AndGate("AnandB and CnandD")

	Connector(g1, rhs)
	Connector(g2, rhs)

	print lhs.getOutput()
	print rhs.getOutput()