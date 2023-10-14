import math

class Vector:
    def __init__(self, u, v):
        self.u = u
        self.v = v

    def __repr__(self):
        return "geom.Vector(u: {}, v: {})".format(self.u, self.v)

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

    def norm(self):
        return math.hypot(self.u, self.v)

    def angle_to(self, other):
        dot = self.dot_product(other)
        norm = self.norm() * w.norm()
        return math.acos(dot / norm)

    def normalized(self):
        return self.scaled(1 / self.norm())

    def scaled(self, scale):
        return Vector(self.u * scale, self.v * scale)

    def project(self, other):
        return self.dot_product(other.normalized())


