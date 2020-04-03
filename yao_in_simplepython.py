
import random

def encryptDecrypt(message,key):
	c = pow(message,key[0])%key[1]	
	return c
''' Function : To check Prime '''
def isPrime(i):
	for j in range(2,i):
		if(i%j==0):
			return False
	return True


# Input global range 
r1 = int(input('Enter global range r1 <= x,y <= r2 : '))
r2 = int(input('Enter r2 : '))
print(' Global Range : ', r1 ,' <= x,y <= ',r2)

x = int(input('Enter value of Alice secret x  (within global range) = ')) 
y = int(input('Enter value of Bob secret y (within global range) = '))

# Input RSA parameters of Bob
e= int(input('Enter public key of Bob e = ')) 
d= int(input('Enter private key of Bob d = ')) 
n= int(input('Enter n  = '))

# Public key of Bob
publicKeyBob =[e,n]
# Private key of Bob
privateKeyBob= [d,n]

'''
Alice Compute C = E(PUb, M1), M1 -- a large
random number
 Compute C1 = C – x and sends C1 to Bob
'''
N = n.bit_length()
# choose random M1
m1= random.getrandbits(N)
while m1 >= n:
	m1 = random.getrandbits(N)
N = m1.bit_length()
# Alice encrypts m1 using publicKeyBob RSA 
c = encryptDecrypt(m1,publicKeyBob)
#Alice sends C=C-x to Bob
c = c-x
# 3. Bob computes M2 i = D(PRb,C1+i), for r1<= i <=r2
rangeN = r2+r1-1
n = [0]*(rangeN+1)

for i in range(1, len(n)):
	n[i] = encryptDecrypt(c+i,privateKeyBob)

m = n[1:]
# 4. Choose a large prime p (<M1); Bob can know the size of M1

primes = [i for i in range(2,2**(N-1)) if isPrime(i)]

# 5. Compute Z i = M2 i mod p, 1<=i<100
z= [0]*(rangeN)
prime = random.choice(primes)
primes.remove(prime)

for i in range(0, len(m)):
	z[i] = m[i]%prime
condt=0

'''Verify if |Z i – Z j | >= 2 for all (i,j) and 0 < Z i < p-1, for all i,
otherwise try another prime and repeat from step-4 '''
while condt == 0:
	for i in range(0, len(m)):
		for j in range(i+1 , len(m)):
			if( abs(z[i]-z[j]) < 2):
				condt=0
	if condt == 1:
		for i in range(0,len(m)):
			if(z[i]>=prime or z[i]<=0):
				condt=0
	if condt == 0:
		if primes:
			prime = random.choice(primes)
		# If conditions fails repeat the process
			primes.remove(prime)
			for i in range(0,len(m)):
				z[i]=m[i]%prime
		else:
			break
# sequence
for i in range(y,len(z)):
	z[i]=z[i]+1

''' Alice recevies sequence z[]
Select z[x] , Check  if z[x] = m1 mod prime'''

if(m1%prime == z[x-1]):
	print("y > x") # Bob's secret is greater than Alice's secret
else:
	print("x > y") # Alice's secret is greater than Bob's secret"
