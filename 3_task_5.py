i = []
cntr = 0

while True:
    i = input("Введите числа: ").split(" ")
    try:
        for el in i:
            el = int(el)
            cntr += el
        print(f"{cntr}")
        i = []
    except ValueError:
        print('end')
        break
print(cntr)






