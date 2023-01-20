from manim import *
from shapes import MarkedLine

class Temp(Scene):
    def construct(self):
        line = Line()
        self.play(Create(line))
        self.wait()
        self.play(Transform(line, MarkedLine(cong_mark_num=6, parrel_mark_num=10)))
        self.wait()