#!py_env/bin/python
# python3

'''
Simple prime generator with a sieve of Eratosthenes

Created on Aug 23, 2016
'''

from math import sqrt

print("Let's generate prime numbers")

print("What is a lower bound? ", end='')
m = int(input('-->'))

print("What is an upper bound? ", end='')
n = int(input('-->'))

sieve = [x for x in range(n+1)]
sieve[0] = -1
sieve[1] = -1
tobechecked = [i for i in range(2, int(sqrt(n))+1)]
primes = []
for i in tobechecked:
    if sieve[i] < 0:
        continue
    #print("checking %d" % i)
    if i >= m:
        primes.append(i)
        print(i)
    
    ki = i
    while ki <= n:
        sieve[ki] = -1
        ki += i
for p in sieve:
    if p >= m:
        primes.append(p)
        print(p)
            
#print(sieve)
#print(primes)  
