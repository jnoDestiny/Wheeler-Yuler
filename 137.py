import math
import array as arr

i = 1
farr = []
farr.append(0)
farr.append(1)

for i in range (2,60):
    farr.append(farr[i-1] + farr[i-2])

nugget = 2

for i in range (2,16):
    nugget = nugget + farr[4*i-1]
    print(i, nugget)