#!/usr/bin/env python3

<<<<<<< HEAD
"""
Frank Entriken
2298368
entriken@chapman.edu
Scientific Computing 220
Classwork 4
"""

def eratosthenes(n):
    """Create a list of prime numbers up to user input 'n'
    """
    prime_list = []
    for number in range(2, n):
        prime = True
        for i in range(2, number):
            if ((number%i) == 0):
                prime = False
        if prime:
            prime_list.append(number)

    return prime_list

def gen_eratosthenes():
    """Generator that continues to yield prime numbers until stopped
    """
    while True:
        prime_list = []
        for number in range(2, 1000000):
            prime = True
            for i in range(2, number):
                if ((number%i) == 0):
                    prime = False
            if prime:
                yield number

def main(argv):
    """Runs eratosthenes with argument set to user input
    """
    print(primes.eratosthenes(int(argv[1])))
=======

###
# Name: Amelia Roseto
# Student ID: 2289652
# Email: roseto@chapman.edu
# Course: PHYS220/MATH220/CPSC220 Fall 2018
# Assignment: CW 4
###

import math

#function
def eratosthenes(n):

    sieve = [True] * n
    sieve[0] = False
    sieve[1] = False

    for i in range(2, int(math.sqrt(n)) +1):
        marker = i * 2
        while marker < n:
            sieve[marker] = False
            marker += i

    primelist = []
    for i in range(n):
        if sieve[i] == True:
            primelist.append(i)

    return primelist

def gen_eratosthenes():

    prime_list = list(range(2, 10000))
    prime_list = [i for i in prime_list if ((i % 2 != 0) or (i == 2))]
    x = -1
    n = 0
    while True:
        x = x + 1
        n = prime_list[x]
        yield n
        for a in prime_list:
            if (a != n and a % n == 0):
                prime_list.remove(a)

def main (argv):
    n = int(argv[1])
    print (eratosthenes(n))
>>>>>>> 0f1e2992ebe1946bff36fbf5c9621066f98cbb00

if __name__ == "__main__":
    import sys
    main(sys.argv)
<<<<<<< HEAD
=======

>>>>>>> 0f1e2992ebe1946bff36fbf5c9621066f98cbb00
