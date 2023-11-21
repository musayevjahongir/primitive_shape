from polygon import Polygon

class Rectangle(Polygon):
    def __init__(self, height: int, width: int) -> None:
        super().__init__(height, width) 
t1=Rectangle(12, 8)
print(t1.getArea())