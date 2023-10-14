import math
import blmath
import rand


####################
# Point class
####################

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return "geom.Point(x: {}, y: {})".format(self.x, self.y)

    def coords(self):
        return self.x, self.y

    def distance(p):
        return math.hypot(self.x - p.x, self.y - p.y)

    def magnitude(self):
        return math.hypot(p.x, p.y)

    def angle(self):
        return math.atan2(self.y, self.x)

    def angle_to(p):
        return math.atan2(p.y - self.y, p.x - self.x)

    def translate(self, x, y):
        self.x += x
        self.y += y

    def scale(self, sx, sy):
        self.x *= sx
        self.y *= sy

    def uniscale(self, s):
        self.scale(s, s)

    def rotate(self, angle):
        x = self.x * math.cos(angle) + self.y * math.sin(angle)
        y = self.y * math.cos(angle) - self.y * math.sin(angle)
        self.x = x;
        self.y = y


####################
# Point util methods
####################

def mid_point(p0, p1):
    return lerp_point(0.5, p0, p1)

def lerp_point(t, p0, p1):
    return Point(blmath.lerp(t, p0.x, p1.x), blmath.lerp(t, p0.y, p1.y))

def random_point_in_rect(x, y, w, h):
    return Point(rand.float_range(x, x + w), rand.float_range(y, y + h))

def random_point_in_circle(x, y, r, dist = True):
    angle = rand.angle()
    radius = 0
    if dist:
        radius = math.sqrt(rand.float()) * r
    else:
        radius = rand.float() * r
    return Point(x + math.cos(angle) * radius, y + math.sin(angle) * radius)

def random_point_in_triangle(pA, pB, pC):
    s = rand.float()
    st = math.sqrt(rand.float())
    a = 1 - st
    b = (1 - s) * st
    c = s * st
    return Point(a * pA.x + b * pB.x + c * pC.x, a * pA.y + b * pB.y + c * pC.y)

def bezier_point(t, p0, p1, p2, p3):
    one_minus_t = 1.0 - t
    m0 = one_minus_t * one_minus_t * one_minus_t
    m1 = 3.0 * one_minus_t * one_minus_t * t
    m2 = 3.0 * one_minus_t * t * t
    m3 = t * t * t
    return Point(
        m0 * p0.x + m1 * p1.x + m2 * p2.x + m3 * p3.x,
        m0 * p0.y + m1 * p1.y + m2 * p2.y + m3 * p3.y
    )

def quadratic_point(t, p0, p1, p2):
    one_minus_t = 1.0 - t
    m0 = one_minus_t * one_minus_t
    m1 = 2.0 * one_minus_t * t
    m2 = t * t
    return Point(
        m0 * p0.x + m1 * p1.x + m2 * p2.x,
        m0 * p0.y + m1 * p1.y + m2 * p2.y
    )

def clockwise(p1, p2, p3):
    return (p1.x - p3.x) * (p2.y - p3.y) - (p2.x - p3.x) * (p1.y - p3.y) > 0

def convex_hull(points):
    hull = []
    point_on_hull = points[0]
    for p in points:
        if p.x < point_on_hull.x:
            point_on_hull = p
    while True:
        hull.append(point_on_hull)
        end_point = points[0]
        for p in points:
            if end_point == point_on_hull or clockwise(p, end_point, point_on_hull):
                end_point = p
        point_on_hull = end_point
        if end_point == hull[0]:
            break
    return hull
