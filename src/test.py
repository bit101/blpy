import blpc
import rand
import math
import blmath
import geom
import random
import color


surface = blpc.Surface(400, 400)
context = blpc.Context(surface)
context.set_line_width (0.5)


p = color.Palette()
for i in range(10):
    p.add(color.random_rgb())

p.sort()

for i in range(len(p.colors)):
    c = p.colors[i]
    print(c.luminance())
    context.set_source_color(c)
    context.fill_rectangle(i * 40, 0, 40, 400)




surface.write_to_png("out.png")
