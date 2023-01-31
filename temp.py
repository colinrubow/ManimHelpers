from manim import *
from shapes import MarkedLine
from constructions import bisect_line
from constant_suppliments import HOT_PINK

class Temp(Scene):
    def construct(self):
        line_AB = Line(ORIGIN, 2*UP + 2*LEFT)
        self.play(Create(line_AB))
        self.wait()
        bisect_line(self, line_AB, False, 19)