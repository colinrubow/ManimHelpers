from manim import *
from shapes import MarkedLine
from constructions import parallel_line, equal_angle
from constant_suppliments import HOT_PINK

class Temp(Scene):
    def construct(self):
        line_A = Line(ORIGIN, UP + RIGHT)
        self.play(Create(line_A)); self.wait()

        self.play(line_A.)