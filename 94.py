import math


for i in range(1, 10000000000, 2):
    number = 3*i**2 + 2*i - 1
    root = math.sqrt(number)
    if int(root + 0.5)**2 == number:
        print(i, i, i - 1)

    number = 3 * i ** 2 - 2 * i - 1
    root = math.sqrt(number)
    if int(root + 0.5) ** 2 == number:
        print(i, i, i + 1)

# print(5 +5 +6+17 +17 +16
# +65 +65 +66
# +241 +241 +240
# +901 +901 +902
# +3361 +3361 +3360
# +12545 +12545 +12546
# +46817 +46817 +46816
# +174725 +174725 +174726
# +652081 +652081 +652080
# +2433601 +2433601 +2433602
# +9082321 +9082321 +9082320
# +33895685 +33895685 +33895686
# +126500417 +126500417 +126500416)

# print(5+17+65+241+901+3361+12545+46817+174725+652081+2433601+9082321)