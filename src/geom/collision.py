import math
import blmath
from .vector import *

def point_in_rect(x, y, rx, ry, rw, rh):
	return x >= rx and x <= rx + rw and y >= ry and y <= ry + rh


def point_in_circle(x, y, cx, cy, cr):
    return math.hypot(cx - x, cy - y) <= cr

def circle_on_circle(x0, y0, r0, x1, y1, r1):
    dist = math.hypot(x1 - x0, y1 - y0)
    return dist < (r0 + r1)

def segment_on_line(x0, y0, x1, y1, x2, y2, x3, y3):
    """
    SegmentOnLine determines whether or not a segment intersects an infinite length line
    and returns the point it intersects if it does.
    x0, y0 -> x1, y1 = segment. x2, y2 -> x3, y3 = line
    """
    v0 = Vector.between(x0, y0, x1, y1)
    v1 = Vector.between(x2, y2, x3, y3)
    cross_prod = v0.cross_product(v1)
    if math.isclose(cross_prod, 0):
        # parallel
        return 0, 0, false

    delta = Vector.between(x0, y0, x2, y2)
    t1 = (delta.u * v1.v - delta.v * v1.u) / cross_prod

    if t1 >= 0 and t1 <= 1:
        return blmath.lerp(t1, x0, x1), blmath.lerp(t1, y0, y1), True
    return 0, 0, False

def segment_on_segment(x0, y0, x1, y1, x2, y2, x3, y3):
    """SegmentOnSegment returns whether or not two line segments intersect and the point they intersect if they do."""
    v0 = Vector.between(x0, y0, x1, y1)
    v1 = Vector.between(x2, y2, x3, y3)
    cross_prod = v0.cross_product(v1)
    if math.isclose(cross_prod, 0):
        # parallel
        return 0, 0, False
    delta = Vector.between(x0, y0, x2, y2)
    t1 = (delta.u * v1.v - delta.v * v1.u) / cross_prod
    t2 = (delta.u * v0.v - delta.v * v0.u) / cross_prod

    if t1 >= 0 and t1 <= 1 and t2 >= 0 and t2 <= 1:
        return blmath.lerp(t1, x0, x1), blmath.lerp(t1, y0, y1), True
    return 0, 0, False

def line_on_line(x0, y0, x1, y1, x2, y2, x3, y3):
    """LineOnLine returns whether or not two infinite length lines intersect and the point they intersect if they do."""
    v0 = Vector.between(x0, y0, x1, y1)
    v1 = Vector.between(x2, y2, x3, y3)
    cross_prod = v0.cross_product(v1)
    if math.isclose(cross_prod, 0):
        # parallel
        return 0, 0, False
    delta = Vector.between(x0, y0, x2, y2)
    t1 = (delta.u * v1.v - delta.v * v1.u) / cross_prod
    return blmath.lerp(t1, x0, x1), blmath.lerp(t1, y0, y1), True

def point_distance_to_segment(px, py, x0, y0, x1, y1):
    # https://stackoverflow.com/questions/849211/shortest-distance-between-a-point-and-a-line-segment
    a = px - x0
    b = py - y0
    c = x1 - x0
    d = y1 - y0
    dot = a * c + b * d
    len_sq = c * c + d * d
    # watching out for zero length line
    param = -1.0 if len_sq == 0 else dot / len_sq
    if param < 0:
        xx = x0
        yy = y0
    elif param > 1:
        xx = x1
        yy = y1
    else:
        xx = x0 + param * c
        yy = y0 + param * d
    return math.hypot(px - xx, py - yy)

def point_distance_to_line(px, py, x0, y0, x1, y1):
    dx = x1 - x0
    dy = y1 - y0
    num = math.fabs(dx * (y0 - py) - dy * (x0 - px))
    denom = math.sqrt(dx * dx + dy * dy)
    return num / denom
    
def circle_on_line(x0, y0, x1, y1, cx, cy, r):
    p = Point(cx, cy)
    l = Line(x0, y0, x1, y1)
    lp = l.closest_point(p)
    d = lp.distance(p)

    if d < r:
        h = r - d
        c = math.sqrt(r * r - math.pow(r - h, 2))
        angle = math.atan2(y1 - y0, x1 - x0)
        cos = math.cos(angle)
        sin = math.sin(angle)
        return Point(lp.x + cos * c, lp.y + sin * c), Point(lp.x - cos * c, lp.y - sin * c), True
    return nil, nil, False

def rect_on_rect(x0, y0, w0, h0, x1, y1, w1, h1):
    return not (
        x1 > x0 + w0 or
        x1 + w1 < x0 or
        y1 > y0 + h0 or
        y1 + h1 < y0
    )

def segment_on_rect(x0, y0, x1, y1, rx, ry, rw, rh):
    x, y, hit = segment_on_segment(x0, y0, x1, y1, rx, ry, rx + rw, ry)
    if hit:
        return True
    x, y, hit = segment_on_segment(x0, y0, x1, y1, rx + rw, ry, rx + rw, ry+rh)
    if hit:
        return True
    x, y, hit = segment_on_segment(x0, y0, x1, y1, rx + rw, ry + rh, rx, ry + rh)
    if hit:
        return True
    x, y, hit = segment_on_segment(x0, y0, x1, y1, rx, ry + rh, rx, ry)
    if hit:
        return True
    return False

