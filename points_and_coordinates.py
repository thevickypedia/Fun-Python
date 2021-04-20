from math import sqrt


class Point:
    """
    __init__ - gets two parameters as coordinates stored as xx, yy and origin stored as x, y
    __str__ - returns the coordinates as string
    getX - returns the X value from the coordinates
    getY - returns the Y values from the coordinates
    distanceFromPoint - takes two arguments x and y and returns their distance from the coordinates
    distanceFromOrigin - returns the distance between the origin and the coordinates
    """
    count = 0

    def __init__(self, x, y):
        self.count += 1
        self.x = 0
        self.y = 0
        self.xx = x
        self.yy = y

    def __str__(self):
        return_val = self.xx, self.yy
        return str(return_val)

    def getX(self):
        return str(self.xx)

    def getY(self):
        return str(self.yy)

    def distanceFromPoint(self, x2, y2):
        x1 = self.xx
        y1 = self.yy
        d1 = (x2 - x1) ** 2
        d2 = (y2 - y1) ** 2
        return sqrt(d1 + d2)

    def distanceFromOrigin(self):
        x2 = self.x
        x1 = self.xx
        y2 = self.y
        y1 = self.yy
        d1 = (x2 - x1) ** 2
        d2 = (y2 - y1) ** 2
        return sqrt(d1 + d2)


if __name__ == '__main__':
    p1 = Point(3, 4)
    p2 = Point(3, 0)
    p1_values = [i for i in str(p1) if i.isdigit()]
    p2_values = [j for j in str(p2) if j.isdigit()]
    x1_ = int(p1_values[0])
    y1_ = int(p1_values[1])
    x2_ = int(p2_values[0])
    y2_ = int(p2_values[1])
    print(f'Distance between p1 and p2: {p1.distanceFromPoint(x2_, y2_)}')
    print(f'Distance from origin to p1: {p1.distanceFromOrigin()}')
    print(f'Distance from origin to p2: {p2.distanceFromOrigin()}')
    print(f'p1 < p2: {p1.distanceFromOrigin() < p2.distanceFromOrigin()}')
    print(f'p1 <= p2: {p1.distanceFromOrigin() <= p2.distanceFromOrigin()}')
    print(f'p1 > p2: {p1.distanceFromOrigin() > p2.distanceFromOrigin()}')
    print(f'p1 >= p2: {p1.distanceFromOrigin() >= p2.distanceFromOrigin()}')
    print(f'p1 == p2: {p1.distanceFromOrigin() == p2.distanceFromOrigin()}')
    print(f'p1 != p2: {p1.distanceFromOrigin() != p2.distanceFromOrigin()}')
    print(f"p1 == 'Hello': {p1 == 'Hello'}")
    print(f"p1 != 'Hello': {p1 != 'Hello'}")
    print(f"p2 == 'Hello': {p2 == 'Hello'}")
    print(f"p2 != 'Hello': {p2 != 'Hello'}")
    print(f"Number of point objects created: {p1.count}")
