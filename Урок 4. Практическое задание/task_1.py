"""
Задание 1.

Приведен код, который позволяет сохранить в
массиве индексы четных элементов другого массива

Сделайте замеры времени выполнения кода с помощью модуля timeit

Оптимизируйте, чтобы снизить время выполнения
Проведите повторные замеры.

Добавьте аналитику: что вы сделали и почему!!!
Без аналитики задание не принимается
"""
import timeit


def func_1(nums):
    new_arr = []
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            new_arr.append(i)
    return new_arr


num = [el for el in range(10000)]

print(timeit.timeit('func_1(num)', globals=globals(), number=1000))

# 1.4024693999999998

print(timeit.timeit('func_1(num)', globals=globals(), number=10000))

# 11.4458393


def func_1_1(nums):
    return [i for i, el in enumerate(nums) if el % 2 == 0]


print(timeit.timeit('func_1_1(num)', globals=globals(), number=1000))

# 0.9334314999999993

print(timeit.timeit('func_1_1(num)', globals=globals(), number=10000))

# 9.4494401

""" преобразование кода в составители списков ускорило работу кода на ~15%"""
