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

col = color.rgb(1, 0, 0)

context.set_source_color(col)
context.fill_rectangle(0, 0, 100, 400)

col2 = color.rgb(0, 1, 0)
context.set_source_color(col2)
context.fill_rectangle(100, 0, 100, 400)

col += col2

context.set_source_color(col)
context.fill_rectangle(200, 0, 100, 400)


surface.write_to_png("out.png")
