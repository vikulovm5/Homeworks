"""
1.	Написать программу, которая будет складывать, вычитать, умножать или делить
два числа. Числа и знак операции вводятся пользователем. После выполнения
вычисления программа не должна завершаться, а должна запрашивать новые данные
для вычислений. Завершение программы должно выполняться при вводе символа '0'
в качестве знака операции. Если пользователь вводит неверный знак
(не '0', '+', '-', '*', '/'), то программа должна сообщать ему об ошибке и
снова запрашивать знак операции.

Также сообщать пользователю о невозможности деления на ноль,
если он ввел 0 в качестве делителя.

Подсказка:
Вариант исполнения:
- условие рекурсивного вызова - введена операция +, -, *, / - ШАГ РЕКУРСИИ
- условие завершения рекурсии - введена операция 0 - БАЗОВЫЙ СЛУЧАЙ

Пример:
Введите операцию (+, -, *, / или 0 для выхода): +
Введите первое число: 214
Введите второе число: 234
Ваш результат 448
Введите операцию (+, -, *, / или 0 для выхода): -
Введите первое число: вп
Вы вместо трехзначного числа ввели строку (((. Исправьтесь
Введите операцию (+, -, *, / или 0 для выхода):

Решите через рекурсию. Решение через цикл не принимается.
Для оценки Отлично в этом блоке необходимо выполнить 5 заданий из 7
"""

def calc():
    operator = input('Выберите операцию ( +, -, *, / ) Для выхода из программы нажмите 0 ')
    if operator == '0':
        return 'Выход'
    else:
        if operator in '+-*/':
            try:
                a = int(input('Введите число А'))
                b = int(input('Введите число B'))

                if operator == '+':
                    print(f'Ваш результат равен {a + b}')
                    return calc()

                elif operator == '-':
                    print(f'Ваш результат равен {a - b}')
                    return calc()

                elif operator == '*':
                    print(f'Ваш результат равен {a * b}')
                    return calc()

                elif operator == '/':
                    if operator != 0:
                        print(f'Ваш результат равен {a / b}')
                    else:
                        print('Деление на 0 невозможно')
                    return calc()

            except ValueError:
                print('Введено не число')
                return calc()

        else:
            print('Символ выбран некорректно. Повторите попытку')
            return calc()


