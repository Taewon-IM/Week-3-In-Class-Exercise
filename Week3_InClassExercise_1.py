from abc import ABC, abstractmethod
import math

class Shape3D(ABC):
    @abstractmethod
    def volume(self):
        pass
    
    @abstractmethod
    def surface_area(self):
        pass
    
    def describe(self):
        params = ", ".join(f"{key}: {value}" for key, value in vars(self).items())
        print(f"{self.__class__.__name__} with {params}")


class Cube(Shape3D):
    def __init__(self, side):
        if side <= 0:
            raise ValueError("Side must be a positive number.")
        self.side = side

    def volume(self):
        return self.side ** 3

    def surface_area(self):
        return 6 * (self.side ** 2)
    

class Sphere(Shape3D):
    def __init__(self, radius):
        if radius <= 0:
            raise ValueError("Radius must be a positive number.")
        self.radius = radius
        
    def volume(self):
        return (4/3) * math.pi * (self.radius ** 3)

    def surface_area(self):
        return 4 * math.pi * (self.radius ** 2)


class Cylinder(Shape3D):
    def __init__(self, radius, height):
        if radius <= 0 or height <= 0:
            raise ValueError("Radius and height must be positive numbers.")
        self.radius = radius
        self.height = height
        
    def volume(self):
        return math.pi * (self.radius ** 2) * self.height

    def surface_area(self):
        base = 2 * math.pi * (self.radius ** 2)
        side = 2 * math.pi * self.radius * self.height
        return base + side


shapes = [
    Cube(side=2),
    Sphere(radius=3),
    Cylinder(radius=2, height=5)
]

for s in shapes:
    s.describe()
    print(f"Volume: {s.volume():.2f}")
    print(f"Surface area: {s.surface_area():.2f}")
    print("---")
