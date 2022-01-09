def geometric_series_sum(b, n, m):
    T = 1
    new_base = b % m
    sum = 0
    while n > 0:
        if n & 1 == 1:
            sum = (new_base * sum + T) % m
        T = ((new_base + 1) * T) % m
        new_base = (new_base * new_base) % m
        n //= 2
    return sum


mod = 1000000007
n = 10**6


arr = [0]
for k in range(1, n + 1):
    arr.append(1 - k ** 2)


sum = 0
for k in range(1, n + 1):
    sum = (sum + geometric_series_sum(arr[k], n + 1, mod) - 1) % mod


print(sum)
