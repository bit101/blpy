import math
from .collision import *
from .point import *

class Circle:
    def __init__(self, x, y, radius):
        self.x = x
        self.y = y
        self.radius = radius
        
    def __repr__(self):
        return "geom.Circle(x: {}, y: {}, radius: {})".format(self.x, self.y, self.radius)

    def __mul__(self, scalar):
        return Circle(self.x * scalar, self.y * scalar, self.radius * scalar)

    def __imul__(self, scalar):
        return Circle(self.x * scalar, self.y * scalar, self.radius * scalar)

    def __rmul__(self, scalar):
        return Circle(self.x * scalar, self.y * scalar, self.radius * scalar)

    def __truediv__(self, scalar):
        return Circle(self.x / scalar, self.y / scalar, self.radius / scalar)

    def __itruediv__(self, scalar):
        return Circle(self.x / scalar, self.y / scalar, self.radius / scalar)

    def __rtruediv__(self, scalar):
        return Circle(self.x / scalar, self.y / scalar, self.radius / scalar)

    @staticmethod
    def from_point(point, radius):
        return Circle(point.x, point.y, radius)

    def contains(self, point):
        return point_in_circle(point.x, point.y, self.x, self.y, self.radius)

    def hit(self, other):
        return circle_on_circle(self.x, self.y, self.radius, other.x, other.y, other.radius)

    def intersection(self, other):
        if self.hit(other):
            d = math.sqrt(math.pow(self.x - other.x, 2) + math.pow(self.y - other.y, 2))
            l = (self.radius * self.radius - other.radius * other.radius + d * d) / (2 * d)
            h = math.sqrt(self.radius * self.radius - l * l)
            x0 = l * (other.x - self.x) / d + h * (other.y - self.y) / d + self.x
            y0 = l * (other.y - self.y) / d - h * (other.x - self.x) / d + self.y
            x1 = l * (other.x - self.x) / d - h * (other.y - self.y) / d + self.x
            y1 = l * (other.y - self.y) / d + h * (other.x - self.x) / d + self.y
            return Point(x0, y0), Point(x1, y1), True
        return nil, nil, False

    def invert_point(self, point):
        x, y = self.invert_xy(point.x, point.y)
        return Point(x, y)

    def invert_xy(self, x, y):
        dx = x - self.x
        dy = y - self.y
        dist0 = math.sqrt(dx * dx + dy * dy)
        dist1 = self.radius * self.radius / dist0
        ratio = dist1 / dist0
        return self.x + dx * ratio, self.y + dy * ratio

    def outer_circles(self, count, rotation = 0):
        circles = []
        angle = math.tau / count
        sina2 = math.sin(angle / 2)
        s = (self.radius * sina2) / (1 - sina2)
        r = self.radius + s
        a = rotation
        for i in range(count):
            circles.append(Circle(self.x + math.cos(a) * r, self.y + math.sin(a) * r, s))
            a += angle
        return circles

    def inner_circles(self, count, rotation = 0):
        circles = []
        angle = math.tau / count
        sina2 = math.sin(angle / 2)
        s = (self.radius * sina2) / (1 + sina2)
        r = self.radius - s
        a = rotation
        for i in range(count):
            circles.append(Circle(self.x + math.cos(a) * r, self.y + math.sin(a) * r, s))
            a += angle
        return circles

