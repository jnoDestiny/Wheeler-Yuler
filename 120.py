# Project Euler 120

sum = 0
for a in range (3, 1001):
    rmax = 0
    a2 = a**2
    for n in range(1, a2, 2):
        bitch = 2*n*a % a2
        if (bitch > rmax):
            rmax = bitch
    if rmax < 2:
        rmax = 2
    sum += rmax

print(sum)
