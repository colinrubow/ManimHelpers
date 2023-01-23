from manim import *
from shapes import MarkedLine
from constructions import point_to_line

class Temp(Scene):
    def construct(self):
        point_A = Dot()
        line_BC = Line(start=1*UP + 1*RIGHT, end=-2*UP + 4*RIGHT)
        self.play(Create(point_A), Create(line_BC))
        self.wait()
        point_to_line(self, point_A, line_BC, 1, True, 3)
        self.wait()