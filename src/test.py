import blpc
import rand
import math
import blmath
import geom
import random


surface = blpc.Surface(400, 400)
context = blpc.Context(surface)
context.clear_white()
context.set_line_width (0.5)

p = geom.random_point_in_rect(0, 0, 400, 400)
context.point(p, 2)
l = geom.Line(100, 100, 200, 200)
context.stroke_line_object(l)



l2 = l.perpendicular(p)
context.stroke_line_object(l2)



surface.write_to_png("out.png")
