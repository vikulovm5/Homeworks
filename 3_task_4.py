# def my_func(x, y):
#    return x ** y

def my_func(x, y):
    c = 1
    while c < abs(y):
        x = x * x
        c += 1
    return 1/x


a = (int(input("Введите действительное положительное число X:")))
b = (int(input("Введите целое отрицательное число Y:")))

print(f"Результат: {my_func(a, b)}")
