import math

class Shape:
    pass

class Rectangle(Shape):
    def setDim(self, l, b):
        self.l = l
        self.b = b

    def getArea(self):
        return self.l * self.b

    def getPerimeter(self):
        return 2 * (self.l + self.b)

class Triangle(Shape):
        def __init__(self):
            self.a, self.b, self.c = 3, 4, 5

        def getPerimeter(self):
            return self.a + self.b + self.c

        def getArea(self):
            s = self.getPerimeter() / 2
            return math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))


def main():
    l = int(input("length:"))
    b = int(input("breadth:"))

    r = Rectangle()
    r.setDim(l, b)

    print("Rectangle Area:", r.getArea())
    print("Rectangle Perimeter:", r.getPerimeter())

    t = Triangle()
    print("Triangle Area:", t.getArea())
    print("Triangle Perimeter:", t.getPerimeter())


if __name__ == "__main__":
    main()