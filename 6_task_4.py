class Car:
    def __init__(self, speed, color, name):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = False

    def go(self):
        return f'{self.name} is moving'

    def stop(self):
        return f'{self.name} stopped'

    def turn_right(self):
        return f'{self.name} turned right'

    def turn_left(self):
        return f'{self.name} turned left'

    def show_speed(self):
        return f'Speed of {self.name} is: {self.speed}'

    def police_check(self):
        if self.is_police:
            return f'{self.name} is a police car'
        else:
            return f'{self.name} is not a police car'


class TownCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name)

    def show_speed(self):
        if self.speed > 60:
            return f'Speed of {self.name} is: {self.speed}. It is over speed limit. Please slow down.'
        else:
            return f'Speed of {self.name} is: {self.speed}'


class SportCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name)


class WorkCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name)

    def show_speed(self):
        if self.speed > 40:
            return f'Speed of {self.name} is: {self.speed}. It is over speed limit. Please slow down.'
        else:
            return f'Speed of {self.name} is: {self.speed}'


class PoliceCar(Car):
    def __init__(self,  speed, color, name):
        super().__init__(speed, color, name)
        self.is_police = True


vw = TownCar(55, 'red', 'Volkswagen')
bmw = SportCar(130, 'black', 'BMW')
ford = TownCar(70, 'white', 'Ford')
suzuki = WorkCar(40, 'blue', 'Suzuki')
renault = PoliceCar(80, 'silver', 'Renault')

print(vw.go())
print(vw.turn_left())
print(vw.show_speed())
print(bmw.show_speed())
print(bmw.police_check())
print(ford.show_speed())
print(ford.stop())
print(renault.turn_right())
print(renault.police_check())
