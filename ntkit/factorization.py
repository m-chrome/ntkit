from math import ceil
from math import floor
from math import sqrt

from .common import factorize_by_two


# Find two dividers of number with Fermat method
def fermat_method(number):
    h = ceil(sqrt(number))
    if pow(h, 2) == number:
        return h, h

    p, q = 0, 0
    x = h
    while True:
        v = pow(x, 2) - number
        if v == pow(floor(sqrt(v)), 2):
            y = floor(sqrt(v))
            p = x + y
            q = x - y
            break
        x += 1
        v += 2 * h + 1

    return p, q


def factorize_recursively(number, method, dividers):
    p, q = method(number)
    if p == number:
        dividers.append(p)
        return
    factorize_recursively(p, method, dividers)
    factorize_recursively(q, method, dividers)
    return dividers


# Common function, returns list of number dividers
def factorize(number, method):
    dividers = []

    # Factorize by 2
    power2, t_number = factorize_by_two(number)
    dividers += [2] * power2

    # Factorize by user-defined method
    dividers = factorize_recursively(t_number, method, dividers)
    return dividers
