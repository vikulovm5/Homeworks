"""
Задача 4.
Поработайте с обычным словарем и OrderedDict.
Выполните операции с каждым их них (заполнение, получение элемента) и сделайте замеры.
Опишите полученные результаты, сделайте выводы.

И есть ли смысл исп-ть OrderedDict в Python 3.6 и более поздних версиях?
"""

from timeit import timeit
from collections import OrderedDict


test_dict = {}
test_ordered_dict = OrderedDict()


def fill_dict(elem_count):
    for i in range(elem_count):
        test_dict[i] = None


def fill_ordered_dict(elem_count):
    for i in range(elem_count):
        test_ordered_dict[i] = None


print(f'{timeit("fill_dict(100000)", globals=globals(), number=100)}')
#1.4209267
print(f'{timeit("fill_ordered_dict(100000)", globals=globals(), number=100)}')
#1.4266081


print(f'{timeit("test_dict.copy()", globals=globals(), number=100)}')
#0.3316673999999997
print(f'{timeit("test_ordered_dict.copy()", globals=globals(), number=100)}')
#1.8632043999999999



def del_from_dict():
    for i in range(len(test_dict)):
        test_dict.popitem()


def del_from_ordered_dict():
    for i in range(len(test_ordered_dict)):
        test_ordered_dict.popitem()


print(f'{timeit("del_from_dict()", globals=globals(), number=100)}')
#0.01184360000000062
print(f'{timeit("del_from_ordered_dict()", globals=globals(), number=100)}')
#0.020835700000000124

"""
Операции с OrderedDict занимают больше времени, чем с обычным словарём.

Так как словари в Python 3.6 по умолчанию упорядоченны, смысла в использовании OrderedDict нет.
"""
