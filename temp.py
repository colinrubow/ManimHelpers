from manim import *
from shapes import MarkedLine
from constructions import perpendicular_from_point_off_line
from constant_suppliments import HOT_PINK

class Temp(Scene):
    def construct(self):
        line_AB = Line(3*LEFT + 2*DOWN, 2*RIGHT)
        point_C = Dot(-1*UP + 1*RIGHT)
        self.play(Create(line_AB), Create(point_C)); self.wait()
        perpendicular_from_point_off_line(self, line_AB, point_C, 5)