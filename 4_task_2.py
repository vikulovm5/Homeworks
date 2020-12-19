import itertools

my_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
new_list = []
a = itertools.cycle(my_list)
cntr = 0
length = len(my_list)
b = next(a)
while cntr < length:
    for el in my_list:
        b = next(a)
        cntr += 1
        if el > b:
            new_list.append(el)

print(new_list)
