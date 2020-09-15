def MadMax(N, Tele):
	maxVal = 0
	leftList = []
	rightList = []
	impulseList = []
	halfSize = int((N)/2)
	print(halfSize)
	
	Tele.sort()
	print(Tele)
	
	maxVal = Tele[N-1]
	del Tele[-1]
	
	leftList = Tele[:halfSize]
	leftList.append(maxVal)
	rightList = Tele[halfSize:]
	rightList.reverse()
	impulseList = leftList + rightList
	print(range(len(Tele)))
	return(impulseList)
