from manim import *
from ManimHelpers.shapes import MarkedLine

def equilateral_triangle(s: Scene, base_AB: Line, cong_num: int = 0, positive_solution: bool = True, time: float = 3) -> VGroup:
    """will construct an equilateral triangle using Prop 1.1 with 6 operations
    
    Parameters
    ----------
    s :
        The Scene for doing the animations and constructions
    base_AB :
        The Line or Marked Line that makes the base of the triangle
    cong_num :
        The order of indicator for congruence identification
    positive_solution :
        Whether to choose the up or down intersection to create the triangle
    time :
        How long the construction will take

    Returns
    -------
    A VGroup of the three MarkedLines that make up the equilateral triangle
    """
    l = base_AB.get_length()

    circle_BCD = Circle(radius=l, color=WHITE).shift(base_AB.start)
    circle_ACE = Circle(radius=l, color=WHITE).shift(base_AB.end)

    line_CA = base_AB.copy().rotate(
        angle=60*DEGREES,
        about_point=base_AB.get_start()
        ) if positive_solution else base_AB.copy().rotate(
            angle=-60*DEGREES,
            about_point=base_AB.get_start()
            )
    line_CB = base_AB.copy().rotate(
        angle=-60*DEGREES,
        about_point=base_AB.get_end()
        ) if positive_solution else base_AB.copy().rotate(
            angle=60*DEGREES,
            about_point=base_AB.get_end()
            )

    line_CA = MarkedLine(line=line_CA, cong_mark_num=cong_num)
    line_CB = MarkedLine(line=line_CB, cong_mark_num=cong_num)
    line_AB = MarkedLine(line=Line(start=base_AB.get_start(), end=base_AB.get_end()), cong_mark_num=cong_num)

    # construct
    dt = time/6
    s.play(Create(circle_BCD, run_time=dt))
    s.play(Create(circle_ACE, run_time=dt))
    s.play(Create(line_CA, run_time=dt))
    s.play(Create(line_CB, run_time=dt))
    s.play(Create(line_AB, run_time=dt))
    s.remove(base_AB)
    s.play(FadeOut(circle_BCD, run_time=dt), FadeOut(circle_ACE, run_time=dt))

    return VGroup(
        line_CA,
        line_CB,
        line_AB
    )

def point_to_line(s: Scene, point_A: Dot, line_BC: Line, cong_num: int = 0, positive_solution: bool = True, time: float = 3) -> MarkedLine:
    """Will construct a line from a point equal to a give line using prop 1.2 with 12 operations
    
    Parameters
    ----------
    s :
        The Scene to draw in
    point :
        The point to draw from
    line :
        The length to match
    cong_num :
        The congruence marker type
    positive_solution :
        The parity of the construction
    time :
        How long the construction should take

    Returns
    -------
    The desired MarkedLine
    """
    dt = time/12
    line_AB = Line(start=point_A.get_center(), end=line_BC.get_start())
    s.play(Create(line_AB, run_time=dt))
    triangle_ABD = equilateral_triangle(s, line_AB, cong_num=0, positive_solution=positive_solution, time=dt*6)
    line_AE = Line(start=point_A.get_center(), end=point_A.get_center() + -2*triangle_ABD[0].get_unit_vector()*line_BC.get_length())
    s.play(Create(line_AE, run_time=dt))
    line_BF = Line(start=line_BC.get_start(), end=line_BC.get_start() + 2*triangle_ABD[1].get_unit_vector()*line_BC.get_length())
    s.play(Create(line_BF, run_time=dt))
    circle_CGH = Circle(radius=line_BC.get_length(), color=WHITE).shift(line_BC.get_start())
    s.play(Create(circle_CGH, run_time=dt))
    circle_GKL = Circle(radius=line_AB.get_length() + line_BC.get_length(), color=WHITE).shift(triangle_ABD[0].get_end())
    s.play(Create(circle_GKL, run_time=dt))
    mline_AL = MarkedLine(
        Line(start=point_A.get_center(), end=point_A.get_center() + -triangle_ABD[0].get_unit_vector()*(line_BC.get_length())),
        cong_mark_num = cong_num
    )
    s.play(Create(mline_AL))
    s.play(FadeOut(
        line_AB,
        triangle_ABD,
        line_BF,
        line_AE,
        circle_CGH,
        circle_GKL
    ))
    return mline_AL