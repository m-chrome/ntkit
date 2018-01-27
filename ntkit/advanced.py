from . import factorization
from . import primality_tests


def full_factorize(number, fact_method=factorization.fermat_method,
                   primality_method=primality_tests.miller_rabin_primality_test):
    to_verify = [number]
    factorize_list = []
    while to_verify:
        candidate = to_verify.pop()
        if primality_method(candidate):
            factorize_list.append(candidate)
        else:
            if candidate % 2 == 0:
                p, q = 2, candidate // 2
            else:
                p, q = fact_method(candidate)
            to_verify.append(p)
            to_verify.append(q)
    primes = set(factorize_list)
    vision = []
    for prime in primes:
        vision.append((prime, factorize_list.count(prime)))
    return tuple(sorted(vision))
