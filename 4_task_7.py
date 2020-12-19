from math import factorial


def fact(n):
    for i in range(1, n + 1):
        yield factorial(i)


if __name__ == '__main__':
    try:
        value = int(input('Введите число: '))
    except ValueError:
        print('Введено не число')

    for el in fact(value):
        print(el)
