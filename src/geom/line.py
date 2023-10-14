from .collision import *
from .point import *
from .vector import *


class Line:
    def __init__(self, x0, y0, x1, y1):
        self.x0 = x0
        self.y0 = y0
        self.x1 = x1
        self.y1 = y1
        
    def __repr__(self):
        return "geom.Line(x0: {}, y0: {}, x1: {}, y1: {})".format(self.x0, self.y0, self.x1, self.y1)

    @staticmethod
    def from_points(p0, p1):
        return Line(p0.x, p0.y, p1.x, p1.y)

    def closest_point(self, point):
        v = Vector.between(self.x0, self.y0, point.x, point.y)
        d = Vector.between(self.x0, self.y0, self.x1, self.y1).normalized()
        vs = v.project(d)
        t = vs / math.hypot(self.x1 - self.x0, self.y1 - self.y0)
        return Point(blmath.lerp(t, self.x0, self.x1), blmath.lerp(t, self.y0, self.y1))

    def hit_segment(self, segment):
        return segment_on_line(segment.x0, segment.y0, segment.x1, segment.y1, self.x0, self.y0, self.x1, self.y1)

    def hit_line(self, segment):
        return line_on_line(segment.x0, segment.y0, segment.x1, segment.y1, self.x0, self.y0, self.x1, self.y1)

    def distance_to(self, point):
        return self.closest_point(point).distance(point)

    def perpendicular(self, point):
        dx = self.x1 - self.x0
        dy = self.y1 - self.y0
        return Line(point.x, point.y, point.x - dy, point.y + dx)

