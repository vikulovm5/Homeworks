from sys import argv
if len(argv) == 4:
    try:
        print("Введите размер выработки в часах, почасовой оплаты, премии: ")
        my_sal = int(argv[1]) * int(argv[2]) + int(argv[3])
        my_prize = int(input("Введите размер премии: "))
        print(f'Заработная плата составит: {my_sal}')
    except ValueError:
            print("Введенные данные не являются числом")
else:
    print("Неверное количество аргументов. Введите размер выработки в часах, почасовой оплаты, премии: ")