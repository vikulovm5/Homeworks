def data(name, last_name, year, city, mail, phone):
    return name, last_name, year, city, mail, phone


a = input("Введите имя: ")
b = input("Введите фамилию: ")
c = input("Введите год рождения: ")
d = input("Введите город проживания: ")
e = input("Введите email: ")
f = input("Введите номер телефона: ")

print(f"{str(data(a, b, c, d, e, f))}")
