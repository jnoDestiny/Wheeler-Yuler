# Project Euler 100


xarr = [1]
yarr = [1]

def update():
    n = 2
    x1 = xarr[0]
    y1 = yarr[0]
    xk = xarr[len(xarr) - 1]
    yk = yarr[len(yarr) - 1]
    xarr.append(3 * xk + 4 * yk)
    yarr.append(2 * xk + 3 * yk)

while xarr[len(xarr) - 1] * (2 * yarr[len(yarr) - 1] - xarr[len(xarr) - 1]) <= 10**12:
    update()

print(xarr)
print(yarr)
print(yarr[len(yarr) - 1] * (2 * yarr[len(yarr) - 1] - xarr[len(xarr) - 1]))
