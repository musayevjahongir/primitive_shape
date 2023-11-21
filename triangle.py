from polygon import Polygon
from math import sqrt
class Triangle(Polygon):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
    def getArea(self):
        p=(self.a+self.b+self.c)/2
        return sqrt(p*(p-self.a)*(p-self.b)*(p-self.c))
    def getPerimeter(self):
        return self.a+self.b+self.c
u1=Triangle(3, 4, 5)
print(u1.getArea(), u1.getPerimeter())