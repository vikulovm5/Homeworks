time = int(input("Введите время в секундах: "))

hours = time // 3600
minutes = (time % 3600) // 60
seconds = (time % 3600) % 60

print(f"{hours:02.0f}:{minutes:02.0f}:{seconds:02.0f}")






