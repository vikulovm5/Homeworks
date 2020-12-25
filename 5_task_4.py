with open(file='counts.txt', encoding="UTF-8", mode='rt') as counts:
    with open(file='new_counts.txt', encoding="UTF-8", mode='at') as new_counts:
        my_list = ('Один', 'Два', 'Три', 'Четыре')
        cnt = 0
        for line in counts:
            i = list(line.split(' '))
            i.pop(0)
            i.insert(0, my_list[cnt])
            cnt += 1
            new_counts.write(str(' '.join(i)))
