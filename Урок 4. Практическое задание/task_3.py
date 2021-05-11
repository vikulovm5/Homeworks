"""
Задание 3.

Приведен код, формирующий из введенного числа
обратное по порядку входящих в него
цифр и вывести на экран.

Сделайте профилировку каждого алгоритма через cProfile и через timeit

Обязательно предложите еще свой вариант решения и также запрофилируйте!

Сделайте вывод, какая из четырех реализаций эффективнее и почему!!!

Без аналитики задание считается не принятым
"""
import timeit


def revers_1(enter_num, revers_num=0):
    if enter_num == 0:
        return revers_num
    else:
        num = enter_num % 10
        revers_num = (revers_num + num / 10) * 10
        enter_num //= 10
        return revers_1(enter_num, revers_num)


def revers_2(enter_num, revers_num=0):
    while enter_num != 0:
        num = enter_num % 10
        revers_num = (revers_num + num / 10) * 10
        enter_num //= 10
    return revers_num


def revers_3(enter_num):
    enter_num = str(enter_num)
    revers_num = enter_num[::-1]
    return revers_num


def revers_4(enter_num):
    enter_num_list = list(str(enter_num))
    enter_num_list.reverse()
    return ''.join(enter_num_list)


enter_num = 18556834


print('revers_1:', timeit.timeit('revers_1(enter_num)', globals=globals()))
print('revers_2:', timeit.timeit('revers_2(enter_num)', globals=globals()))
print('revers_3:', timeit.timeit('revers_3(enter_num)', globals=globals()))
print('revers_4:', timeit.timeit('revers_4(enter_num)', globals=globals()))


"""
revers_1: 2.764712
revers_2: 1.8988652999999998
revers_3: 0.4414152999999992
revers_4: 0.7433858999999998

Функция 1 работает дольше остальных из за рекурии. Функция 2 использует цикл. Функция 3 выигрывает за сет обратного набора элементов. Функция 4 работает с встроенными функциями списка и занимает чуть больше времени.
"""