import sys
import re
from math import exp

print (sys.version)

csTi = 0.1069
csV = 0.1308
mfpTi = 1.658 / 2
mfpV = 1.628 / 2

fsr = True
limit = 200

def intensity(crossSection, latticeConstant, meanFreePath, offset=0, time=0, isLastSr=True):
	half = 0.5* latticeConstant if isLastSr else 0
	num = 0
	for i in range(time):
		num += exp(-(i + half + offset) * latticeConstant / meanFreePath)
	return crossSection * num

def isCorrectInput(str):
    return True if re.fullmatch('[0-9\/]+', str) else False

def init():
	try:
		print ("V / Ti / V /NSTO")
		print ("Please input each layer number. (exp. 2/2/6)")
		layerNums = input()
		if not isCorrectInput (layerNums):
			raise ValueError("incorect input!")
		layers = [int(s) for s in layerNums.split("/")]
		print ("Please input c-length (A).")
		cLength = input()
		cLength = cLength if cLength else 3.905
		print(layers)
		
		i = 0
		aV = intensity(csV, cLength, mfpV, i, layers[0])
		i += layers[0]
		print(i, aV)
		aTi = intensity(csTi, cLength, mfpTi, i, layers[1])
		i += layers[1]
		print(i, aTi)
		aV += intensity(csV, cLength, mfpV, i, layers[2])
		i += layers[2]
		print(i, aV)
		if limit > i:
			aTi += intensity(csTi, cLength, mfpTi, i, 200 - i)
		
		print("-- calculation Done --")
		print("area V : " + str(aV))
		print("area Ti : " + str(aTi))
		print("area ratio V/Ti : " + str(aV / aTi))
		
	except ValueError as e:
		print(e)
		return False
	else:
		return True

init()