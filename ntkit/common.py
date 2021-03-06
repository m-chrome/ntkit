from math import gcd


# Find power of 2 in number
def factorize_by_two(number):
    n = number
    power = 0
    while n % 2 == 0:
        power += 1
        n //= 2
    return power, n


def extended_euclid_algo(a, n):
    if n == 0:
        return a, 1, 0

    x1, x2, y1, y2 = 0, 1, 1, 0

    while n > 0:
        q = int(a / n)
        r = a - q * n
        x = x2 - q * x1
        y = y2 - q * y1
        a = n
        n = r
        x2 = x1
        x1 = x
        y2 = y1
        y1 = y

    return a, x2, y2


def find_inverted_element(element, r_module):
    if r_module < 2:
        return None

    if element == 1:
        return 1

    cur_gcd, inverted, _ = extended_euclid_algo(element, r_module)

    if cur_gcd > 1:
        return None
    else:
        return inverted if inverted > 0 else r_module + inverted


def jacobi_symbol(a, m):
    if a == 0 or gcd(a, m) != 1:
        return 0

    x, y, s = a, m, 1

    if a < 0:
        x *= -1
        s = pow(-1, (m-1) // 2)

    while True:
        c = x % y
        x = c
        t = 0

        if x == 0:
            return 1

        while x % 2 == 0:
            x = x // 2
            t += 1

        if t % 2 == 1:
            s *= pow(-1, (pow(y, 2) - 1) // 8)

        if x > 1:
            s *= pow(-1, ((x - 1) * (y - 1)) // 4)
            c = x
            x = y
            y = c
        else:
            break

    return s
