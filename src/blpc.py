import cairo
import color
import geom
import rand
import math

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
    
def Surface(width, height):
    return cairo.ImageSurface(cairo.FORMAT_ARGB32, width, height)

class Context(cairo.Context):
    def __init__(self, surface):
        self.width = surface.get_width()
        self.height = surface.get_height()
        super().__init__()

    ####################
    # Clear and Set
    ####################
    def black_on_white(self):
        self.clear_white()
        self.set_source_black()

    def white_on_black(self):
        self.clear_black()
        self.set_source_white()

    def blueprint(self):
        self.clear_rgb(self, 0, 0.0784, 0.5176)
        self.set_source_white()

    ####################
    # Clear 
    ####################
    def clear_rgb(self, r, g, b):
        self.save()
        self.set_source_rgb(r, g, b)
        self.paint()
        self.restore()

    def clear_rgba(self, r, g, b, a):
        self.save()
        self.set_source_rgba(r, g, b, a)
        self.paint()
        self.restore()

    def clear_color(self, color):
        self.clear_rgba(color.r, color.g, color.b, color.a)
        pass

    def clear_white(self):
        self.clear_rgb(1, 1, 1)

    def clear_black(self):
        self.clear_rgb(0, 0, 0)

    def clear_gray(self, g):
        self.clear_rgb(g, g, g)

    def clear_hsv(self, h, s, v):
        self.clear_color(color.hsv(h, s, v))

    def clear_hsva(self, h, s, v, a):
        self.clear_color(color.hsva(h, s, v, a))

    def clear_random_gray(self):
        g = rand.float()
        self.clear_rgb(g, g, g)


    def clear_random_rgb(self):
        r = rand.float()
        g = rand.float()
        b = rand.float()
        self.clear_rgb(r, g, b)

    ####################
    # Set
    ####################
    def set_source_color(self, color):
        self.set_source_rgba(color.r, color.g, color.b, color.a)
        pass

    def set_source_black(self):
        self.set_source_rgb(0, 0, 0)

    def set_source_white(self):
        self.set_source_rgb(1, 1, 1)

    def set_source_gray(self, g):
        self.set_source_rgb(g, g, g)

    def set_source_hsv(self, h, s, v):
        self.set_source_color(color.hsv(h, s, v))

    def set_source_hsva(self, h, s, v, a):
        self.set_source_color(color.hsva(h, s, v, a))

    def set_source_random_gray(self):
        g = rand.float()
        self.set_source_rgb(g, g, g)

    def set_source_random_rgb(self):
        r = rand.float()
        g = rand.float()
        b = rand.float()
        self.set_source_rgb(r, g, b)

    ####################
    # Misc
    ####################
    def translate_center(self):
        x, y = self.get_center()
        self.translate(x, y)

    def get_center(self):
        return self.width / 2, self.height / 2

    def get_aspect_ratio(self):
        return self.width / self.height

    def get_size(self):
        return self.width, self.height

    ####################
    # Shapes
    ####################

    ##########
    # arc, etc
    ##########
    def fill_arc(self, x, y, r, a1, a2):
        self.arc(x, y, r, a1, a2)
        self.fill()

    def stroke_arc(self, x, y, r, a1, a2):
        self.arc(x, y, r, a1, a2)
        self.stroke()

    def fill_arc_negative(self, x, y, r, a1, a2):
        self.arc_negative(x, y, r, a1, a2)
        self.fill()

    def stroke_arc_negative(self, x, y, r, a1, a2):
        self.arc_negative(x, y, r, a1, a2)
        self.stroke()

    def chord(self, x, y, r, a1, a2):
        self.move_to(x + math.cos(a1) * r, y + math.sin(a1) * r)
        self.line_to(x + math.cos(a2) * r, y + math.sin(a2) * r)

    def stroke_chord(self, x, y, r, a1, a2):
        self.chord(x, y, r, a1, a2)
        self.stroke()

    def circle_segment(self, x, y, r, a1, a2):
        self.arc(x, y, r, a1, a2)
        self.close_path()

    def stroke_circle_segment(self, x, y, r, a1, a2):
        self.circle_segment(x, y, r, a1, a2)
        self.stroke()

    def fill_circle_segment(self, x, y, r, a1, a2):
        self.circle_segment(x, y, r, a1, a2)
        self.fill()

    def circle_segment_negative(self, x, y, r, a1, a2):
        self.arc_negative(x, y, r, a1, a2)
        self.close_path()

    def stroke_circle_segment_negative(self, x, y, r, a1, a2):
        self.circle_segment_negative(x, y, r, a1, a2)
        self.stroke()

    def fill_circle_segment_negative(self, x, y, r, a1, a2):
        self.circle_segment_negative(x, y, r, a1, a2)
        self.fill()

    def circle_sector(self, x, y, r, a1, a2):
        self.move_to(x, y)
        self.arc(x, y, r, a1, a2)
        self.close_path()

    def stroke_circle_sector(self, x, y, r, a1, a2):
        self.circle_sector(x, y, r, a1, a2)
        self.stroke()

    def fill_circle_sector(self, x, y, r, a1, a2):
        self.circle_sector(x, y, r, a1, a2)
        self.fill()

    def circle_sector_negative(self, x, y, r, a1, a2):
        self.arc_negative(x, y, r, a1, a2)
        self.close_path()

    def stroke_circle_sector_negative(self, x, y, r, a1, a2):
        self.circle_sector_negative(x, y, r, a1, a2)
        self.stroke()

    def fill_circle_sector_negative(self, x, y, r, a1, a2):
        self.circle_sector_negative(x, y, r, a1, a2)
        self.fill()

    ##########
    # arrow
    ##########
    def draw_arrow(self, x0, y0, x1, y1, point_size):
        angle = math.atan2(y1 - y0, x1 - x0)
        length = math.hypot(x1 - x0, y1 - y0)
        self.save()
        self.translate(x0, y0)
        self.rotate(angle)
        self.move_to(0, 0)
        self.line_to(length, 0)
        self.line_to(length - point_size, -point_size*0.6)
        self.move_to(length, 0)
        self.line_to(length - point_size, point_size*0.6)
        self.restore()

    def stroke_arrow(self, x0, y0, x1, y1, point_size):
        self.draw_arrow(x0, y0, x1, y1, point_size)
        self.stroke()


    def draw_double_arrow(self, x0, y0, x1, y1, point_size):
        angle = math.atan2(y1 - y0, x1 - x0)
        length = math.hypot(x1 - x0, y1 - y0)
        self.save()
        self.translate(x0, y0)
        self.rotate(angle)
        self.move_to(0, 0)
        self.line_to(length, 0)
        self.line_to(length - point_size, -point_size * 0.6)
        self.move_to(length, 0)
        self.line_to(length - point_size, point_size * 0.6)
        self.move_to(point_size, point_size * 0.6)
        self.line_to(0, 0)
        self.line_to(point_size, -point_size * 0.6)
        self.restore()

    def stroke_double_arrow(self, x0, y0, x1, y1, point_size):
        self.draw_double_arrow(x0, y1, x1, y1, point_size)
        self.stroke()

    ##########
    # circle
    ##########
    def circle(self, x, y, r):
        self.arc(x, y, r, 0, math.tau)

    def fill_circle(self, x, y, r):
        self.circle(x, y, r)
        self.fill()

    def stroke_circle(self, x, y, r):
        self.circle(x, y, r)
        self.stroke()

    def fill_circle_object(self, circle):
        self.fill_circle(circle.x, circle.y, circle.radius)

    def stroke_circle_object(self, circle):
        self.stroke_circle(circle.x, circle.y, circle.radius)

    def fill_circles(self, circle_list):
        for c in circle_list:
            self.fill_circle_object(c)

    def stroke_circles(self, circle_list):
        for c in circle_list:
            self.stroke_circle_object(c)

    ##########
    # guides
    ##########
    def crosshair(self, x, y, size = 10):
        self.move_to(x - size, y)
        self.line_to(x + size, y)
        self.move_to(x, y - size)
        self.line_to(x, y + size)
        self.stroke()

    def draw_origin(self, size = 10):
        self.crosshair(0, 0, size)

    def draw_axes(self, line_width = 1):
        orig_line_width = self.get_line_width()
        self.set_line_width(line_width)
        w, h = self.get_size()
        self.move_to(0, -h)
        self.line_to(0, h)
        self.move_to(-w, 0)
        self.line_to(w, 0)
        self.stroke()
        self.set_line_width(orig_line_width)

    ##########
    # curves
    ##########
    def stroke_curve_to(self, x0, y0, x1, y1, x2, y2):
        self.curve_to(x0, y0, x1, y1, x2, y2)
        self.stroke()

    def quadratic_curve_to(self, x0, y0, x1, y1):
        px, py = self.get_current_point()
        self.curve_to(
            2.0 / 3.0 * x0 + 1.0 / 3.0 * px,
            2.0 / 3.0 * y0 + 1.0 / 3.0 * py,
            2.0 / 3.0 * x0 + 1.0 / 3.0 * x1,
            2.0 / 3.0 * y0 + 1.0 / 3.0 * y1,
            x1, y1,
        )

    def stroke_quadratic_curve_to(self, x0, y0, x1, y1):
        self.quadratic_curve_to(x0, y0, x1, y1)
        self.stroke()

    ##########
    # ellipse
    ##########
    def ellipse(self, x, y, xr, yr):
        if xr == 0 or yr == 0:
            return
        self.save()
        self.translate(x, y)
        self.scale(xr, yr)
        self.circle(0, 0, 1)
        self.restore()

    def fill_ellipse(self, x, y, xr, yr):
        self.ellipse(x, y, xr, yr)
        self.fill()

    def stroke_ellipse(self, x, y, xr, yr):
        self.ellipse(x, y, xr, yr)
        self.stroke()

    ##########
    # fracline
    ##########
    def fractal_line(self, x1, y1, x2, y2, roughness, iterations):
        dx = x2 - x1
        dy = y2 - y1
        offset = math.sqrt(dx * dx + dy * dy) * 0.15
        path = [geom.Point(x1, y1), geom.Point(x2, y2)]

        for i in range(iterations):
            newpath = []
            for j in range(len(path)):
                p = path[j]
                newpath.append(geom.Point(p.x, p.y))
                if j < len(path) - 1:
                    mid = geom.mid_point(p, path[j + 1])
                    mid.x += rand.float_range(-offset, offset)
                    mid.y += rand.float_range(-offset, offset)
                    newpath.append(mid)
            offset *= roughness
            path = newpath
        self.path(path)

    def stroke_fractal_line(self, x1, y1, x2, y2, roughness, iterations):
        self.fractal_line(x1, y1, x2, y2, roughness, iterations)
        self.stroke()

    ##########
    # grid
    ##########
    def grid(self, x, y, w, h, xres, yres):
        xx = x 
        yy = y
        while (xx <= x + w):
            self.move_to(xx, y)
            self.line_to(xx, y + h)
            xx += xres
        while (yy <= y + h):
            self.move_to(x, yy)
            self.line_to(x + w, yy)
            yy += yres
        self.stroke()


    def grid_full(res, line_width = 1):
        self.save()
        # todo

    ###########
    # guilloche
    ###########
    def guillloche(self, x, y, inner_radius, inner_amp, inner_cycles, inner_rotation, outer_radius, outer_amp, outer_cycles, outer_rotation, nodes, div):
        for t in frange(0, math.tau * div, 0.01):
            r0 = inner_radius + math.sin(t * inner_cycles + inner_rotation) * inner_amp;
            r1 = outer_radius + math.sin(t * outer_cycles + outer_rotation) * outer_amp;
            rng = (r1 - r0) * 0.5
            mid = r0 + rng
            radius = mid + math.sin(t * nodes / div) * rng
            self.line_to(x + math.cos(t) * radius, y + math.sin(t) * radius)
        self.stroke()

    def heart(self, x, y, w, h, r = 0):
        self.save()
        self.translate(x, y)
        self.rotate(r)
        path = []
        res = math.sqrt(w * h)
        for i in range(int(res)):
            a = math.tau * i / res
            x = w * math.pow(math.sin(a), 3)
            y = h * (0.8125 * math.cos(a) - 0.3125 * math.cos(2 * a) - 0.125 * math.cos(3 * a) - 0.0625 * math.cos(4 * a))
            path.append(geom.Point(x, -y))
        self.path(path)
        self.restore()

    def fill_heart(self, x, y, w, h, r = 0):
        self.heart(x, y, w, h, r)
        self.fill()

    def stroke_heart(self, x, y, w, h, r = 0):
        self.heart(x, y, w, h, r)
        self.stroke()

    ##########
    # hex grid
    ##########
    def hex_grid(self, x, y, w, h, res0, res1):
        sin60r = math.sin(math.pi / 3) * res0
        xinc = 2 * sin60r
        yinc = res0 * 1.5
        offset = 0

        for yy in frange(y, y + h + yinc, yinc):
            for xx in frange(x, x + w + xinc, xinc):
                self.polygon(xx + offset, yy, res1, 6, math.pi / 2)
            if offset == 0:
                offset = sin60r
            else:
                offset = 0

    def fill_hex_grid(self, x, y, w, h, res0, res1):
        self.hex_grid(x, y, w, h, res0, res1)
        self.fill()

    def stroke_hex_grid(self, x, y, w, h, res0, res1):
        self.hex_grid(x, y, w, h, res0, res1)
        self.stroke()

    ##########
    # lines
    ##########
    def stroke_line(self, x0, y0, x1, y1):
        self.move_to(x0, y0)
        self.line_to(x1, y1)
        self.stroke()

    def stroke_line_object(self, line):
        self.line_through(line.x0, line.y0, line.x1, line.y1, self.width + self.height)

    def stroke_segment_object(self, line):
        self.stroke_line(line.x0, line.y0, line.x1, line.y1)

    def line_through(self, x0, y0, x1, y1, overlap):
        self.save()
        self.translate(x0, y0)
        self.rotate(math.atan2(y1 - y0, x1 - x0))
        p2 = math.hypot(x0 - x1, y0 - y1)
        self.move_to(-overlap, 0)
        self.line_to(p2 + overlap, 0)
        self.stroke()
        self.restore()

    ##########
    # multi
    ##########
    def multi_curve(self, points):
        self.move_to(points[0].x, points[0].y)
        mid = geom.mid_point(points[0], points[1])
        self.line_to(mid.x, mid.y)
        for i in range(1, len(points) - 1):
            p0 = points[i]
            p1 = points[i + 1]
            mid = geom.mid_point(p0, p1)
            self.quadratic_curve_to(p0.x, p0.y, mid.x, mid.y)
        p = points[-1]
        self.line_to(p.x, p.y)

    def stroke_multi_curve(self, points):
        self.multi_curve(points)
        self.stroke()

    def multi_loop(self, points):
        pA = points[0]
        pZ = points[-1]
        mid1 = geom.mid_point(pA, pZ)
        self.move_to(mid1.x, mid1.y)
        for i in range(len(points) - 1):
            p0 = points[i]
            p1 = points[i + 1]
            mid = geom.mid_point(p0, p1)
            self.quadratic_curve_to(p0.x, p0.y, mid.x, mid.y)
        self.quadratic_curve_to(pZ.x, pZ.y, mid1.x, mid1.y)

    def fill_multi_loop(self, points):
        self.multi_loop(points)
        self.fill()

    def stroke_multi_loop(self, points):
        self.multi_loop(points)
        self.stroke()

    ##########
    # path
    ##########
    def path(self, points, close = False):
        self.move_to(points[0].x, points[0].y)
        for i in range(1, len(points)):
            p = points[i]
            self.line_to(p.x, p.y)

    def fill_path(self, points):
        self.path(points, True)
        self.fill()

    def stroke_path(self, points, close = False):
        self.path(points)
        if close:
            self.close_path()
        self.stroke()

    ##########
    # points
    ##########
    def point(self, point, r):
        self.fill_circle(point.x, point.y, r)

    def points(self, points, radius = 0.5):
        for p in points:
            self.fill_point(p.x, p.y, radius)

    def label_points(self, points, numeric):
        if numeric:
            num = 0
            for p in points:
                print(p)
                self.draw_text(str(num), p.x + 5, p.y + 5)
                num += 1
        else:
            char = 65
            count = 0
            for p in points:
                label = chr(char)
                if count > 0:
                    label = "{}{}".format(label, count)
                self.draw_text(label, p.x + 5, p.y + 5)
                char += 1
                if char > 90:
                    char = 65
                    count += 1

    ##########
    # polygon
    ##########
    def polygon(self, x, y, r, sides, rotation):
        self.save()
        self.translate(x, y)
        self.rotate(rotation)
        self.move_to(r, 0)
        for i in range(sides):
            angle = math.tau / sides * i
            self.line_to(math.cos(angle) * r, math.sin(angle) * r)
        self.line_to(r, 0)
        self.restore()

    def stroke_polygon(self, x, y, r, sides, rotation):
        self.polygon(x, y, r, sides, rotation)
        self.stroke()

    def fill_polygon(self, x, y, r, sides, rotation):
        self.polygon(x, y, r, sides, rotation)
        self.fill()

    ##########
    # ray
    ##########
    def ray(self, x, y, angle, offset, length):
        self.save()
        self.translate(x, y)
        self.rotate(angle)
        self.move_to(offset, 0)
        self.line_to(offset + length, 0)
        self.stroke()
        self.restore()

    ##########
    # rect
    ##########
    def fill_rectangle(self, x, y, w, h):
        self.rectangle(x, y, w, h);
        self.fill()

    def stroke_rectangle(self, x, y, w, h):
        self.rectangle(x, y, w, h);
        self.stroke()

    def fill_rectangle_object(self, rect):
        self.rectangle(rect.x, rect.y, rect.w, rect.h);
        self.fill()

    def stroke_rectangle_object(self, rect):
        self.rectangle(rect.x, rect.y, rect.w, rect.h);
        self.stroke()

    ###########
    # right tri
    ###########
    def draw_right_triangle(self, x, y, w, h, rotation):
        self.save()
        self.translate(x, y)
        self.rotate(rotation)
        self.move_to(0, 0)
        self.line_to(w, 0)
        self.line_to(0, h)
        self.line_to(0, 0)
        self.restore()

    def fill_right_triangle(self, x, y, w, h, rotation):
        self.draw_right_triangle(x, y, w, h, rotation)
        self.fill()

    def stroke_right_triangle(self, x, y, w, h, rotation):
        self.draw_right_triangle(x, y, w, h, rotation)
        self.stroke()

    ############
    # round rect
    ############
    def round_rectangle(self, x, y, w, h, r):
        self.move_to(x + r, y)
        self.line_to(x + w - r, y)
        self.arc(x + w - r, y + r, r, -math.pi / 2, 0)
        self.line_to(x + w, y + h - r)
        self.arc(x + w - r, y + h - r, r, 0, math.pi / 2)
        self.line_to(x + r, y + h)
        self.arc(x + r, y + h - r, r, math.pi / 2, math.pi)
        self.line_to(x, y + r)
        self.arc(x + r, y + r, r, math.pi, -math.pi / 2)
        self.close_path()

    def fill_round_rectangle(self, x, y, w, h, r):
        self.round_rectangle(x, y, w, h, r)
        self.fill()

    def stroke_round_rectangle(self, x, y, w, h, r):
        self.round_rectangle(x, y, w, h, r)
        self.stroke()

    ##########
    # super*
    ##########
    def superellipse(self, xc, yc, rx, ry, p):
        for t in frange(0, math.tau, 0.01):
            cos = math.cos(t)
            sin = math.sin(t)
            x = math.pow(math.fabs(cos), 2.0 / p) * rx * sign(cos)
            y = math.pow(math.fabs(sin), 2.0 / p) * ry * sign(sin)
            self.line_to(xc + x, yc + y)
        self.close_path()

    def fill_superellipse(self, xc, yc, rx, ry, p):
        self.superellipse(xc, yc, rx, ry, p)
        self.fill()

    def stroke_superellipse(self, xc, yc, rx, ry, p):
        self.superellipse(xc, yc, rx, ry, p)
        self.stroke()

    def squircle(self, xc, yr, radius):
        self.superellipse(xc, yc, radius, radius, 4)

    def fill_squircle(self, xc, yr, radius):
        self.fill_superellipse(xc, yc, radius, radius, 4)

    def stroke_squircle(self, xc, yr, radius):
        self.stroke_superellipse(xc, yc, radius, radius, 4)

    def superformula(self, x, y, radius, symmetry, n1, n2, n3):
        for t in frange(0, math.tau, 0.01):
            angle = symmetry * t / 4
            term1 = math.pow(math.fabs(math.cos(angle)), n2)
            term2 = math.pow(math.fabs(math.sin(angle)), n3)
            r = math.pow(term1 + term2, -1 / n1) * radius
            self.line_to(x + math.cos(t) * r, y + math.sin(t) * r)
        self.close_path()

    def fill_superformula(self, x, y, radius, symmetry, n1, n2, n3):
        self.superformula(x, y, radius, symmetry, n1, n2, n3)
        self.fill()

    def stroke_superformula(self, x, y, radius, symmetry, n1, n2, n3):
        self.superformula(x, y, radius, symmetry, n1, n2, n3)
        self.stroke()

    ##########
    # star
    ##########
    def star(self, x, y, r0, r1, points, rotation):
        self.save()
        self.translate(x, y)
        self.rotate(rotation)
        for i in range(0, points * 2):
            r = r1
            if i % 2 == 1:
                r = r0
            angle = math.pi / points * i
            self.line_to(math.cos(angle)* r, math.sin(angle) * r)
        self.close_path()
        self.restore()

    def fill_star(self, x, y, r0, r1, points, rotation):
        self.star(x, y, r0, r1, points, rotation)
        self.fill()

    def stroke_star(self, x, y, r0, r1, points, rotation):
        self.star(x, y, r0, r1, points, rotation)
        self.stroke()

    ##########
    # text
    ##########
    def draw_text(self, text, x, y):
        self.save()
        self.translate(x, y)
        self.show_text(text)
        self.fill()
        self.restore()

    ##########
    # triangle
    ##########
    def stroke_triangle_object(self, triangle):
        self.stroke_path(triangle.points(), True)
    
    def fill_triangle_object(self, triangle):
        self.fill_path(triangle.points())
    
