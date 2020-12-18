def div(a, b):
    if b == 0:
        return "Делить на 0 нельзя"
    else:
        c = a / b
        return c


dividend = (int(input("Введите число a: ")))
divider = (int(input("Введите число b: ")))

print(f"Частное: {div(dividend, divider)}")

