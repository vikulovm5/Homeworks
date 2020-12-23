with open(file='numbers.txt', encoding="UTF-8", mode='wt') as numbers:
    numbers.write(input('Введите числа: '))

with open(file='numbers.txt', encoding="UTF-8", mode='rt') as numbers:
    summary = 0
    for line in numbers:
        i = tuple(line.split(' '))
        for x in i:
            x = int(x)
            summary += x
    print(f'Сумма чисел равна: {summary}')