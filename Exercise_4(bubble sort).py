def MadMax(N, Tele):
	maxVal = 0
	leftList = []
	rightList = []
	impulseList = []
	halfSize = int((N)/2)
	print(halfSize)

	bubbleSort = True

	while bubbleSort:
		bubbleSort = False
		for i in range(len(Tele)-1):
			if Tele[i] > Tele[i+1]:
				Tele[i], Tele[i+1] = Tele[i+1], Tele[i]
				bubbleSort = True
	maxVal = Tele[N-1]
	del Tele[-1]
	leftList = Tele[:halfSize]
	leftList.append(maxVal)
	rightList = Tele[halfSize:]
	rightList.reverse()
	impulseList = leftList + rightList
	print(range(len(Tele)))
	return(impulseList)
