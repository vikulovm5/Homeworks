profit = int(input("Введите сумму прибыли: "))
costs = int(input("Введите сумму издержек: "))
proceeds = profit - costs

if profit > costs:
    print("Фирма работает в плюс")
    rent = str(proceeds / profit)
    print("Рентабельность равна: " + rent)
    people = int(input("Введите количество работников: "))
    one_proceed = str(profit / people)
    print("Прибыль на одного работника равна: " + one_proceed)
else:
    print("Фирма работает в убыток")
