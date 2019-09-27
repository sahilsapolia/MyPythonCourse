import math
class Circle:
    def __init__(self,radius):
        self.radius = radius
    
    def area(self):
        return self.radius*math.pi*2

circle_1 = Circle(2)
print(circle_1.area())