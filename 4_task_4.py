a = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
b = []
for el in a:
    if a.count(el) == 1:
        b.append(el)

print(b)
