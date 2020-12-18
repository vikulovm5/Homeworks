from functools import reduce

a = 1
b = [el for el in range(99, 1001) if el % 2 == 0]
for el in b:
    a = el * a
print(a)