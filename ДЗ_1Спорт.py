a = int(input("Введите расстояние в первый день: "))
b = int(input("Введите целевой результат: "))
day = 1

while a < b:
    a = a * 1.1
    day = day + 1

print(f"На {day}-й день результат составил более {b}км")