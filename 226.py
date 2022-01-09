import math
from scipy.optimize import brentq
import scipy.integrate as integrate


def s(x):
    return min(x - math.floor(x), math.ceil(x) - x)


def blanc(x):
    global iterations
    sum = 0
    for i in range(0, iterations+1):
        sum += s(x*2**i) / 2**i

    return sum


def circularArc(x):
    return 0.5 - 0.5*math.sqrt(2*x-4*x**2)


def f(x):
    return blanc(x) - circularArc(x)


def sInt(x):
    floorx = math.floor(x)
    fracx = x - floorx
    if 0 <= fracx <= 0.5:
        return floorx / 4 + 0.5 * fracx ** 2
    else:
        return floorx / 4 + 0.25 - 0.5 * (1 - fracx) ** 2


def bInt(x):
    global iterations
    sum = 0
    for i in range(0, iterations+1):
        sum += 1/(4**i) * sInt(x*2**i)

    return sum

iterations = 26
r = brentq(f, 0.0789, 0.07891)
print(0.25 - bInt(r) - integrate.quad(circularArc, r, 0.5)[0])
