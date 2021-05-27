"""
1. Отсортируйте по убыванию методом "пузырька" одномерный целочисленный массив,
заданный случайными числами на промежутке [-100; 100). Выведите на экран
исходный и отсортированный массивы.

Сортировка должна быть реализована в виде функции.

Обязательно доработайте алгоритм (сделайте его умнее).

Идея доработки: если за проход по списку не совершается ни одной сортировки,
то завершение. Обязательно сделайте замеры времени обеих реализаций
и обосновать дала ли оптимизация эффективность

Подсказка: обратите внимание, сортируем не по возрастанию, как в примере,
а по убыванию.

Сделайте выводы!!!
Опишите в чем была ваша доработка и помогла ли вам доработка??
"""

from random import randint
from timeit import default_timer, repeat


def bubble_sort(lst_obj):
    n = 1
    while n < len(lst_obj):
        for i in range(len(lst_obj)-n):
            if lst_obj[i] > lst_obj[i+1]:
                lst_obj[i], lst_obj[i+1] = lst_obj[i+1], lst_obj[i]
        n += 1
    return lst_obj


def bubble_sort_reverse(lst_obj):
    n = len(lst_obj) - 1
    end = 0
    while n >= end:
        is_changed = 0
        for i in range(n, end, -1):
            if lst_obj[i-1] > lst_obj[i]:
                lst_obj[i], lst_obj[i-1] = lst_obj[i-1], lst_obj[i]
                is_changed = 1
        if not is_changed:
            break
        end += 1
    return lst_obj


def comb_sort(lst_obj):
    new_len = len(lst_obj)
    gap = (new_len * 10 // 13) if new_len > 1 else 0
    while gap:
        twist = 0
        for i in range(new_len - gap):
            if lst_obj[i + gap] < lst_obj[i]:
                lst_obj[i], lst_obj[i + gap] = lst_obj[i + gap], lst_obj[i]
                twist = 1
        gap = (gap * 10 // 13) or twist
    return lst_obj


def new_lists():
    orig_lst1 = [randint(-100, 100) for a in range(10)]
    orig_lst2 = [randint(-100, 100) for a in range(100)]
    orig_lst3 = [randint(-100, 100) for a in range(1000)]

    return orig_lst1, orig_lst2, orig_lst3


orig_lst = [randint(-100, 100) for a in range(1000)]
print(orig_lst)
print(bubble_sort(orig_lst[:]))
print(bubble_sort_reverse(orig_lst[:]))
print(comb_sort(orig_lst[:]))

explore_func = ['bubble_sort', 'bubble_sort_reverse', 'comb_sort']

for test_num in range(1, 3):
    print(f'Тестирование {test_num}', end='\n')
    explore_lists = new_lists()

    for function in explore_func:
        print(f'- {function}')

        for explore_lst in explore_lists:
            time_sec = min(repeat(
                f'{function}({explore_lst[:]})', globals=globals(), timer=default_timer, repeat=2, number=1))

            print(f'Время на сортировку списка из {len(explore_lst)} символов: {time_sec} секунд')
        print('')

"""
Тестирование 1
- bubble_sort
Время на сортировку списка из 10 символов: 1.0100000000012876e-05 секунд
Время на сортировку списка из 100 символов: 0.0011338999999999655 секунд
Время на сортировку списка из 1000 символов: 0.10519440000000002 секунд

- bubble_sort_reverse
Время на сортировку списка из 10 символов: 8.699999999972619e-06 секунд
Время на сортировку списка из 100 символов: 0.0006865000000000343 секунд
Время на сортировку списка из 1000 символов: 0.10262379999999993 секунд

- comb_sort
Время на сортировку списка из 10 символов: 6.399999999961992e-06 секунд
Время на сортировку списка из 100 символов: 0.00012080000000014302 секунд
Время на сортировку списка из 1000 символов: 0.0023155999999999732 секунд

Тестирование 2
- bubble_sort
Время на сортировку списка из 10 символов: 1.819999999996824e-05 секунд
Время на сортировку списка из 100 символов: 0.0014225999999999406 секунд
Время на сортировку списка из 1000 символов: 0.09734160000000003 секунд

- bubble_sort_reverse
Время на сортировку списка из 10 символов: 8.800000000031005e-06 секунд
Время на сортировку списка из 100 символов: 0.0006565000000000598 секунд
Время на сортировку списка из 1000 символов: 0.10860349999999985 секунд

- comb_sort
Время на сортировку списка из 10 символов: 6.200000000067263e-06 секунд
Время на сортировку списка из 100 символов: 0.0001162999999999581 секунд
Время на сортировку списка из 1000 символов: 0.0028020999999998075 секунд


После доработки время сортировки крупных списков существенно сократилось, т.к. расстояние между сравниваемыми числами стремится к единице.
Короткие списки быстрее пробегаются простым пузырьковым методом.

"""
