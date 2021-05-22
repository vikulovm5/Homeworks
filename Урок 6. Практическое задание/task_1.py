"""
Задание 1.

Выполните профилирование памяти в скриптах
Проанализировать результат и определить программы с
наиболее эффективным использованием памяти.

Примечание: Для анализа возьмите любые 3-5 ваших РАЗНЫХ скриптов!
(хотя бы 3 разных для получения оценки отл).
На каждый скрипт вы должны сделать как минимум по две реализации.

Можно взять только домашние задания с курса Основ
или с текущего курса Алгоритмов

Результаты профилирования добавьте в виде комментариев к коду.
Обязательно сделайте аналитику (что с памятью в ваших скриптах, в чем ваша оптимизация и т.д.)

ВНИМАНИЕ: ЗАДАНИЯ, В КОТОРЫХ БУДУТ ГОЛЫЕ ЦИФРЫ ЗАМЕРОВ (БЕЗ АНАЛИТИКИ)
БУДУТ ПРИНИМАТЬСЯ С ОЦЕНКОЙ УДОВЛЕТВОРИТЕЛЬНО

Попытайтесь дополнительно свой декоратор используя ф-цию memory_usage из memory_profiler
С одновременным замером времени (timeit.default_timer())!
"""

from memory_profiler import memory_usage
from timeit import default_timer


def memory_time_profiler(func):
    def data(*args, **kwargs):
        mem_start = memory_usage()
        time_start = default_timer()
        result = func(args[0])
        time_stop = default_timer()
        mem_stop = memory_usage()
        time_fin = time_stop - time_start
        mem_fin = mem_stop[0] - mem_start[0]

        print(f'Нагрузка на память: {mem_fin} , время выполнения: {time_fin}')
        return result

    return data


@memory_time_profiler
def func_1(nums):
    new_arr = []
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            new_arr.append(i)
    return new_arr


@memory_time_profiler
def func_2(nums):
    return [x for x in nums if x % 2 == 0]


func_1(range(100000))
print("_________________________")
func_2(range(100000))
print("~~~~~~~~~~")
"""
Нагрузка на память: 2.30078125 , время выполнения: 0.03182290000000032
_________________________
Нагрузка на память: 2.22265625 , время выполнения: 0.009608800000000084
~~~~~~~~~~
Функции получения четных элементов массива. Используется памяти примерно одинаково, но у LC чуть меньше.
Время выполнения LC в разы меньше, т.к. в func_1 используется еще и .append.
"""


@memory_time_profiler
def profile_recurs(num, even=0, odd=0):
    def odd_even_num(num, even=0, odd=0):
        if num > 0:
            if num % 2 == 0:
                even += 1
            else:
                odd += 1
            num = num // 10
            return odd_even_num(num, even, odd)
        else:
            return print(f"Четные цифры: {even}, нечетные: {odd}")


@memory_time_profiler
def odd_even_num_2(num, even=0, odd=0):
    while num > 0:
        if num % 2 == 0:
            even += 1
        else:
            odd += 1
        num = num//10


my_num = 616486484334848789456123166786646546465848848646546
profile_recurs(my_num)
print("_________________________")
odd_even_num_2(my_num)
print("~~~~~~~~~~")

"""
Нагрузка на память: 0.0 , время выполнения: 6.700000000137152e-06
_________________________
Нагрузка на память: 0.0 , время выполнения: 2.6699999999379997e-05
~~~~~~~~~~
Рекурсия создает стек, заполняющийся каждый раз, до достижения базового случая. Поэтому время выполнения возрастает. 
Существенных различий в нагрузке на память нет.
"""


@memory_time_profiler
def app_list(lst):
    new_lst = []
    for item in lst:
        new_lst.append(int(item))
    return new_lst


@memory_time_profiler
def mapped_list(lst):
    new_lst = list(map(int, lst))
    return new_lst


my_list = (i for i in range(100000000))
app_list(my_list)
print("_________________________")
mapped_list(my_list)
print("~~~~~~~~~~")

"""
Нагрузка на память: 3864.046875 , время выполнения: 31.5118652
_________________________
Нагрузка на память: 0.0 , время выполнения: 1.3099999996768474e-05
~~~~~~~~~~
Функции преобразования строки в число. Встроенная ф-ция map задействует ощутимо меньше памяти (хватает выделенной, дополнительная не задействуется),
и время выполнения гораздо меньше.
"""
