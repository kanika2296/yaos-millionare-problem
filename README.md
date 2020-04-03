# Yao's Millionare Problem
Yao's Millionaires' problem is a secure multi-party computation problem which was introduced in 1982 by computer scientist and computational theorist Andrew Yao. The problem discusses two millionaires, Alice and Bob, who are interested in knowing which of them is richer without revealing their actual wealth.

## Problem statement
Yao’s millionaire problem:
1. Alice knows a secret – x, Bob knows a secret – y.
2. Both together wants to know whether x>y, but none wish to reveal x or y.
3. Let, r1<= x,y <= r2, and Bob has public-private keys (PUb and PRb).

## Algorithm
Alice is the intiator :
1. Compute C = E(PUb, M1), M1 a large random number
2. Compute C1 = C – x and sends C1 to Bob
3. Bob computes M[i] = D(PRb,C1+i), for 1<= i <=100
4. Choose a large prime p (<M1); Bob can know the size of M1
5. Compute Z i = M[i] mod p, r1<=i<r2
6. Verify if |Z[i] – Z[j]| >= 2 for all (i,j) and 0 < Z[i] < p-1, for all i, otherwise try another prime and repeat from step-4
7. Send to Alice the sequence: Z[1], Z[2],..., Z[y] , Z[y+1]+1, Z[y+2]+1, ...,Z[r2]+ 1,p
8. Check if x-th number in the sequence is congruent to M1 mod p, if so, x <y, otherwise x>y
9. Alice tells the conclusion to Bob
10. Receive conclusion
# Simple python implementation (python3)
``` 
INPUT
1. r1 : global range 
2. r2 : global range 
3. x : Alice's secret
4. y : Bob's secret
5. e : prime number, public key 
6. d : private key of initiator
7. n : integer
```
```
OUTPUT
y > x  #Bob's secret is greater than Alice's secret
or
x > y  #Alice's secret is greater than Bob's secret
```
# Client-Server implementation (python3)
SERVER : socket with multithreading, supports multiple client connections.
Bob : socket client.
Alice : socket client.

**To make this program run, alice's secret need to be entered first**
```
INPUT
1. x = value of Alice's secret
2. y = value of Bob's secret
3. e = value of Bob's public key
4. n
5. d = value of Bob's private key
```
```
OUTPUT
y > x  #Bob's secret is greater than Alice's secret
or
x > y  #Alice's secret is greater than Bob's secret
```
