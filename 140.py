import math

gArray = []
gArray.append(1)
gArray.append(4)

for i in range (2,100):
    gArray.append(gArray[i-1] + gArray[i-2])
    print(gArray[i])

fArray = []
fArray.append(0)
fArray.append(1)

for i in range (2,200):
    fArray.append(fArray[i-1] + fArray[i-2])
    print(fArray[i])

# i = 1
# counter = 1
# while (1):
#     number = 5*i**2+14*i+1
#     root = math.sqrt(number)
#     if int(root + 0.5)**2 == number:
#         print(counter, i)
#         counter += 1
#     i += 1

sum = 0
nugget = 0
for i in range (1,31):
    if i%2 == 0:
        nugget += fArray[2*i]
    else:
        nugget += fArray[2*i-2] + fArray[2*i+1]
    sum += nugget
    print(i, nugget)

print(sum)