new_file = open(file='new_file.txt', encoding="UTF-8", mode='rt')

counter = 0

for line in new_file:
    counter += 1
    my_line = tuple(line.split(' '))
    words = len(my_line)
    print(f"Слов в {counter} строке: {words}")
    if len(my_line) == 0:
        break

print(f"Всего строк: {counter}")


new_file.close()