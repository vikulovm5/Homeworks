import time


class TrafficLight:
    __color = ['red', 'yellow', 'green']

    def running(self):
        x = 0
        while x < 3:
            print(f'Turning {TrafficLight.__color[x]}')
            if x == 0:
                time.sleep(7)
            elif x == 1:
                time.sleep(2)
            elif x == 2:
                time.sleep(9)
            x += 1


a = TrafficLight()
a.running()
