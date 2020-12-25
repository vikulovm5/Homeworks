x = 0
y = 0
z = 0
n = 0
a = 0
lessons = open(file='lessons.txt', encoding="UTF-8", mode='rt')
for line in lessons:
    u = list(line.split(' '))
    for i in u:
        i = str(i)
        i = i.split('(')
        for j in i:
            try:
                n += (int(j))
            except ValueError:
                continue
    if a == 0:
        x = n
    elif a == 1:
        y = n
    else:
        z = n
    n = 0
    a += 1
my_dict = dict(Информатика=x, Физика=y, Физкультура=z)
print(my_dict)
lessons.close()
