import math
class GeometricForms:

    def __init__(self, x, y): 
        
        self.x = x
        self.y = y
        self.pi = math.pi  
    
    def translate(self, dx, dy):
        self.x += dx
        self.y += dy
    
    def __repr__(self):
        return f'Geometricforms(x={self.x}, y={self.y})'
    
    def __str__(self):
        return f'Geometricforms(x={self.x}, y={self.y})'
    
    @property
    def area(self):
        return self._area
    
    @area.setter
    def area(self, area):
        area = self.length * self.width
        
        self._area = area

          
    @property
    def perimeter(self):
        return self.perimeter
          
    @perimeter.setter
    def perimeter(self, perimeter):
        perimeter = 2 * (self.length + self.width)
        self._perimeter = perimeter
    
    def __eq__(self, other):
        return type(self) == type(other)

    def __lt__(self, other):
        return self.area < other.area, self.perimeter < other.perimeter
    
    def __le__(self, other): 
        return self.area <= other.area, self.perimeter <= other.perimeter 
    
    def __gt__(self, other):
        return self.area > other.area, self.perimeter > other.perimeter 
    
    def __ge__(self, other):
        return self.area >= other.area, self.perimeter >= other.perimeter
    
    
    def is_inside(self, point_x, point_y):
        pass
