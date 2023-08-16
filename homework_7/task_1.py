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

new_auto = auto('bmw', 2, 'M5')
new_auto.move()
new_auto.stop()
print(new_auto.age)
new_auto.birthday()
print(new_auto.age)




