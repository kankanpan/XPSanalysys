from math import exp
def test(b,d,a,o):
	num = 0
	for i in range(100):
		num += exp(-(i*d+a)/o)
	return b*num

iti = 4548.13
iv = 13935.1
c = 3.846368571

fti = False

ati = test(0.1069, c, 0 if fti else 0.5*c, 1.658)
av = test(0.1308, c, 0 if fti else 0.5*c, 1.628)

result = iti*av/(iv*ati)

print ("Ti/V")
print (fti)
print (result)

print ("(sum=1)")
print (1/(1+result))
print (1/(1+result)*result)