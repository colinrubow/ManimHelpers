from manim import *
from ManimHelpers.shapes import MarkedLine

def equilateral_triangle(s: Scene, base_AB: Line, cong_num: int = 0, positive_solution: bool = True, time: float = 6) -> VGroup:
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

def point_to_line(s: Scene, point_A: np.ndarray, line_BC: Line, cong_num: int = 0, positive_solution: bool = True, time: float = 3) -> MarkedLine:
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
    line_AB = Line(start=point_A, end=line_BC.get_start())
    s.play(Create(line_AB, run_time=dt))
    triangle_ABD = equilateral_triangle(s, line_AB, cong_num=0, positive_solution=positive_solution, time=dt*6)
    line_AE = Line(start=point_A, end=point_A + -2*triangle_ABD[0].get_unit_vector()*line_BC.get_length())
    s.play(Create(line_AE, run_time=dt))
    line_BF = Line(start=line_BC.get_start(), end=line_BC.get_start() + 2*triangle_ABD[1].get_unit_vector()*line_BC.get_length())
    s.play(Create(line_BF, run_time=dt))
    circle_CGH = Circle(radius=line_BC.get_length(), color=WHITE).shift(line_BC.get_start())
    s.play(Create(circle_CGH, run_time=dt))
    circle_GKL = Circle(radius=line_AB.get_length() + line_BC.get_length(), color=WHITE).shift(triangle_ABD[0].get_end())
    s.play(Create(circle_GKL, run_time=dt))
    mline_AL = MarkedLine(
        Line(start=point_A, end=point_A + -triangle_ABD[0].get_unit_vector()*(line_BC.get_length())),
        cong_mark_num = cong_num
    )
    s.play(Create(mline_AL))
    s.play(FadeOut(
        line_AB,
        triangle_ABD,
        line_BF,
        line_AE,
        circle_CGH,
        circle_GKL,
        run_time=dt
    ))
    return mline_AL

def cut_line_to_length(s: Scene, greater_line: Line, lesser_line: Line, cong_num: int = 0, time: float = 3) -> tuple:
    """Will use a circle to cut a given length out of another length using prop 1.3 with 14 operations.
    If greater_line and lesser_line start from the same point then 3 operations.
    
    Parameters
    ----------
    s :
        The scene to draw in
    greater_line :
        A Line longer than the other line
    lesser_line :
        A Line shorter than the other line
    cong_num :
        The congruence symbol
    time :
        The amount of time given

    Returns
    -------
    A tuple of the mline that was cut off and the dot at the end of the mline.
    """
    if False not in np.isclose(greater_line.get_start(), lesser_line.get_start()):
        dt = time/3
        circle_DEF = Circle(radius=lesser_line.get_length(), color=WHITE).shift(greater_line.get_start())
        s.play(Create(circle_DEF, run_time=dt))
        dot = Dot(greater_line.get_start() + greater_line.get_unit_vector()*lesser_line.get_length())
        s.play(Create(dot), run_time=dt)
        s.play(FadeOut(circle_DEF, run_time=dt))
        return (MarkedLine(Line(start=greater_line.get_start(), end=greater_line.get_start() + greater_line.get_unit_vector()*lesser_line.get_length()), cong_mark_num=cong_num), dot)
    dt = time / 14
    mline_AD = point_to_line(s, greater_line.get_start(), lesser_line, time=dt*12)
    circle_DEF = Circle(radius=mline_AD.get_length(), color=WHITE).shift(greater_line.get_start())
    s.play(Create(circle_DEF, run_time=dt))
    dot = Dot(greater_line.get_start() + greater_line.get_unit_vector()*mline_AD.get_length())
    s.play(Create(dot), run_time=dt)
    s.play(FadeOut(circle_DEF, mline_AD, run_time=dt))
    return (MarkedLine(Line(start=greater_line.get_start(), end=greater_line.get_start() + greater_line.get_unit_vector()*mline_AD.get_length()), cong_mark_num=cong_num), dot)

def isosceles_triangle(s: Scene, point_A: np.ndarray, length: float, start_angle: float, end_angle: float, cong_num: tuple = (0, 0), time: float = 3) -> VGroup:
    """Will construct an isosceles triangle where side AB will be equal to side AC.
    Side AB will start with an orientation equal to start_angle and end_angle is the angle between side AB and AC.
    Will construct in 5 operations.
    
    Parameters
    ----------
    s :
        The canvas
    point_A :
        The vertex of the triangle
    length :
        The length of line AB
    start_angle :
        The angle of line AB
    end_angle :
        The angle between line AB and line AC
    cong_num :
        The congruence indicator type where a in (a, b) indicate the equal side congruence type and b is the base
    time :
        the time to complete the construction
    
    Returns
    -------
    A VGroup made of three MarkedLines
    """

    dt = time/5

    circle_ABC = Circle(radius=length, color=WHITE).shift(point_A)
    s.play(Create(circle_ABC, run_time=dt))

    mline_AB = MarkedLine(
        Line(start=point_A, end=point_A + RIGHT*length).rotate(angle=start_angle, about_point=point_A),
        cong_mark_num=cong_num[0]
    )
    s.play(Create(mline_AB, run_time=dt))

    mline_AC = MarkedLine(
        Line(start=point_A, end=point_A + RIGHT*length).rotate(angle=start_angle + end_angle, about_point=point_A),
        cong_mark_num=cong_num[0]
    )
    s.play(Create(mline_AC, run_time=dt))

    mline_BC = MarkedLine(
        Line(start=mline_AB.get_end(), end=mline_AC.get_end()),
        cong_mark_num=cong_num[1]
    )
    s.play(Create(mline_BC), run_time=dt)
    
    s.play(FadeOut(circle_ABC), run_time=dt)

    return VGroup(
        mline_AB,
        mline_AC,
        mline_BC
    )

def bisect_angle(s: Scene, line_AB: Line, line_AC: Line, l: float = 1, time: float = 13) -> Line:
    """Cuts an angle in half. Assumes the line that cuts will start at line_1.get_start() and line_2.get_start()
        and will be in same direction as both lines. Performs using I.9 in 13 operations.
        
    Parameters
    ----------
    s :
        the Scene
    line_AB :
        one of the lines
    line_AC :
        the other line
    l :
        the length of the bisector
    time :
        how long the construction should take

    Returns
    -------
    the Line that bisects the angle
    """
    dt = time / 13
    point_D = Dot(line_AB.get_start() + line_AB.get_unit_vector()*0.5*line_AB.get_length())
    s.play(Create(point_D), run_time=dt)
    line_AD = Line(line_AB.get_start(), point_D.get_center())
    mline_AE, point_E = cut_line_to_length(s, line_AC, line_AD, cong_num=0, time=dt*3)
    line_DE = Line(point_D.get_center(), point_E.get_center())
    s.play(Create(line_DE), run_time=dt)
    angle_AB = line_AB.get_angle()
    if angle_AB < 0: angle_AB = 2*PI + angle_AB
    angle_AC = line_AC.get_angle()
    if angle_AC < 0: angle_AC = 2*PI + angle_AC
    polarity = -1
    if angle_AB < PI:
            if 0 <= angle_AC < angle_AB or 2*PI > angle_AC > angle_AB + PI:
                polarity = True
            else:
                polarity = False
    else:
        if angle_AB - PI < angle_AC < angle_AB:
            polarity = True
        else:
            polarity = False
    if polarity == -1:
        raise AssertionError("bisect line still has issues")

    triangle_DEF = equilateral_triangle(s, line_DE, cong_num=0, positive_solution=polarity, time=dt*6)
    line_AF = Line(line_AB.get_start(), triangle_DEF[0].get_end())
    line_AF_prime = Line(line_AF.get_start(), line_AF.get_start() + line_AF.get_unit_vector()*l)
    s.play(Create(line_AF_prime), run_time=dt)
    s.play(FadeOut(point_D, point_E, line_DE, triangle_DEF), run_time=dt)
    return line_AF_prime

def bisect_line(s: Scene, line_AB: Line, positive_solution: bool = True, time: float = 20) -> Line:
    """Draws a perpendicular line off of line_AB using I.10 in 20 operations
    
    Parameters
    ----------
    
    s :
        The Scene
    line_AB :
        The line to bisect
    positive_solution :
        The direction to draw the bisector from
    time :
        How long to take
    
    Returns
    -------
    The bisecting Line
    """
    dt = time / 20
    triangle_ABC = equilateral_triangle(s, line_AB, 0, positive_solution, dt*6)
    bisector = bisect_angle(
        s,
        Line(triangle_ABC[0].get_end(), triangle_ABC[0].get_start()),
        triangle_ABC[1],
        np.sqrt(line_AB.get_length()**2 - (line_AB.get_length()/2)**2),
        dt*13
    )
    s.play(FadeOut(triangle_ABC[0], triangle_ABC[1]))
    return bisector
