def int_func(text):
   return str.capitalize(text)
#
#
# x = input("Введите слово: ")
#
# print(int_func(x))


y = []
x = list(input("Введите строку: ").split(" "))
for i in x:
    y.append(int_func(i))

print(y)
