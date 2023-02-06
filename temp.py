from manim import *
from shapes import MarkedLine
from constructions import triangle
from constant_suppliments import HOT_PINK

class Temp(Scene):
    def construct(self):
        line_A = Line(2*RIGHT, 4*RIGHT)
        line_B = Line(2*RIGHT, 3.25*RIGHT)
        line_C = Line(2*RIGHT, 3*RIGHT)

        line_base = Line(4*LEFT, ORIGIN)

        self.play(Create(line_A), Create(line_B), Create(line_C), Create(line_base))

        triangle(self, line_base, line_A, line_B, line_C, (1, 2, 3), True, 20); self.wait()