from manim import *
from shapes import MarkedLine
from constructions import parallel_line, equal_angle
from constant_suppliments import HOT_PINK

class Temp(Scene):
    def construct(self):
        point_A = Dot(2*UP)
        line_BC = Line(2*DOWN + 2*LEFT, 2*DOWN + 2*RIGHT)

        self.play(Create(point_A), Create(line_BC)); self.wait()
        print(*self.mobjects)

        parallel_line(self, point_A.get_center(), line_BC, False, 0, 15); self.wait()