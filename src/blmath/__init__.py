import math

def lerp(t, min_val, max_val):
    return min_val + (max_val - min_val) * t

def difference(a, b):
    return math.fabs(a - b)

def norm(value, min_val, max_val):
    return (value - min_val) / (max_val - min_val)

def map(srcValue, srcMin, srcMax, dstMin, dstMax):
    n = norm(srcValue, srcMin, srcMax)
    return lerp(n, dstMin, dstMax)

def mapLinExp(srcValue, srcMin, srcMax, dstMin, dstMax):
    if srcMin > srcMax:
        srcMin, srcMax = srcMax, srcMin
    if dstMin > dstMax:
        dstMin, dstMax = dstMax, dstMin
    if dstMin == 0:
        return math.nan
    return math.pow(dstMax / dstMin, (srcValue - srcMin) / (srcMax - srcMin)) * dstMin

def mapExpLin(srcValue, srcMin, srcMax, dstMin, dstMax):
    if srcMin > srcMax:
        srcMin, srcMax = srcMax, srcMin
    if dstMin > dstMax:
        dstMin, dstMax = dstMax, dstMin
    if srcMin == 0:
        return math.nan
    return (math.log(srcValue / srcMin)) / (math.log(srcMax / srcMin)) * (dstMax - dstMin) + dstMin

def wrap(value, min_val, max_val):
    rng = max_val - min_val
    return min_val + math.fmod((math.fmod(value - min_val, rng) + rng), rng)

def wrap_angle(value):
    return wrap(value, 0, math.tau)

def clamp(value, min_val, max_val):
    if min_val > max_val:
        min_val, max_val = max_val, min_val
    if value < min_val:
        return min_val
    if value > max_val:
        return max_val
    return value

def round_to(value, decimal):
    return round(value, decimal)

def round_to_nearest(value, mult):
    return round(value / mult) * mult

def sin_range(angle, min_val, max_val):
    return map(math.sin(angle), -1, 1, min_val, max_val)

def cos_range(angle, min_val, max_val):
    return map(math.cos(angle), -1, 1, min_val, max_val)

def lerp_sin(value, min_val, max_val):
	return sin_range(value * math.pi * 2 - math.pi / 2, min_val, max_val)

def gamma(val, gamma):
    return math.pow(val, 1 / gamma)

def simplify(x, y):
    g = math.gcd(x, y)
    return x / g, y / g

def mod_pos(a, b):
    val = math.fmod(a, b)
    if (val < 0 and b > 0) or (val > 0 and b < 0):
        val += b
    return val

def frange(start, stop, inc = 1):
    while start < stop:
        yield start
        start += inc

def sign(value):
    if value < 0:
        return -1
    if value > 0:
        return 1
    return 0
    
