import blpc
import rand
import math
import blmath
import geom
import random
import color
import noise

surface = blpc.Surface(400, 400)
context = blpc.Context(surface)
context.set_line_width (0.5)

scale = 0.02
res = 1

for x in range(0, 400, res):
    for y in range(0, 400, res):
        v = noise.simplex2(x * scale, y * scale)
        v = blmath.map(v, -1, 1, 0, 1)
        context.set_source_gray(v)
        context.fill_rectangle(x, y, res, res)



surface.write_to_png("out.png")
