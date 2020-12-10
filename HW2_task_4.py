ls = (input("Введите строку: "))
arr = ls.split()
for i, el in enumerate(arr):
    print(f"{i+1, el[:10]}")
