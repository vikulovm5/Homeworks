class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        return f'Запуск отрисовки.'

class Pen:
    def __init__(self, title):
        super().__init__()

    def draw(self):
        return f'Запуск отрисовки. Используется ручка.'

class Pencil:
    def __init__(self, title):
        super().__init__()

    def draw(self):
        return f'Запуск отрисовки. Используется карандаш.'

class Handle:
    def __init__(self, title):
        super().__init__()

    def draw(self):
        return f'Запуск отрисовки. Используется маркер.'


a = Pen("ручка")
b = Pencil("карандаш")
d = Handle("маркер")

print(a.draw())
print(b.draw())
print(d.draw())
