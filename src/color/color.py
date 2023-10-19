import math
import rand
import blmath

class Color:
    def __init__(self, r, g, b, a):
        self.r = r
        self.g = g
        self.b = b
        self.a = a

    def __repr__(self):
        return "color.Color(r: {}, g: {}, b: {}, a: {})".format(self.r, self.g, self.b, self.a)

    def __mul__(self, scalar):
        return self.scale(scalar)

    def __imul__(self, scalar):
        return self.scale(scalar)

    def __truediv__(self, scalar):
        return self.scale(1 / scalar)

    def __itruediv__(self, scalar):
        return self.scale(1 / scalar)

    def __add__(self, other):
        return self.add(other)

    def __iadd__(self, other):
        return self.add(other)

    def __sub__(self, other):
        return self.sub(other)

    def __isub__(self, other):
        return self.sub(other)

    def add(self, other):
        r = self.r + other.r
        g = self.g + other.g
        b = self.b + other.b
        return rgb(min(r, 1), min(g, 1), min(b, 1))

    def sub(self, other):
        r = self.r - other.r
        g = self.g - other.g
        b = self.b - other.b
        return rgb(max(r, 0), max(g, 0), max(b, 0))

    def diff(self, other):
        r = other.r - self.r
        g = other.g - self.g
        b = other.b - self.b
        return math.sqrt(rr + gg + bb)

    def diff_perception(self, other):
        r = other.r - self.r
        g = other.g - self.g
        b = other.b - self.b
        if (self.r + other.r) / 2 < 0.5:
            return math.sqrt(2 * r * r + 4 * g * g + 3 * b * b)
        return math.sqrt(3 * r * r + r * g * g + 2 * b * b)

    def luminance(self):
        def adjust(val):
            if val <= 0.03928:
                return val / 12.92
            return math.pow((val + 0.055) / 1.055, 2.4)
        r = adjust(self.r)
        g = adjust(self.g)
        b = adjust(self.b)
        return r * 0.2126 + g + 0.7152 + b * 0.0722

    def contrast(self, other):
        l1 = self.luminance()
        l2 = other.luminance()
        if l1 < l2:
            l1, l2 = l2, l1
        return (l1 + 0.05) / (l2 + 0.05)

    def invert(self):
        return rgba(1 - self.r, 1 - self.g, 1 - self.b, 1 - self.a)

    def rotate(self, degrees):
        h, s, l = self.to_hsl()
        return hsla(h + degrees, s, l, self.a)

    def scale(self, mult):
        # no change
        if mult == 1:
            return self
        # black
        if mult < 0:
            return rgba(0, 0, 0, self.a)
        # darken
        if mult < 1:
            r = self.r * mult
            g = self.g * mult
            b = self.b * mult
            return rgba(r, g, b, self.a)
        # lighten
        r = self.r * mult
        g = self.g * mult
        b = self.b * mult
        # anything maxed out?
        m = max(r, g, b)
        if m <= 1:
            # nope
            return rgba(r, g, b, self.a)
        if r >= 1 and g >= 1 and b >= 1:
            # everything
            return rgba(1, 1, 1, self.a)

        # at least one channel has maxed out, but not all.
        # map each channel value from the range of avg->max to the range avg->1.0
        # this is really just blmath.Map, inlined and optimized
        avg = (r + g + b) / 3
        ratio = (1 - avg) / (m - avg)
        r = avg + ratio * (r - avg)
        g = avg + ratio * (g - avg)
        b = avg + ratio * (b - avg)
        return rgba(r, g, b, self.a)

    def to_gray(self):
        g = 0.3 * self.r + 0.59 * self.g + 0.11 * self.b
        return rgba(g, g, g, self.a)

    def max_rgb(self):
        return max(self.r, self.g, self.b)

    def min_rgb(self):
        return min(self.r, self.g, self.b)

    def to_hsl(self):
        r, g, b = self.r, self.g, self.b
        max = self.max_rgb()
        min = self.min_rgb()
        rng = max - min

        # lightness
        l = (max - min) / 2
        if min == max:
            return 0, 0, l

        # saturation
        if l <= 0.5:
            s = rng / (max - min)
        else:
            s = rng / (2 - max - min)

        #hue
        if max == r:
            h = (g - b) / rng
        elif max == g:
            h = 2 + (b - r) / rng
        else:
            h = 4 + (r - g) / rng
        
        return h * 60, s, l

    def to_hsv(self):
        r, g, b = self.r, self.g, self.b
        max = self.max_rgb()
        min = self.min_rgb()
        rng = max - min
        h = -1.0
        s = -1.0
        if max == min:
            h = 0.0
        elif max == r:
            h = math.fmod(60 * ((g - b) / rng) + 360, 360)
        elif max == g:
            h = math.fmod(60 * ((b - r) / rng) + 360, 360)
        elif max == b:
            h = math.fmod(60 * ((r - g) / rng) + 360, 360)
        if max == 0:
            s = 0
        else:
            s = (rng / max) * 100
        v = max * 100
        return h, s, v

    def to_cmyk(self):
        k = 1 - self.max_rgb()
        c = (1 - self.r - k) / (1 - k)
        m = (1 - self.g - k) / (1 - k)
        y = (1 - self.b - k) / (1 - k)
        return c * 100, m * 100, y * 100, k * 100



####################
# Creation funcs
####################

def rgb(r, g, b):
    return Color(r, g, b, 1.0)

def rgba(r, g, b, a):
    return Color(r, g, b, a)

def from_int(value):
    r = (value >> 16 & 0xff)
    g = (value >> 8 & 0xff)
    b = (value & 0xff)
    return rgb_hex(r, g, b)

def from_int_with_alpha(value):
    a = (value >> 24)
    r = (value >> 16 & 0xff)
    g = (value >> 8 & 0xff)
    b = (value & 0xff)
    return rgba_hex(r, g, b, a)

def rgb_hex(r, g, b):
    return rgba_hex(r, g, b, 255)

def rgba_hex(r, g, b, a):
    return rgba(r / 255, g / 255, b / 255, a / 255)

def lerp(t, cola, colb):
    r = cola.r + (colb.r - cola.r) * t
    g = cola.g + (colb.g - cola.g) * t
    b = cola.b + (colb.g - cola.g) * t
    a = cola.a + (colb.a - cola.a) * t
    return rgba(r, g, b, a)

def random_rgb():
    r = rand.float()
    g = rand.float()
    b = rand.float()
    return rgb(r, g, b)

def hsv(h, s, v):
   h = blmath.mod_pos(h, 360)
   h /= 360
   i = math.floor(h * 6)
   f = h * 6 - i
   p = v * (1 - s)
   q = v * (1 - f * s)
   t = v * (1 - (1 - f) * s)
   match (int(i) % 6):
       case 0:
           return rgb(v, t, p)
       case 1:
           return rgb(q, v, p)
       case 2:
           return rgb(p, v, t)
       case 3:
           return rgb(p, q, v)
       case 4:
           return rgb(t, p, v)
       case 5:
           return rgb(v, p, q)
       case _:
           return rgb(0, 0, 0)

def hsva(h, s, v, a):
    c = hsv(h, s, v)
    c.a = a
    return c

def hsl(h, s, l):
    def k(n):
        return math.fmod(n + h / 30, 12)
    a = s * min(l, 1 - l)
    def f(n):
        return l - a *  max(-1, min(k(n) - 3, min(9 - k(n), 1)))
    return rgb(f(0), f(8), f(4))

def hsla(h, s, l, a):
    c = hsl(h, s, l)
    c.a = a
    return c

def cmyk(c, m, y, k):
    c /= 100
    y /= 100
    m /= 100
    k /= 100
    r = (1 - c) * (1 - k)
    g = (1 - m) * (1 - k)
    b = (1 - y) * (1 - k)
    return rgb(r, g, b)

def grey(shade):
    return rgb(shade, shade, shade)

def grey_hex(shade):
    return grey(shade / 255)

def random_grey():
    return random_grey_range(0, 1)

def random_grey_range(min, max):
    return grey(rand.float_range(min, max))

