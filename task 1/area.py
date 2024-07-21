import math

class Shape:
    def area(self):
        raise NotImplementedError("Должен быть реализован данный метож!")

    def is_right_angle(self):
        raise NotImplementedError("Этот метод неприменим для этой формы.")

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

class Triangle(Shape):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
        self._validate_triangle()

    def _validate_triangle(self):
        if (self.a + self.b <= self.c) or (self.a + self.c <= self.b) or (self.b + self.c <= self.a):
            raise ValueError("The provided sides do not form a triangle")

    def area(self):
        s = (self.a + self.b + self.c) / 2
        return math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))

    def is_right_angle(self):
        sides = sorted([self.a, self.b, self.c])
        return math.isclose(sides[0] ** 2 + sides[1] ** 2, sides[2] ** 2)

def calculate_area(shape):
    if not isinstance(shape, Shape):
        raise TypeError("Объект должен быть экземпляром Shape")
    return shape.area()

def is_right_angle_triangle(shape):
    if not isinstance(shape, Triangle):
        raise TypeError("Объект должен быть экземпляром Triangle")
    return shape.is_right_angle()
