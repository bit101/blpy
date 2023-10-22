from .circle import *
from .line import *
from .point import *
from .segment import *

def bisect(p0, p1, p2):
    a = math.atan2(p0.y - p1.y, p0.x - p1.x)
    c = math.atan2(p2.y - p1.y, p2.x - p1.x)
    b = a + (c - a) / 2
    return Point(p1.x + math.cos(b) * 100, p1.y + math.sin(b) * 100)

class Triangle:
    def __init__(self, x0, y0, x1, y1, x2, y2):
        self.p0 = Point(x0, y0)
        self.p1 = Point(x1, y1)
        self.p2 = Point(x2, y2)

    def __repr__(self):
        return f'geom.Triangle(({self.p0.x!r}, {self.p0.y!r}), ({self.p1.x!r}, {self.p1.y!r}), ({self.p2.x!r}, {self.p2.y!r}))'


    def __mul__(self, scalar):
        return Triangle(self.p0 * scalar, self.p1 * scalar, self.p2 * scalar)

    def __imul__(self, scalar):
        return Triangle(self.p0 * scalar, self.p1 * scalar, self.p2 * scalar)

    def __rmul__(self, scalar):
        return Triangle(self.p0 * scalar, self.p1 * scalar, self.p2 * scalar)

    def __truediv__(self, divisor):
        return Triangle(self.p0 / scalar, self.p1 / scalar, self.p2 / scalar)

    def __itruediv__(self, divisor):
        return Triangle(self.p0 / scalar, self.p1 / scalar, self.p2 / scalar)

    def __rtruediv__(self, divisor):
        return Triangle(self.p0 / scalar, self.p1 / scalar, self.p2 / scalar)

    @staticmethod
    def from_points(p0, p1, p2):
        t = Triangle(0, 0, 0, 0, 0, 0 )
        t.p0 = p0
        t.p1 = p1
        t.p2 = p2

    @staticmethod
    def equilateral_triangle(cx, cy, px, py):
        angle = math.atan2(py - cy, px - cx)
        dist = math.hypot(py - cy, px - cx)
        return Triangle(
            px, py,
            cx + math.cos(angle + math.tau / 3) * dist,
            cy + math.sin(angle + math.tau / 3) * dist,
            cx + math.cos(angle - math.tau / 3) * dist,
            cy + math.sin(angle - math.tau / 3) * dist,
        )

    def points(self):
        return [self.p0, self.p1, self.p2]

    def centroid(self):
        mida = lerp_point(0.5, self.p1, self.p2)
        midb = lerp_point(0.5, self.p0, self.p2)
        sega = Segment(self.p0.x, self.p0.y, mida.x, mida.y)
        segb = Segment(self.p1.x, self.p1.y, midb.x, midb.y)
        x, y, hit = sega.hit_segment(segb)
        return Point(x, y)

    def circumcenter(self):
        mida = lerp_point(0.5, self.p0, self.p1)
        linea = Line(self.p0.x, self.p0.y, self.p1.x, self.p1.y).perpendicular(mida)
        midb = lerp_point(0.5, self.p0, self.p2)
        lineb = Line(self.p0.x, self.p0.y, self.p2.x, self.p2.y).perpendicular(midb)
        x, y, hit = linea.hit_line(lineb)
        if hit:
            return Point(x, y)
        return None

    def circumcircle(self):
        p = self.circumcenter()
        if p == None:
            return None
        radius = p.distance(self.p0)
        return Circle(p.x, p.y, radius)


    def incenter(self):
        b = bisect(self.p0, self.p1, self.p2)
        a = bisect(self.p1, self.p0, self.p2)
        lineb = Line(b.x, b.y, self.p1.x, self.p1.y)
        linea = Line(a.x, a.y, self.p0.x, self.p0.y)
        x, y, hit = linea.hit_line(lineb)
        if hit:
            return Point(x, y)
        return None

    def incircle(self):
        center = self.incenter()
        line = Line(self.p0.x, self.p0.y, self.p1.x, self.p1.y)
        radius = line.distance_to(center)
        return Circle(center.x, center.y, radius)


    def orthocenter(self):
        bc = Line(self.p1.x, self.p1.y, self.p2.x, self.p2.y)
        pA = bc.closest_point(self.p0)

        ac = Line(self.p0.x, self.p0.y, self.p2.x, self.p2.y)
        pB = ac.closest_point(self.p1)

        line0 = Line(self.p0.x, self.p0.y, pA.x, pA.y)
        line1 = Line(self.p1.x, self.p1.y, pB.x, pB.y)

        x, y, hit = line0.hit_line(line1)
        return Point(x, y)

    def area(self):
        seg = Segment(self.p0.x, self.p0.y, self.p1.x, self.p1.y)
        h = seg.distance_to(self.p2)
        b = seg.length()
        return y * b / 2

    def contains(self, point):
        d1 = clockwise(point, self.p0, self.p1)
        d2 = clockwise(point, self.p1, self.p2)
        d3 = clockwise(point, self.p2, self.p0)
        hasCCW = not (d1 and d2 and d3)
        hasCW = d1 or d2 or d3
        return not (hasCCW and hasCW)

