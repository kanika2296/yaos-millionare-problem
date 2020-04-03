import socket
import pickle
import random
import time

BUFSIZE = 1024

''' Function: RSA encryption & Decryption'''
def encryptDecrypt(message,key):
	c = pow(message,key[0])%key[1]	
	return c
''' Function : To check Prime '''
def isPrime(i):
	for j in range(2,i):
		if(i%j==0):
			return False
	return True

# create socket
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# connect the client
# client.connect((target, port))
client.connect(('127.0.0.1', 1233))
response = client.recv(BUFSIZE)
print(response.decode())
# send client name
client.send(str.encode("Bob"))
response = client.recv(BUFSIZE)
# send online message
client.send(str.encode("ONLINE#"))

# Input global range 
r1 =1
r2 =10
# Input y, secret value
y = int(input('Enter value of Bob secret y (within 1 <=x<= 20) :  ')) 
# Input e
e= int(input('Enter public key of Bob e = ')) 
# Send e
client.send(str.encode(str(e)))
print("Public key e sent ...")
d= int(input('Enter private key of Bob d = ')) 
# Send n
n= int(input('Enter n  = '))
client.send(str.encode(str(n)))
print("Public key n sent ...")
time.sleep(0.2)
# Public key of Bob
publicKeyBob =[e,n]
# Private key of Bob
privateKeyBob= [d,n]
# Receive size of random number to generate prime   
m1 = client.recv(BUFSIZE)
m1 = m1.decode()
m1 = int(m1)
print("Received size of prime number ... ")
time.sleep(0.5)
# Receive C = C-X
c = client.recv(BUFSIZE)
c = c.decode()
c = int(c)
print("Received c from Alice ...")
# Yao's problem
rangeN = r2+r1-1
n = [0]*(rangeN+1)
for i in range(1, len(n)):
	n[i] = encryptDecrypt(c+i,privateKeyBob)
m = n[1:]
# Choose a large prime p (<M1); Bob can know the size of M1
primes = [i for i in range(2,2**(m1-1)) if isPrime(i)]
#time.sleep(0.5)
# Compute Z i = M2 i mod p, 1<=i<100
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
z.insert(len(z),prime)
# Send sequence
z1 = pickle.dumps(z)
client.send(z1)
print("Sequence sent to Alice ...")
#print(response.decode())
# Send offline message
print("Received result : \n")
result = client.recv(BUFSIZE)
print(result.decode())
client.close()
