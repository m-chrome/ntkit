from math import ceil
from math import sqrt


# Find two dividers of number with Fermat method
def fermat_method(number):
    h = ceil(sqrt(number))
    if h ** 2 == number:
        return h, h

    p, q = 0, 0
    x = h
    while True:
        v = x ** 2 - number
        if v == int(sqrt(v)) ** 2:
            y = int(sqrt(v))
            p = x + y
            q = x - y
            break
        x += 1
        v += 2 * h + 1

    return p, q
