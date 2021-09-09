"""
Alexsander Rosante's creation 2021
Reference video: http://y2u.be/7eboFOkRHr4
"""


# Support:

def nat(n):
    return abs(round(n))


def get_primes(n_lst):
    primes = []
    for n in n_lst:
        for i in range(2, n + 1):
            if not n % i:
                if n != i:
                    break
                else:
                    primes.append(n)
    return primes


def tetration(n, loop):
    if loop == 0:
        return n ** n
    return n ** tetration(n, loop - 1)


# Factorials:

def factorial(n):  # n!
    n, fact = nat(n), 1
    for i in range(1, n + 1):
        fact *= i
    return fact


def double_factorial(n):  # n!!
    n, fact, builder = nat(n), 1, range(1, n + 1, 2) if n % 2 else range(2, n + 1, 2)
    for i in builder:
        fact *= i
    return fact


def subfactorial(n):  # !n
    n, fact = nat(n), factorial(nat(n))
    fact *= sum([(-1) ** i / factorial(i) for i in range(0, n + 1)])
    return round(fact)


def primorial(n):  # n#
    n, fact, primes = nat(n), 1, get_primes(list(range(n + 1)))
    for prime in primes:
        fact *= prime
    return fact


def super_factorial_sloane(n):  # sf(n)
    n, fact = nat(n), 1
    for i in range(1, n + 1):
        fact *= factorial(i)
    return fact


def super_factorial_pickover(n):  # n$
    n = nat(n)
    if n > 0:
        return factorial(n) ** tetration(factorial(n), loop=factorial(n) - 2)


def exponential_factorial(n):  # n$
    n = nat(n)
    if n == 0:
        return 1
    else:
        return n ** exponential_factorial(n - 1)


def hyper_factorial(n):  # H(n)
    n, fact = nat(n), 1
    for i in range(1, n + 1):
        fact *= i ** i
    return fact
