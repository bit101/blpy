import math
import random

def seed(s):
    random.seed(s)

def rand_seed():
    random.seed()

def float():
    return random.random()

def int_range(min, max):
    return random.randint(min, max)

def float_range(min, max):
    return min + float() * (max - min)

def angle():
    return float_range(0, math.tau)

def float_array(size, min, max):
    arr = []
    for i in range(size):
        arr.append(float_range(min, max))
    return arr

def int_array(size, min, max):
    arr = []
    for i in range(size):
        arr.append(int_range(min, max))
    return arr

def boolean():
    return weighted_bool(0.5)

def weighted_bool(weight):
    return float() < weight

def string(length):
    s = ""
    for i in range(length):
        c = int_range(33, 128)
        s += chr(c)
    return s

def string_lower(length):
    s = ""
    for i in range(length):
        c = int_range(97, 122)
        s += chr(c)
    return s

def string_upper(length):
    s = ""
    for i in range(length):
        c = int_range(65, 90)
        s += chr(c)
    return s

def string_alpha(length):
    s = ""
    for i in range(length):
        c = int_range(65, 115)
        if c > 90:
            c += 6
        s += chr(c)
    return s

def string_from(length, chars):
    s = ""
    for i in range(length):
        s += random.choice(chars)
    return s

def gauss_range(min, max):
    rng = (max - min) / 2
    mean = min + rng
    # a standard deviation of 1.0 will have 99.7% of its values between -3 and +3.
    # but for 100,000 samples, that's still around 300 points beyond that range.
    # 99.994% will be between -4 and 4.
    # for 100,000 samples, that's around 6 outside the range. better.
    # so we get the standard deviation by dividing the range by 4.0
    std = rng / 4.0
    return random.gauss(mean, std)

def power(min, max, power):
    return min + math.pow(float(), power) * (max - min)

