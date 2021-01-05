class Material:
    def __init__(self, x):
        self.x = x

    @staticmethod
    def full_sq(v, h):
        return v + h


class Coat(Material):
    def __init__(self, x):
        super().__init__(x)

    def coat_sq(self, x):
        h = self.x/6.5 + 0.5
        return h


class Jacket(Material):
    def __init__(self, x):
        super().__init__(x)

    def jacket_sq(self):
        v = 2 * self.x + 0.3
        return v


a = Coat(4)
b = Jacket(3)

print(a.coat_sq)
print(b.jacket_sq)
print(full_sq())