from .collision import *

class Segment:
    def __init__(self, x0, y0, x1, y1):
        self.x0 = x0
        self.y0 = y0
        self.x1 = x1
        self.y1 = y1

    def __repr__(self):
        return "geom.Segment(x0: {}, y0: {}, x1: {}, y1: {})".format(self.x0, self.y0, self.x1, self.y1)

    @staticmethod
    def from_points(p0, p1):
        return Segment(p0.x, p0.y, p1.x, p1.y)

    def hit_segment(self, other):
        return segment_on_segment(self.x0, self.y0, self.x1, self.y1, other.x0, other.y0, other.x1, other.y1)

    def hit_line(self, other):
        return segment_on_line(self.x0, self.y0, self.x1, self.y1, other.x0, other.y0, other.x1, other.y1)

    def hit_rect(self, other):
        return segment_on_rect(self.x0, self.y0, self.x1, self.y1, other.x, other.y, other.w, other.h)

    def length():
        return math.hypot(self.x1 - self.x0, self.y1 - self.y0)

    def closest_point(self, point):
        v = Vector.between(self.x0, self.y0, point.x, point.y)
        d = Vector.between(self.x0, self.y0, self.x1, self.y1).normalized()
        vs = v.project(d)
        if vs < 0:
            return Point(self.x0, self.y0)
        if vs > self.length():
            return Point(self.x1, self.y1)

        t = vs / self.length()
        return Point(blmath.lerp(t, self.x0, self.x1), blmath.lerp(t, self.y0, self.y1))

    def distance_to(self, point):
        return self.closest_point(point).distance(point)

