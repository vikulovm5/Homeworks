class Road:

    def __init__(self, _length, _width, _thickness):
         self._length = _length
         self._width = _width
         self._thickness = _thickness
         self.__safe_mass = 25

    def mass(self):
        m = self._length * self._width * self.__safe_mass * self._thickness
        return (f'{self._length}(м) * {self._width}(м) * {self.__safe_mass}(кг) * {self._thickness}(см) = {m}(т)')


a = Road(10000, 20, 5)
print(a.mass())
