from manim import *
from shapes import MarkedLine
from constructions import equal_angle
from constant_suppliments import HOT_PINK

class Temp(Scene):
    def construct(self):
        line_AB = Line(RIGHT, 2*RIGHT + UP)
        line_AC = Line(RIGHT, 2*RIGHT + DOWN)

        line_base = Line(4*LEFT, ORIGIN)

        self.play(Create(line_AB), Create(line_AC), Create(line_base))

        equal_angle(self, line_base, line_base.get_start(), (line_AB, line_AC), None, True, 20); self.wait()