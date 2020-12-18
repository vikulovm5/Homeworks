from itertools import count, cycle

a = int(input('Введите число: '))
for i in count(a):
    print(i)
    if i > 9:
        break

b = [1,2,3]
count = 0
for i in cycle(b):
    if count > 10:
        break
    print(i)
    count += 1
