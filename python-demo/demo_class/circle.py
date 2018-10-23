class Circle():

    #class object attribute
    pi = 3.14

    # def __init__(self,radius=1):
    #     super(Circle, self).__init__()
    #     self.radius = radius

    def __init__(self,radius=1):

        self.radius = radius
        self.area = radius*radius*Circle.pi #or self.pi

    def get_circumference(self):
        return self.radius * self.pi * 2

my_cir = Circle()
print(my_cir.pi)
print(my_cir.radius)
print(my_cir.get_circumference())
print('Circle area is',my_cir.area)

import sys
print(sys.executable)
print(sys.version)
print(sys.version_info)

my_circle = Circle(30)
print('Circumference is',my_circle.get_circumference())
print('Circle area is',my_circle.area)
