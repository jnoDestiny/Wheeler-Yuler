from math import sqrt, log, ceil

# Project Euler 318
def N(p, q):
    return ceil(2011 * log(10) / (2 * (log(sqrt(q) + sqrt(p)) - log(q - p))))


# sum = 0
# for p in range(1, 2011 // 2 + 1):
#     q = p + 1
#     while (q + p <= 2011) and ((q - p)**2 - 2 * (q + p) + 1) < 0:
#         sum += N(p, q)
#         q += 1

# print(sum)


# Project Euler 119

# mySet = set()


# def digitalSum(n):
#     sum = 0
#     while n > 0:
#         sum += n % 10
#         n //= 10
#     return sum


# def checkPlease(n):
#     s = digitalSum(n)
#     if s == 1:
#         return 0
#     return s ** round(log(n, s)) == n


# for a in range(2, 100):
#     for b in range(2, 100):
#         if (checkPlease(a**b)):
#             mySet.add(a**b)


# def shittySort(myList):
#     for i in range(len(myList) - 1):
#         for j in range(i + 1, len(myList)):
#             if (myList[j] < myList[i]):
#                 temp = myList[j]
#                 myList[j] = myList[i]
#                 myList[i] = temp


# myList = list(mySet)
# shittySort(myList)
# for i in range(len(myList)):
#     print(i + 1, " - ", myList[i])


# Project Euler 120


# sum = 0
# for a in range (3, 1001):
#     rmax = 0
#     a2 = a**2
#     for n in range(1, a2, 2):
#         bitch = 2*n*a % a2
#         if (bitch > rmax):
#             rmax = bitch
#     if rmax < 2:
#         rmax = 2
#     sum += rmax

# print(sum)


# Project Euler 100


# xarr = [1]
# yarr = [1]

# def update():
#     n = 2
#     x1 = xarr[0]
#     y1 = yarr[0]
#     xk = xarr[len(xarr) - 1]
#     yk = yarr[len(yarr) - 1]
#     xarr.append(3 * xk + 4 * yk)
#     yarr.append(2 * xk + 3 * yk)

# while xarr[len(xarr) - 1] * (2 * yarr[len(yarr) - 1] - xarr[len(xarr) - 1]) <= 10**12:
#     update()

# print(xarr)
# print(yarr)
# print(yarr[len(yarr) - 1] * (2 * yarr[len(yarr) - 1] - xarr[len(xarr) - 1]))


# Project Euler 282


X = [1, 2, 3]
Y = [1, 1, 2]

arr = [5]
sum = 5
for i in range(1, 14):
    arr.append(3 + 2 * arr[len(arr) - 1])

print(arr)
