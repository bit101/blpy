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





c0 = geom.Circle(200, 200, 100)

context.stroke_circle_object(c0)

p0 = geom.random_point_in_rect(0, 0, 400, 400)
p1 = c0.tangent_point(p0, False)
p2 = c0.tangent_point(p0, True)

context.point(p0, 2)
context.point(p1, 2)
context.point(p2, 2)

context.move_to(p1.x, p1.y)
context.line_to(p0.x, p0.y)
context.line_to(p2.x, p2.y)
context.stroke()





surface.write_to_png("out.png")
