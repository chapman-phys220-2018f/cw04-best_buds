#!/usr/bin/env python3

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

if __name__ == "__main__":
    import sys
    main(sys.argv)
