import socket
import pickle
import random
import time
BUFSIZE = 1024

''' Function: RSA encryption & Decryption'''
def encryptDecrypt(message,key):
	c = pow(message,key[0])%key[1]	
	return c

# create an ipv4 (AF_INET) socket object using the tcp protocol (SOCK_STREAM)
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# connect the client
# client.connect((target, port))
client.connect(('127.0.0.1', 1233))
response = client.recv(BUFSIZE)
print(response.decode())
client.send(str.encode("Alice"))
response = client.recv(BUFSIZE)
client.send(str.encode("ONLINE#"))

# Input global range 
r1 =1
r2 =10
# Input value for Alice's secret
x = int(input('Enter value of Alice secret x (within 1 <=x<= 20) : ')) 
e = client.recv(BUFSIZE)
e = e.decode()
# Receive public key
print("Value of e received ... ")
time.sleep(0.2)
n = client.recv(BUFSIZE)
n = n.decode()
print("Value of n received ...")
e = int(e)
n = int(n)
publicKeyBob = [e,n]
print("Received Public Key : ",publicKeyBob)

# Generate and send length of random number M1
N = n.bit_length()
m1 = random.getrandbits(N)
while m1 >= n:
	m1 = random.getrandbits(N)
N =m1.bit_length()
s = str(N)
client.send(str.encode(s))
print("size of random number shared ...")


# Alice encrypts mi using publicKeyBob RSA 
c = encryptDecrypt(m1,publicKeyBob)
#Alice sends C=C-x to Bob
c = str(abs(c-x))
time.sleep(0.5)
client.send(str.encode(c))
print("Value of C sent ...")

seq = pickle.loads(client.recv(BUFSIZE))
#print(seq)

prime = seq[len(seq)-1]
''' Alice recevies sequence z[]
Select z[x] , Check  if z[x] = m1 mod prime'''
print("Result : ")
if(m1%prime == seq[x-1]):
	result = "y > x"
	print(result) # Bob's secret is greater than Alice's secret
else:
	result = "x > y"
	print(result) # Alice's secret is greater than Bob's secret"
client.send(str.encode(result))
client.close()
