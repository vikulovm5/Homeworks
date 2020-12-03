number = int(input("Введите целое положительное число: "))

arr = []

while number > 1:
    variant = number % 10
    arr.append(variant)
    number = number // 10

print(max(arr))
