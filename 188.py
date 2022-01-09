def abmodn(a, b, n):
    prod = a
    b = b % n
    for i in range(0, b - 1):
        prod = prod * a % n
    return prod

def tetration(x, y, modulo):
    power = x
    for i in range(0, y - 1):
        power = abmodn(x, power, modulo)
        print(power)
    return power

print(tetration(1777, 1855, 10**8))
