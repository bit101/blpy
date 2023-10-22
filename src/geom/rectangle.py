from .collision import *

class Rectangle:
    def __init__(self, x, y, w, h):
        self.x = x;
        self.y = y;
        self.w = w;
        self.h = h;

    def __mul__(self, scalar):
        return Rectangle(self.x * scalar, self.y * scalar, self.w * scalar, self.h * scalar)

    def __imul__(self, scalar):
        return Rectangle(self.x * scalar, self.y * scalar, self.w * scalar, self.h * scalar)

    def __rmul__(self, scalar):
        return Rectangle(self.x * scalar, self.y * scalar, self.w * scalar, self.h * scalar)

    def __truediv__(self, divisor):
        return Rectangle(self.x / divisor, self.y / divisor, self.w / scalar, self.h / scalar)

    def __itruediv__(self, divisor):
        return Rectangle(self.x / divisor, self.y / divisor, self.w / scalar, self.h / scalar)

    def __rtruediv__(self, divisor):
        return Rectangle(self.x / divisor, self.y / divisor, self.w / scalar, self.h / scalar)

    @staticmethod
    def from_points(p0, p1):
        x0 = p0.x
        y0 = p0.y
        x1 = p1.x
        y1 = p1.y
        if x0 > x1:
            x0, x1 = x1, x0
        if y0 > y1:
            y0, y1 = y1, y0
        return rectangle(x0, y0, x1 - x0, y1 - y0)

    def contains(self, point):
        return point_in_rect(p.x, p.y, self.x, self.y, self.w, self.h)

    def hit_rect(self, other):
        return rect_on_rect(self.x, self.y, self.w, self.h, other.x, other.y, other.w, other.h)

    def hit_segment(self, segment):
        return segment_on_rect(segment.x0, segment.y0, segment.x1, segment.y1, r.x, r.y, r.w, r.h)

