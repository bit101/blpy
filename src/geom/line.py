


class Line:
    def __init__(self, x0, y0, x1, y1):
        self.x0 = x0
        self.y0 = y0
        self.x1 = x1
        self.y1 = y1
        
    def __repr__(self):
        return "geom.Line(x0: {}, y0: {}, x1: {}, y1: {})".format(self.x0, self.y0, self.x1, self.y1)

    @staticmethod
    def from_points(p0, p1):
        return Line(p0.x, p0.y, p1.x, p1.y)






# // HitSegment reports the point of intersection of a line and a line segment.
# func (l *Line) HitSegment(s *Segment) (float64, float64, bool) {
# 	return SegmentOnSegment(s.X0, s.Y0, s.X1, s.Y1, l.X0, l.Y0, l.X1, l.Y1)
# }

# // HitLine reports the point of intersection of two lines.
# func (l *Line) HitLine(m *Line) (float64, float64, bool) {
# 	return LineOnLine(l.X0, l.Y0, l.X1, l.Y1, m.X0, m.Y0, m.X1, m.Y1)
# }

# // ClosestPoint reports the point on a line closest to another given point.
# func (l *Line) ClosestPoint(p *Point) *Point {

# 	v := VectorBetween(l.X0, l.Y0, p.X, p.Y)
# 	d := VectorBetween(l.X0, l.Y0, l.X1, l.Y1).Normalized()
# 	vs := v.Project(d)
# 	t := vs / math.Hypot(l.X1-l.X0, l.Y1-l.Y0)
# 	return NewPoint(blmath.Lerp(t, l.X0, l.X1), blmath.Lerp(t, l.Y0, l.Y1))
# }

# // DistanceTo reports the distance from a given point to this line.
# func (l *Line) DistanceTo(p *Point) float64 {
# 	return l.ClosestPoint(p).Distance(p)
# }

# // Perpendicular returns a line that is perpendicular to the line and crosses through the given point.
# func (l *Line) Perpendicular(p *Point) *Line {
# 	dx := l.X1 - l.X0
# 	dy := l.Y1 - l.Y0
# 	return NewLine(p.X, p.Y, p.X-dy, p.Y+dx)
# }
