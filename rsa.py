import random
import sys

def getPrimeByBits(bitLen):
	bitLow = bitLen
	lower = 2**(bitLow - 1)
	upper = 2**bitLen - 1
	l = getPrime(lower, upper)
	return [random.choice(l), random.choice(l)]

def getPrime(lower, upper):
	l = []
	for num in range(lower,upper + 1):
	   # prime numbers are greater than 1
	   if num > 1:
	       for i in range(2,num):
	           if (num % i) == 0:
	               break
	       else:
	       	l.append(num)
	return l
def main():
	primeBits = 8
	primeList = getPrimeByBits(primeBits)
	#primeList = [3, 11]
	p = primeList[0]
	print('p = {' + str(p) + '}')
	q = primeList[1]
	print('q = {' + str(q) + '}')
	n = p * q
	print('n = {' + str(n) + '}')
	phi = (p - 1)*(q - 1)
	print('Phi = {' + str(phi) + '}')
	eList = getPrime(0, phi)
	eResList = []
	for num in eList:
		if is_multiprime(num, phi):
			eResList.append(num)

	e = random.choice(eResList)
	print('Public key = {' + str(e) + ', ' + str(n) + '}')

	d = get_d(e, phi)
	print('Private key = {' + str(int(d)) + ', ' + str(n) + '}')

	text = input('Type your text: ')

	uni = []
	for c in text:
		uni.append(hex(int(ord(c))**int(e) % int(n)))

	print('Encoded message = ' + ''.join(uni))

	priv = []
	for c in uni:
		priv.append(chr((int(c, 16)**int(d)) % int(n)))
	print(str(priv))


def gcd(a, b):
	if b == 0: return a
	else: return gcd(b, a%b)

def is_multiprime(a, b):
	return gcd(a, b) == 1

def get_d(e, tn):
	n = 1
	while (tn*n+1)% e != 0:
		n = n + 1
	d = (tn*n + 1)/e
	return d


main()