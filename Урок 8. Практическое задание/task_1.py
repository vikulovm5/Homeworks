"""
Задание 1.
Реализуйте кодирование строки "по Хаффману".
У вас два пути:
1) тема идет тяжело? тогда вы можете, опираясь на пример с урока, сделать свою!!! версию алгоритма
Разрешается и приветствуется изменение имен переменных, выбор других коллекций, различные изменения
и оптимизации.

2) тема понятна? постарайтесь сделать свою реализацию.
Вы можете реализовать задачу, например, через ООП или предложить иной подход к решению.
"""

import heapq
from collections import Counter
from collections import namedtuple

s = "beep boop beer!"
print(s)


def haffman(s):
    count = Counter(s)
    lst = []
    for el, el2 in count.items():
        r = [el, el2]
        lst.append(r)
    lst = sorted(lst, key=lambda item: item[1])
    if len(lst) != 1:
        while len(lst) > 1:
            wight = lst[0][1] + lst[1][1]
            comb = {0: lst.pop(0)[0],
                    1: lst.pop(0)[0]}
            for i, el in enumerate(lst):
                if wight > el[1]:
                    continue
                else:
                    lst.insert(i, (comb, wight))
                    break
            else:
                lst.append((comb, wight))
    else:
        weight = lst[0][1]
        comb = {0: lst.pop(0)[0], 1: None}
        lst.append((comb, weight))
    return lst[0][0]


code_table = dict()


def haffman_code(tree, path=''):
    if not isinstance(tree, dict):
        code_table[tree] = path
    else:
        haffman_code(tree[0], path=f'{path}0')
        haffman_code(tree[1], path=f'{path}1')


haffman_code(haffman(s))
ss = ''
for i in s:
    print(code_table[i], end=' ')
    ss += code_table[i] + ' '
print()
print(code_table)
print('____Зашифрованная строка____')
print(ss)


def decode_v1(string, code_table):
    string_final = ''
    string = string.split(' ')
    for el in string:
        for el2, el3 in code_table.items():
            if el == el3:
                string_final = string_final + el2
    return string_final


print('___')
print('____Дешифрованная строка____')
print(decode_v1(ss, code_table))
