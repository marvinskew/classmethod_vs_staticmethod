import numpy as np

class Circle:
    
    def __init__(self, radius):
        self._radius = radius

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, val):
        if not isinstance(val, (int, float)):
            raise TypeError("Radius must be either a float or integer data type.")
        if val < 0:
            raise ValueError("Radius of a circle cannot be negative")
        self._radius = val

    @radius.deleter
    def radius(self):
        del self._radius

    def __str__(self):
        return f"Circle has radius : {self._radius}"

    def __repr__(self):
        return f"{self.__class__.__name__}(radius={self._radius!r})"

    def area_of_circle(self):
        print("Computing Area of the circle... ")
        return np.pi*self._radius**2

    def circumference_of_circle(self):
        print("Computing Perimeter or circumeference of circle... ")
        return 2*np.pi*self._radius

    def arc_length(self, radians):
        print(f"Computing Arc length subtended by the angle in radians : {radians}")
        return self._radius*radians

    def perimeter_of_circle_sector(self, radians):
        print(f"Computing perimeter of sector subtended by the angle in radians : {radians}")
        return 2*self._radius + self._radius*radians

    def area_of_circle_sector(self, radians):
        print(f"Computing area of sector subtended by the angle in radians : {radians}")
        return 0.5*self._radius*self.arc_length(radians)

    @classmethod
    def from_diameter(cls, diameter):
        print(f"Alternative constructor for cirlce with diameter : {diameter}")
        return cls(diameter/2.0)

    @staticmethod
    def convert_degrees_to_radians(degree):
        radians = degree*(np.pi/180)
        return radians
        

if __name__=='__main__':
    c1 = Circle(25.6)
    c1.radius = 10.56
    print(repr(c1))
    c2= Circle.from_diameter(150.0)
    #print(c2)
    #print(Circle.convert_degrees_to_radians(68)) #1.1868238913561442
    print(repr(c2))
    print(c2.area_of_circle())
    print(c2.circumference_of_circle())
    print(c2.arc_length(1.1868238913561442))
    print(c2.perimeter_of_circle_sector(1.1868238913561442))
    print(c2.area_of_circle_sector(1.1868238913561442))

    
    

        
            

    
