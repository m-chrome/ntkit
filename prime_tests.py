from math import gcd
from random import randint
from elementary import jacobi_symbol


def solovay_primality_test(n, k=10):
    for i in range(k):
        a = randint(1, n-1)
        if gcd(a, n) > 1:
            return False
        pows = pow(a, ((n-1)//2), n)
        jac = jacobi_symbol(a, n) % n
        if pows != jac:
            return False
    return True


def factorize_by_two(number):
    n = 0
    q = number
    while q % 2 == 0:
        q //= 2
        n += 1
    return n, int(q)


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
