class circle():
    def __init__(self, radius):
        self.radius = radius
    

    def area(self):
        return 3.14 * self.radius ** 2
    
    def __sub__(self, other):
        diff_radius = abs(self.radius - other.radius)
        if diff_radius == 0:
            return Point(0, 0)
        return diff_radius

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

circle_1 = circle(1)
circle_2 = circle(5)
print(circle_1 - circle_2)