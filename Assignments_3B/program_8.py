from abc import ABC, abstractmethod
import math

class IShape(ABC):
    @abstractmethod
    def CalculateArea(self):
        pass
    @abstractmethod
    def CalculatePerimeter(self):
        pass

class Rectangle(IShape):
    def __init__(self,length ,breadth):
        self.length = length
        self.breadth = breadth

    def CalculateArea(self):
        return self.length * self.breadth

    def CalculatePerimeter(self):
        return 2*(self.length + self.breadth)

class Circle(IShape):
    def __init__(self,radius):
        self.radius = radius
    def CalculateArea(self):
        return math.pi * self.radius * self.radius
    def CalculatePerimeter(self):
        return 2* math.pi * self.radius

def main():
    r = Rectangle(5 ,3)
    print("Rectangle Area:",r.CalculateArea())
    print("Rectangle Perimeter:" ,r.CalculatePerimeter())

    c = Circle(4)
    print("Circle Area:",c.CalculateArea())
    print("Circle Perimeter:" ,c.CalculatePerimeter())

if __name__ == "__main__":
    main()
