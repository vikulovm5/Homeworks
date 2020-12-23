salary = open(file='salary.txt', encoding="UTF-8", mode='rt')

sal = 0
counter = 0
for line in salary:
    counter += 1
    i = tuple(line.split(' '))
    sal += int(i[1])
    if int(i[1]) < 20000:
        print(i[0])

print(f"Средняя зарплата: {sal/counter}")

salary.close()
