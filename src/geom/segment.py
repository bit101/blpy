

class Segment:
    def __init__(self, x0, y0, x1, y1):
        self.x0 = x0
        self.y0 = y0
        self.x1 = x1
        self.y1 = y1

    def __repr__(self):
        return "geom.Segment(x0: {}, y0: {}, x1: {}, y1: {})".format(self.x0, self.y0, self.x1, self.y1)

    @staticmethod
    def from_points(p0, p1):
        return Segment(p0.x, p0.y, p1.x, p1.y)






# // HitSegment returns the point of intersection between this and another segment.
# func (s *Segment) HitSegment(z *Segment) (float64, float64, bool) {
# 	return SegmentOnSegment(s.X0, s.Y0, s.X1, s.Y1, z.X0, z.Y0, z.X1, z.Y1)
# }

# // HitLine returns the point of intersection between this and another line.
# func (s *Segment) HitLine(l *Line) (float64, float64, bool) {
# 	return SegmentOnLine(s.X0, s.Y0, s.X1, s.Y1, l.X0, l.Y0, l.X1, l.Y1)
# }

# // HitRect returns whether this segment intersects a rectangle.
# func (s *Segment) HitRect(r *Rect) bool {
# 	return SegmentOnRect(s.X0, s.Y0, s.X1, s.Y1, r.X, r.Y, r.W, r.H)
# }

# // Length is the length of this segment.
# func (s *Segment) Length() float64 {
# 	return math.Hypot(s.X1-s.X0, s.Y1-s.Y0)
# }

# // ClosestPoint returns the point on this segment closest to another point.
# func (s *Segment) ClosestPoint(p *Point) *Point {
# 	v := VectorBetween(s.X0, s.Y0, p.X, p.Y)
# 	d := VectorBetween(s.X0, s.Y0, s.X1, s.Y1).Normalized()
# 	vs := v.Project(d)
# 	if vs < 0 {
# 		return NewPoint(s.X0, s.Y0)
# 	}
# 	if vs > s.Length() {
# 		return NewPoint(s.X1, s.Y1)
# 	}
# 	t := vs / s.Length()
# 	return NewPoint(blmath.Lerp(t, s.X0, s.X1), blmath.Lerp(t, s.Y0, s.Y1))
# }

# // DistanceTo returns the distance from this segment to another point.
# func (s *Segment) DistanceTo(p *Point) float64 {
# 	return s.ClosestPoint(p).Distance(p)
# }

