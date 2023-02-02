from manim import *
from shapes import MarkedLine
from constructions import bisect_line
from constant_suppliments import HOT_PINK

class Temp(Scene):
    def construct(self):
        line_AB = Line(3*LEFT + 2*DOWN, 2*RIGHT)
        self.play(Create(line_AB)); self.wait()

        bisect_line(self, line_AB, time=5); self.wait()