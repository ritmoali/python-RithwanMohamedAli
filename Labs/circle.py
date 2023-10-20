from geometricforms import GeometricForms
import math

class Circle(GeometricForms):
    
    def __init__(self, x, y, radius):
        super().__init__(x, y)
        self.radius = radius

    def is_inside(self, point_x, point_y):
        distance = math.sqrt((point_x - self.x)**2 + (point_y - self.y)**2)
        return distance <= self.radius
    
    
    def is_unit_circle(self):
        return (self.radius ==1) and (self.x == 0 and self.y == 0)
                

