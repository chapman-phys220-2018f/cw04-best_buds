#!/usr/bin/env python3


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

if __name__ == "__main__":
    import sys
    main(sys.argv)

