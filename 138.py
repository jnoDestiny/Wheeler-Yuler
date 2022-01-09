from math import sqrt, log, ceil

# Project Euler 318
def N(p, q):
    return ceil(2011 * log(10) / (2 * (log(sqrt(q) + sqrt(p)) - log(q - p))))


sum = 0
for p in range(1, 2011 // 2 + 1):
    q = p + 1
    while (q + p <= 2011) and ((q - p)**2 - 2 * (q + p) + 1) < 0:
        sum += N(p, q)
        q += 1

print(sum)
