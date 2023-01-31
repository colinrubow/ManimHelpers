from manim import *
from shapes import MarkedLine
from constructions import perpendicular_from_point_on_line
from constant_suppliments import HOT_PINK

class Temp(Scene):
    def construct(self):
        line_AB = Line(-3*RIGHT, 2*UP + 2*LEFT)
        point_C = Dot(line_AB.get_start() + 0.5*line_AB.get_unit_vector()*line_AB.get_length())
        self.play(Create(line_AB), Create(point_C))
        self.wait()

        perpendicular_from_point_on_line(self, line_AB, point_C, 2, True, 12)
        self.wait()