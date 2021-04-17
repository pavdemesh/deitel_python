"""
Sieve of Eratosthenes
For the first 100_000_000 numbers
"""

import math


primes = [True] * 100_000_000

for i in range(2, int(100_000_000 ** 0.5) + 1):
    if primes[i]:
        #print(f"{i} is a prime number")
        primes[i+i::i] = [False] * len(primes[i+i::i])
        #non_prime = list(range(i+i, 1000, i))
        #print("the following are non primes: ")
        #print(*non_prime)

#Display the primes for n from 1 to 1_000     
for i, item in enumerate(primes[:1000]):
    if i <= 1:
        continue
    if item:
        print(f"{i:>3}", end=" | ")