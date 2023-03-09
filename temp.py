from manim import *
from shapes import MarkedLine
from constructions import parallel_line, equal_angle
from constant_suppliments import HOT_PINK

class Temp(Scene):
    def construct(self):
        letter_1 = VGroup(
            Line(ORIGIN, UP),
            Line(UP, 0.5*RIGHT + 0.5*UP),
            Line(0.5*RIGHT + 0.5*UP, RIGHT + UP),
            Line(RIGHT + UP, RIGHT)
        )
        letter_2 = letter_1.copy().shift(2*RIGHT).rotate(TAU/2)
        letter_3 = letter_1.copy().shift(4*RIGHT).rotate(TAU/2)
        self.add(letter_1)
        self.add(letter_2)
        self.add(letter_3)