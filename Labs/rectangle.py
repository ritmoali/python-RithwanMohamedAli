
from geometricforms import GeometricForms


class Rectangle(GeometricForms):
    def __init__(self, x, y, length, width, area=None):
        super().__init__(x, y)
        self.length = length
        self.width = width
        self.area = area


    def __repr__(self):
        return f'Rectangle(x={self.x}, y={self.y})'
    
    def is_inside(self, point_x, point_y):
        return (
            self.x - self.length/2 <= point_x <= self.x + self.length/2
            and self.y - self.width/2 <= point_y <= self.y + self.width/2  
        )
    def is_square(self):
        return self.length == self.width
