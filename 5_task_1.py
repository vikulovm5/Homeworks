my_file = open(file='my_file.txt', encoding="UTF-8", mode='wt')

for i in (input('Введите данные: ').split(' ')):
    my_file.write(f"{i}\n")

my_file.close()
