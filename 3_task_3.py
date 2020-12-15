def my_func(a, b, c):
    my_lst = [a,b,c]
    for el in my_lst:
        if el > min(my_lst) and el < max(my_lst):
            return el + max(my_lst)


print(f"Сумма наибольших чисел: {my_func(3, 4, 9)}")