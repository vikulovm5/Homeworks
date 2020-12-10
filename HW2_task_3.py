#seasons = {'зима': (1, 2, 12), 'весна': (3, 4, 5), 'лето': (6, 7, 8), 'осень': (9, 10, 11)}

#month = int(input('Введите номер месяца: '))
#for key in seasons.keys():
#    if month in seasons[key]:
#        print(f"Время года - {key}")
#    else:
#        print("Не верно введён номер месяца")

winter = [12,1,2]
spring = [3,4,5]
summer = [6,7,8]
autumn = [9,10,11]

month = int(input('Введите номер месяца: '))
if month in winter:
    print("Время года - зима")
elif month in spring:
    print("Время года - весна")
elif month in summer:
    print("Время года - лето")
elif month in autumn:
    print("Время года - осень")
else:
    print("Не верно введён номер месяца")