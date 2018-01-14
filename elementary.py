from math import gcd

ERROR_NO_INV_ELEM_MSG = "No inverted element for {0} in rind mod {1}"


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


def find_inverted_element(element, module):
    if module < 2:
        return ERROR_NO_INV_ELEM_MSG.format(element, module)

    if element == 1:
        return 1

    cur_gcd, inverted, _ = extended_euclid_algo(element, module)

    if cur_gcd > 1:
        return ERROR_NO_INV_ELEM_MSG.format(element, module)
    else:
        return inverted if inverted > 0 else module + inverted


def jacobi_symbol(a, m):
    if a == 0 or gcd(a, m) != 1:
        return 0

    x, y, s = a, m, 1

    if a < 0:
        x *= -1
        s = (-1) ** int((m-1) / 2)

    while True:
        c = x % y
        x = c
        t = 0

        if x == 0:
            return 1

        while x % 2 == 0:
            x = int(x / 2)
            t += 1

        if t % 2 == 1:
            s *= (-1) ** int((y ** 2 - 1) / 8)

        if x > 1:
            s *= (-1) ** int((x - 1) * (y - 1) / 4)
            c = x
            x = y
            y = c
        else:
            break
    return s
