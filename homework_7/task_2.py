import time


class auto():
    def __init__(self, brand, age, mark):
        self.age = age
        self.brand = brand
        self.color = 'green'
        self.mark = mark
        self.weight = 1500


    def move(self):
        print('Move')


    def stop(self):
        print('Stop')


    def birthday(self):
        self.age += 1





class truck(auto):
    def __init__(self, brand, age, mark, weight, max_load):
        super().__init__(brand, age, mark)
        self.max_load = max_load


    def move(self):
        print('attention')
        super().move()


    def load(self,weight):
        time.sleep(1)
        print('load')
        time.sleep(1)

class car(auto):
    def __init__(self, brand, age, mark, max_speed):
        super().__init__(brand, age, mark)
        self.max_speed = max_speed


    def move(self):
        super().move()
        print(f'max speed is {self.max_speed}')


new_truck = truck('Scania', 2, 'idk', 20000, 15000)
new_truck.move()
new_truck.stop()
print(new_truck.brand)
print(new_truck.color)
print(new_truck.age)
new_truck.birthday()
print(new_truck.age)
new_truck.load(20000)

new_car = car('mercedes', 2, 'w222', 280)
new_car.move()
new_car.stop()
new_car.birthday()
print(new_car.brand)
print(new_car.age)
print(new_car.mark)
print(new_car.color)
print(new_car.weight)

