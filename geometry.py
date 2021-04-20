from math import pi, sqrt


class GeometricObject(object):
    def __init__(self, color="white", filled=True):
        self.color = color
        self.filled = filled

    def get_color(self):
        return self.color

    def set_color(self, color):
        self.color = color

    def is_filled(self):
        return self.filled

    def set_filled(self, filled):
        self.filled = filled

    def __str__(self):
        return f"color: {self.color} " \
               f"and filled: {str(self.filled)}"


class Circle(GeometricObject):
    def __init__(self, radius=1.0, color='white', filled=True):
        super(Circle, self).__init__()
        self.radius, self.color, self.filled = radius, color, filled

    def get_area(self):
        return pi * self.radius * self.radius

    def get_perimeter(self):
        return pi * 2 * self.radius

    def __str__(self):
        return f"Circle: radius = {str(self.radius)}, " \
               f"color: {self.color} " \
               f"and filled: {str(self.filled)}"


class Triangle(GeometricObject):
    def __init__(self, side1=1.0, side2=1.0, side3=1.0, color='white', filled=True):
        super(Triangle, self).__init__()
        self.side1, self.side2, self.side3 = side1, side2, side3
        self.color, self.filled = color, filled

    def get_area(self):
        s = (self.side1 + self.side2 + self.side3) / 2
        calc_ = s * (s - self.side1) * (s - self.side2) * (s - self.side3)
        return sqrt(calc_)

    def get_perimeter(self):
        return self.side1 + self.side2 + self.side3

    def __str__(self):
        return f"Triangle: side1 = {str(self.side1)}, side2 = {str(self.side2)}, " \
               f"side3 = {str(self.side3)}, color = {self.color} " \
               f"and filled: {str(self.filled)}"


if __name__ == '__main__':
    c = Circle(3, 'red', True)
    print(c.__str__())
    print("Entering input values for a circle")
    r = float(input("Enter value for radius: "))
    c1 = Circle(r)
    print(c1)
    print(f"{round(float(c1.get_area()), 2)}")
    print(f"{round(float(c1.get_perimeter()), 2)}")
    print(c1.get_color())
    print(c1.is_filled())

    print("\nEntering input values for a triangle")
    s1 = float(input('Enter value for side1: '))
    s2 = float(input('Enter value for side2: '))
    s3 = float(input('Enter value for side3: '))
    color_input = input('Enter color of the triangle: ')
    filled_input = input('Is the triangle filled (1/0)? ')
    filled_input = (filled_input == "1")
    t = Triangle(s1, s2, s3, color_input, filled_input)
    print(t.__str__())
    print(f"{round(float(t.get_area()), 2)}")
    print(f"{round(float(t.get_perimeter()), 2)}")
    print(t.get_color())
    print(t.is_filled())
