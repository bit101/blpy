import math

class Vector:
    def __init__(self, u, v):
        self.u = u
        self.v = v

    def __repr__(self):
        return f'geom.Vector(u: {self.u!r}, v: {self.v!r})'

    def __abs__(self):
        return math.hypot(self.u, self.v)

    def __add__(self, other):
        return Vector(self.u + other.u, self.v + other.v)

    def __iadd__(self, other):
        return Vector(self.u + other.u, self.v + other.v)

    def __sub__(self, other):
        return Vector(self.u - other.u, self.v - other.v)

    def __isub__(self, other):
        return Vector(self.u - other.u, self.v - other.v)

    def __mul__(self, scalar):
        return Vector(self.u * scalar, self.v * scalar)

    def __imul__(self, scalar):
        return Vector(self.u * scalar, self.v * scalar)

    def __rmul__(self, scalar):
        return Vector(self.u * scalar, self.v * scalar)

    def __truediv__(self, scalar):
        return Vector(self.u / scalar, self.v / scalar)

    def __itruediv__(self, scalar):
        return Vector(self.u / scalar, self.v / scalar)

    def __rtruediv__(self, scalar):
        return Vector(self.u / scalar, self.v / scalar)

    def __neg__(self):
        return Vector(-self.u, -self.v)

    @staticmethod
    def between(x0, y0, x1, y1):
        return Vector(x1 - x0, y1 - y0)

    @staticmethod
    def from_points(p0, p1):
        return Vector(p1.x - p0.x, p1.y - p0.y)

    def dot_product(self, other):
     	return self.u * other.u + self.v * other.v

    def cross_product(self, other):
        return self.u * other.v - self.v * other.u

    def angle_to(self, other):
        dot = self.dot_product(other)
        norm = abs(self) * abs(other)
        return math.acos(dot / norm)

    def normalized(self):
        return self.scaled(1 / abs(self))

    def project(self, other):
        return self.dot_product(other.normalized())


