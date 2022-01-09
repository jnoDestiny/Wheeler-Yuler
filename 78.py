def partition(n):
    sum = 0
    if n < 0:
        return 1
    if n == 0:
        return 1

    i = 1
    while n - pentagonal1[i] >= 0:
        if memo[n - pentagonal1[i]] == 0:
            memo[n - pentagonal1[i]] = partition(n - pentagonal1[i])
        sum += memo[n - pentagonal1[i]] * (-1)**(i + 1)
        i += 1

    i = 1
    while n - pentagonal2[i] >= 0:
        if memo[n - pentagonal2[i]] == 0:
            memo[n - pentagonal2[i]] = partition(n - pentagonal2[i])
        sum += memo[n - pentagonal2[i]] * (-1)**(i + 1)
        i += 1

    return sum


m = 950
k = 100
memo = [0]*k*m
pentagonal1 = [0]
pentagonal2 = [0]

for i in range(1, m):
    pentagonal1.append((3*i**2 - i)//2)
    pentagonal2.append((3*i**2 + i)//2)


for i in range(1, k + 1):
    partition(i * m)
for i in range(0, len(memo)):
    if memo[i] % 1000000 == 0:
        print(i)