"""
Задача 3.
В соответствии с документацией Python,
deque – это обобщение стеков и очередей.
Вот основное правило: если вам нужно что-то быстро дописать или вытащить, используйте deque.
Если вам нужен быстрый случайный доступ, используйте list.

Задача: 
1) создайте простой список (list) и очередь (deque). Сделайте замеры и оцените что заполняется быстрее.
2) Выполните различные операции с каждым из объектов. Сделайте замеры и оцените, где и какие операции быстрее.

Не забудьте, что сравнивать, например, можно операцию appendleft дека и insert списка и т.д.
"""

from timeit import timeit
from collections import deque

test_deque = deque()
test_list = []


def fill_list(elem_count):
    for _ in range(elem_count):
        test_list.append(None)


def right_fill_deque(elem_count):
    for _ in range(elem_count):
        test_deque.append(None)


print(f'{timeit("fill_list(100000)", globals=globals(), number=1)}')
#0.01670949999999971
print(f'{timeit("right_fill_deque(100000)", globals=globals(), number=1)}')
#0.016233900000000023


def insert_into_list(elem_count):
    for _ in range(elem_count):
        test_list.insert(0, None)


def left_fill_deque(elem_count):
    for _ in range(elem_count):
        test_deque.appendleft(None)


print(f'{timeit("insert_into_list(100000)", globals=globals(), number=1)}')
#8.9368538
print(f'{timeit("left_fill_deque(100000)", globals=globals(), number=1)}')
#0.011744199999998983


def insert_into_list_mid():
    i = len(test_list) // 2
    test_list.insert(i, None)


def insert_into_deque():
    i = len(test_deque) // 2
    test_deque.insert(i, None)


print(f'{timeit("insert_into_list_mid()", globals=globals(), number=1000)}')
#0.08003099999999996
print(f'{timeit("insert_into_deque()", globals=globals(), number=1000)}')
#0.2139042



print(f'{timeit("test_list.copy()", globals=globals(), number=1)}')
#0.0013941000000006198
print(f'{timeit("test_deque.copy()", globals=globals(), number=1)}')
#0.0028869000000000256


def get_list_elem():
    for i in range(len(test_list)):
        test_list[i]


def get_deque_elem():
    for i in range(len(test_deque)):
        test_deque[i]


print(f'{timeit("get_list_elem()", globals=globals(), number=1)}')
#0.0179904999999998
print(f'{timeit("get_deque_elem()", globals=globals(), number=1)}')
#0.7390713000000009

"""
з замеров можно сделать вывод, что в большинстве операций по времени выигрывает список, если дело не касается операций с началом списка.
"""