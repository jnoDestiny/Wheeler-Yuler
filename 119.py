# Project Euler 119

mySet = set()


def digitalSum(n):
    sum = 0
    while n > 0:
        sum += n % 10
        n //= 10
    return sum


def checkPlease(n):
    s = digitalSum(n)
    if s == 1:
        return 0
    return s ** round(log(n, s)) == n


for a in range(2, 100):
    for b in range(2, 100):
        if (checkPlease(a**b)):
            mySet.add(a**b)


def shittySort(myList):
    for i in range(len(myList) - 1):
        for j in range(i + 1, len(myList)):
            if (myList[j] < myList[i]):
                temp = myList[j]
                myList[j] = myList[i]
                myList[i] = temp


myList = list(mySet)
shittySort(myList)
for i in range(len(myList)):
    print(i + 1, " - ", myList[i])
