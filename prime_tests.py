from math import gcd
from random import randint

from common import jacobi_symbol
from common import factorize_by_two


def solovay_primality_test(n, k=10):
    for i in range(k):
        a = randint(1, n-1)
        if gcd(a, n) > 1:
            return False
        if pow(a, ((n-1)//2), n) != jacobi_symbol(a, n) % n:
            return False
    return True


def miller_rabin_primality_test(number, k=10):
    if number == 2 or number == 3:
        return True
    if gcd(6, number) != 1:
        return False
    n, q = factorize_by_two(number - 1)
    while k > 0:
        a = randint(1, number - 1)
        b = pow(a, q, number)
        if b == 1 or b == number - 1:
            k -= 1
        else:
            for i in range(n):
                b = pow(b, 2, number)
                if b == number - 1:
                    k -= 1
                    break
                else:
                    if i == n - 1:
                        return False
                    continue
        if k == 0:
            return True
