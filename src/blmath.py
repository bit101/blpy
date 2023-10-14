import math

def lerp(t, min, max):
    return min + (max - min) * t

def difference(a, b):
    return math.fabs(a - b)

def norm(value, min, max):
    return (value - min) / (max - min)

def map(srcValue, srcMin, srcMax, dstMin, dstMax):
    n = nrom(srcValue, srcMin, srcMax)
    return lerp(norm, dstMin, dstMax)

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

def wrap(value, min, max):
    rng = max - min
    return min + math.fmod((math.fmod(value - min, rng) + rng), rng)

def wrap_angle(value):
    return wrap(value, 0, math.tau)

def clamp(value, min, max):
    if min > max:
        min, max = max, min
    if value < min:
        return min
    if value > max:
        return max
    return value

def round_to(value, decimal):
    return round(value, decimal)

def round_to_nearest(value, mult):
    return round(value / mult) * mult

def sin_range(angle, min, max):
    return map(math.sin(angle), -1, 1, min, max)

def cos_range(angle, min, max):
    return map(math.cos(angle), -1, 1, min, max)

def lerp_sin(value, min, max):
	return sin_range(value * math.pi * 2 - math.pi / 2, min, max)

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

