ruleTable = {}
for i in range(32):
	ruleTable[i] = []

n = input()
for _ in range(n):
	query, address = raw_input().strip().split(' ')
	if query != "QUERY":
		ip, mask = address.split('/')
		print ip
		mask = int(mask)
		binAddress = ''.join([bin(int(x)+256)[3:] for x in ip.split('.')])
		print ip, mask, binAddress
		ruleBits = binAddress[:mask]
		if query == "TRUST":
			ruleTable[mask].append((ruleBits, "TRUST"))
			print "OK"
		elif query == "NOTRUST":
			ruleTable[mask].append((ruleBits, "NOTRUST"))
			print "OK"
		elif query == "REMOVE":
			flag = True
			for rBits, level in ruleTable[mask]:
				if rBits == ruleBits:
					ruleTable[mask].remove((rBits, level))
					print "OK"
					flag = False
			if flag:
				print "NULL"
	else:
		#code for QUERY
		curLevel = None
    	ip = address
    	binAddress = ''.join([bin(int(x)+256)[3:] for x in ip.split('.')])
    	for bitMask, rule in ruleTable.iteritems():
    		maskedIP = binAddress[:bitMask]
    		for (ruleBits, level) in rule:
    			if ruleBits == maskedIP:
    				curLevel = level
    	print curLevel	