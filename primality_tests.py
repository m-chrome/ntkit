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


# dividers = list of unique primes divide number-1
def lucas_primality_test(number, dividers, c=20):
    n = len(dividers)
    k = 0
    used_random = set()
    while c > 0:
        while True:
            a = randint(1, number-1)
            if a in used_random:
                continue
            break
        used_random.add(a)
        if gcd(a, number) != 1:
            return False
        while k < n:
            if pow(a, number-1, number) != 1:
                return False
            if pow(a, (number-1)//dividers[k], number) == 1:
                k = 0
                c -= 1
                break
            k += 1
        return True
    return None
