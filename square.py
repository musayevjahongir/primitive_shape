from polygon import Polygon

class Square(Polygon):
    def __init__(self, height: int):
        super().__init__(height, height)
k1=Square(12)
print(k1.getArea())
