from math import gcd
from random import randint
from elementary import jacobi_symbol


def solovay_prime_test(n, k=10):
    for i in range(k):
        a = randint(1, n-1)
        if gcd(a, n) > 1:
            return False
        if (a**((n-1)//2)) % n != jacobi_symbol(a, n) % n:
            return False
    return True
