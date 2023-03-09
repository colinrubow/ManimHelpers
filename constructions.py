from manim import *

def equilateral_triangle(s: Scene, base_AB: Line, time: float = 5) -> tuple:
    """will construct an equilateral triangle using Prop 1.1 with 5 operations
    
    Parameters
    ----------
    s :
        The Scene for doing the animations and constructions
    base_AB :
        The Line or Marked Line that makes the base of the triangle.
    time :
        How long the construction will take

    Returns
    -------
    The two lines that make up the rest of the triangle, in counterclockwise order
    """
    dt = time/5
    r = base_AB.get_length()

    circle_BCD = Circle(radius=r, color=WHITE).shift(base_AB.get_start())
    s.play(Create(circle_BCD), run_time=dt)

    circle_ACE = Circle(radius=r, color=WHITE).shift(base_AB.get_end())
    s.play(Create(circle_ACE), run_time=dt)

    line_AC = base_AB.copy().rotate(angle=60*DEGREES, about_point=base_AB.get_start())
    s.play(Create(line_AC), run_time=dt)

    line_BC = base_AB.copy().rotate(angle=-60*DEGREES, about_point=base_AB.get_end())
    s.play(Create(line_BC), run_time=dt)

    s.play(FadeOut(circle_BCD, circle_ACE), run_time=dt)

    return line_BC, Line(line_AC.get_end(), line_AC.get_start())

def point_to_line(s: Scene, point_A: np.ndarray, line_BC: Line, time: float = 11) -> Line:
    """Will construct a line from a point equal to a given line using prop 1.2 with 11 operations
    
    Parameters
    ----------
    s :
        The Scene to draw in
    point :
        The point to draw from
    line :
        The length to match
    time :
        How long the construction should take

    Returns
    -------
    The desired Line
    """
    dt = time/11

    line_AB = Line(start=point_A, end=line_BC.get_start())
    s.play(Create(line_AB), run_time=dt)

    line_AD, line_BD = equilateral_triangle(s, line_AB, time=dt*5)

    line_AE = Line(start=point_A, end=point_A + -1.5*line_AD.get_unit_vector()*line_BC.get_length())
    s.play(Create(line_AE), run_time=dt)

    line_BF = Line(start=line_BC.get_start(), end=line_BC.get_start() + -1.5*line_BD.get_unit_vector()*line_BC.get_length())
    s.play(Create(line_BF), run_time=dt)

    circle_CGH = Circle(radius=line_BC.get_length(), color=WHITE).shift(line_BC.get_start())
    s.play(Create(circle_CGH), run_time=dt)

    circle_GKL = Circle(radius=line_AB.get_length() + line_BC.get_length(), color=WHITE).shift(line_AD.get_end())
    s.play(Create(circle_GKL), run_time=dt)

    line_AL = Line(point_A, point_A + -line_AD.get_unit_vector()*line_BC.get_length())
    s.add(line_AL)
    
    s.play(FadeOut(
        line_AB,
        line_AD,
        line_BD,
        line_AE,
        line_BF,
        circle_CGH,
        circle_GKL
    ), run_time=dt)
    return line_AL

def cut_seperate_line_to_length(s: Scene, greater_line: Line, lesser_line: Line, time: float = 13) -> Point:
    """Will use a circle to cut a given length out of another length using prop 1.3 with 13 operations.
    If greater_line and lesser_line start from the same point then 3 operations.
    
    Parameters
    ----------
    s :
        The scene to draw in
    greater_line :
        A Line longer than the other line
    lesser_line :
        A Line shorter than the other line
    time :
        The amount of time given

    Returns
    -------
    The point where greater_line was cut.
    """
    dt = time / 13

    line_AD = point_to_line(s, greater_line.get_start(), lesser_line, time=dt*11)
    circle_DEF = Circle(radius=line_AD.get_length(), color=WHITE).shift(greater_line.get_start())
    s.play(Create(circle_DEF), run_time=dt)
    point_E = greater_line.get_start() + greater_line.get_unit_vector()*line_AD.get_length()
    s.play(FadeOut(circle_DEF, line_AD), run_time=dt)
    return point_E

def cut_coincident_line_to_length(s: Scene, greater_line: Line, lesser_line: Line, time: float = 2) -> Point:
    """Will cut greater_line to the length of lesser_line assuming they are coincident in 2 operations
    
    Parameters
    ----------
    s :
        The Scene
    greater_line :
        The longer Line :
    lesser_line :
        The shorter Line :
    time :
        How long to take
        
    Returns
    -------
    The Point on the greater line that was cut
    """
    dt = time / 2
    circle = Circle(lesser_line.length(), color=WHITE).shift(greater_line.get_start())
    s.play(Create(circle), run_time=dt)
    point = greater_line.get_start() + greater_line.get_unit_vector()*lesser_line.get_length()
    s.play(FadeOut(circle), run_time=dt)
    return point

def bisect_angle(s: Scene, line_AB: Line, line_CA: Line, time: float = 10) -> Line:
    """Cuts an angle in half. Assumes the line that cuts will start at line_1.get_start() and line_2.get_start()
        and will be in same direction as both lines. Performs using I.9 in 10 operations.
        
    Parameters
    ----------
    s :
        the Scene
    line_AB :
        one of the lines
    line_AC :
        the other line
    time :
        how long the construction should take

    Returns
    -------
    the Line that bisects the angle
    """
    line_AC = Line(line_CA.get_end(), line_CA.get_start())
    dt = time / 10

    point_D = line_AB.get_start() + line_AB.get_unit_vector()*0.5*line_AB.get_length()
    line_AD = Line(line_AB.get_start(), point_D)
    point_E = cut_coincident_line_to_length(s, line_AC, line_AD, dt*2)
    line_DE = Line(point_D, point_E)
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

    line_FD, line_FE = equilateral_triangle(s, Line(point_E, point_D), 5*dt)
    line_AF = Line(line_AB.get_start(), line_FD.get_start())
    s.play(Create(line_AF), run_time=dt)
    s.play(FadeOut(line_DE, line_FD, line_FE), run_time=dt)
    return line_AF

def bisect_line(s: Scene, line_AB: Line, time: float = 16) -> Line:
    """Draws a perpendicular line off of line_AB using I.10 in 16 operations
    
    Parameters
    ----------
    
    s :
        The Scene
    line_AB :
        The line to bisect
    time :
        How long to take
    
    Returns
    -------
    The bisector Line
    """
    dt = time / 16
    line_CA, line_CB = equilateral_triangle(s, line_AB, 5*dt)

    bisector = bisect_angle(
        s,
        line_CA,
        line_CB,
        dt*10
    )
    s.play(FadeOut(line_CA, line_CB), run_time=dt)
    return bisector

def perpendicular_from_point_on_line(s: Scene, line_AB: Line, point_C: Point, time: float = 9) -> Line:
    """From a point on a line, creates a perpendicular line using I.11 in 9 operations
    
    Parameters
    ----------
    s :
        The Scene
    line_AB :
        The line
    point_C :
        The point
    time :
        How long it takes
    
    Returns
    -------
    The perpendicular Line
    """
    dt = time/9

    line_AC = Line(line_AB.get_start(), point_C)
    point_D = Dot(line_AC.get_start() + line_AC.get_unit_vector()*0.5*line_AC.get_length())

    line_CD = Line(point_C, point_D.get_center())
    line_CB = Line(point_C, line_AB.get_end())
    line_CE = cut_coincident_line_to_length(s, line_CB, line_CD, dt*2)

    line_DE = Line(point_D, line_CE.get_end())
    line_FD, line_FE = equilateral_triangle(s, line_DE, 5*dt)

    line_CF = Line(point_C, line_FD.get_start())
    s.play(Create(line_CF), run_time=dt)

    s.play(FadeOut(line_CE, line_FD, line_FE), run_time=dt)

    return line_CF

def perpendicular_from_point_off_line(s: Scene, line_AB: Line, point_C: Point, time: float = 20) -> Line:
    """Given a line and point not on the line, will drop a perpendicular using I.12 in 20 operations
    
    Parameters
    ----------
    s :
        The Scene
    line_AB :
        The line to drop the perpendicular onto
    point_C :
        The point to drop the perpendicular from
    time :
        How long to take

    Returns
    -------
    The perpendicular Line
    """
    dt = time/20

    line_CZ = Line(point_C, line_AB.get_start() + 0.5*line_AB.get_length()*line_AB.get_unit_vector())
    line_CD = Line(point_C, line_CZ.get_end() + line_CZ.get_unit_vector())

    circle_EFG = Circle(line_CD.get_length(), color=WHITE).shift(point_C.get_center())
    s.play(Create(circle_EFG), run_time=dt)

    # find intersection
    m = line_AB.get_slope()
    b = -m*line_AB.get_start()[0] + line_AB.get_start()[1]
    r = line_CD.get_length()
    y_c = point_C.get_center()[1]
    x_c = point_C.get_center()[0]
    zeta = b - y_c

    x_1 = (-2*m*zeta + 2*x_c + np.sqrt((2*m*zeta - 2*x_c)**2 - 4*(m**2 + 1)*(zeta**2 + x_c**2 - r**2)))/2/(m**2 + 1)
    x_2 = (-2*m*zeta + 2*x_c - np.sqrt((2*m*zeta - 2*x_c)**2 - 4*(m**2 + 1)*(zeta**2 + x_c**2 - r**2)))/2/(m**2 + 1)
    y_1 = m*x_1 + b
    y_2 = m*x_2 + b

    line_GE = Line(np.array([x_1, y_1, 0]), np.array([x_2, y_2, 0]))
    
    bisector_GE = bisect_line(s, line_GE, 16*dt)
    point_H = Dot(bisector_GE.get_end())
    s.play(FadeOut(bisector_GE), Create(point_H), run_time=dt)

    line_CH = Line(point_C, point_H.get_center())
    s.play(Create(line_CH), run_time=dt)

    s.play(FadeOut(point_H, circle_EFG), run_time=dt)
    return line_CH

def triangle_from_lines(s: Scene, base_line: Line, line_A: Line, line_B: Line, line_C: Line, time = 47) ->  tuple:
    """Will construct a triangle using I.22 from three given lines on a base line in 47 operations.
    
    Parameters
    ----------
    s :
        the scene
    base_line :
        the line (longer than line_A + line_B + line_C) to build the triangle on
    line_A :
        the first line
    line_B :
        the second line
    line_C :
        the third line
    time :
        how long it takes    
    
    Returns
    -------
    a tuple of the three lines that make up the triangle respective to (line_A, line_B, line_C)
    """
    dt = time/47

    line_DF = cut_seperate_line_to_length(s, base_line, line_A, 13*dt)
    point_F = Dot(line_DF.get_end())
    s.play(FadeOut(line_DF), Create(point_F), run_time=dt)
    line_FE = Line(line_DF.get_end(), base_line.get_end())
    line_FG = cut_seperate_line_to_length(s, line_FE, line_B, 13*dt)
    point_G = Dot(line_FG.get_end())
    s.play(FadeOut(line_FG), Create(point_G), run_time=dt)
    line_GE = Line(line_FG.get_end(), base_line.get_end())
    line_GH = cut_seperate_line_to_length(s, line_GE, line_C, 13*dt)
    point_H = Dot(line_GH.get_end())
    s.play(FadeOut(line_GH), Create(point_H), run_time=dt)

    circle_DKL = Circle(radius=line_DF.get_length(), color=WHITE).shift(point_F.get_center)
    s.play(Create(circle_DKL), run_time=dt)

    circle_KLH = Circle(line_GH.get_length(), color=WHITE).shift(point_G.get_center())
    s.play(Create(circle_KLH), run_time=dt)

    x1 = point_F.get_center()[0]
    x2 = point_G.get_center()[0]
    y1 = point_F.get_center()()[1]
    y2 = point_G.get_center()[1]
    r1 = line_A.get_length()
    r2 = line_B.get_length()

    if y1 - y2 == 0:
        kx = ((r1**2 - r2**2) - (x1**2 - x2**2))/(2*x2 - 2*x1)
        lx = kx
        ky = (2*y2 + np.sqrt(4*y2**2 - 4*(y2**2 + kx**2 - 2*kx*x2 + x2**2 - r2**2)))/2
        ly = (2*y2 - np.sqrt(4*y2**2 - 4*(y2**2 + kx**2 - 2*kx*x2 + x2**2 - r2**2)))/2
    else:
        m = (x2 - x1)/(y1 - y2)
        b = -1/2/(y1 - y2)*((r1**2 - r2**2) - (x1**2 - x2**2) - (y1**2 - y2**2))
        A = 1 + m**2
        B = -2*x1 + 2*b*m - 2*m*y1
        C = x1**2 + b**2 - 2*b*y1 +  y1**2 - r1**2
        kx = (-B + np.sqrt(B**2 - 4*A*C))/2/A
        lx = (-B - np.sqrt(B**2 - 4*A*C))/2/A
        ky = m*kx + b
        ly = m*lx + b
    
    line_KF = Line(np.array([kx, ky, 0]), point_F.get_center())
    s.play(Create(line_KF), run_time=dt)

    line_KG = Line(np.array([kx, ky, 0]), point_G.get_center())
    s.play(Create(line_KG), run_time=dt)

    s.play(FadeOut(circle_KLH, circle_DKL, point_H, point_G, point_F), run_time=dt)

    return line_KF, line_FG, Line(line_KG.get_end(), line_KG.get_start())
    
def equal_angle(s: Scene, line_AB: Line, point_A: np.ndarray, angle: tuple, time: float = 64) -> Line:
    """will construct an angle on a point on a line equal to a the angle of angle using I.23 in 64 operations

    Parameters
    ----------
    s :
        The Scene
    line_AB :
        The line to construct the angle on
    point_A :
        The point to construct the angle on
    angle :
        A tuple of two lines forming an angle. Assumes counterclockwise order
    time :
        how long it takes

    Returns
    -------
    The line that makes the angle ending on A
    """
    dt = time/64
    line_CD, line_CE = angle
    line_DE = Line(line_CD.get_end(), line_CE.get_end())
    s.play(Create(line_DE), run_time=dt)

    line_A = line_CD
    line_B = line_CE
    line_C = line_DE

    line_AB = Line(point_A, line_AB.get_unit_vector()*1.1*(line_C.get_length() + line_B.get_length()))
    line_AZ = Line(point_A, line_AB.get_unit_vector()*-1.1*line_A.get_length())
    s.play(Create(line_AZ), run_time=dt)

    line_AY = cut_seperate_line_to_length(s, line_AZ, line_A, 13*dt)
    point_Y = Dot(line_AY.get_end())
    s.play(FadeOut(line_AY), Create(point_Y), run_time=dt)

    line_YB = Line(point_Y.get_center(), line_AB.get_end())
    line_FA, line_AG, line_FG = triangle_from_lines(s, line_YB, line_A, line_B, line_C, 47*dt)

    s.play(FadeOut(line_DE, line_AZ, point_Y, line_FG, line_AG), run_time=dt)

    return line_FA

def parallel_line(s: Scene, point_A: np.ndarray, line_BC: Line, time: float = 68) -> Line:
    """Will construct a line parallel to line_BC, through point_A using I.31 in 68 operations
    
    Parameters
    ----------
    s :
        The scene
    point_A :
        The point to draw the parallel line through
    line_BC :
        The direction the parallel line goes in
    to_point :
        The point to draw the parallel line to
    time :
        How long to take

    Returns
    -------
    The Line that is parallel
    """
    dt = time / 68

    point_D = Dot(line_BC.get_start() + line_BC.get_unit_vector()*0.25*line_BC.get_length())
    s.play(Create(point_D), run_time=dt)

    line_AD = Line(point_A, point_D.get_center())
    s.play(Create(line_AD), run_time=dt)

    line_CD = Line(line_BC.get_end(), point_D.get_center())
    line_DA = Line(line_AD.get_end(), line_AD.get_start())
    line_EA = equal_angle(s, line_AD, point_A, (line_CD, line_DA), 64*dt)

    line_AF = Line(point_A, point_A + line_EA.get_unit_vector()*line_EA.get_length())
    s.play(Create(line_AF), run_time=dt)
    line_EF = Line(line_EA.get_start(), line_AF.get_end())

    s.add(line_EF)
    s.remove(line_AF, line_EA)

    s.play(FadeOut(line_AD, point_D), run_time=dt)
    return line_EF

def parallelogram_from_angle_and_triangle(s: Scene, angle: tuple, triangle: tuple, time: float = 219) -> tuple:
    """Constructs a prallelogram on an angle equal to the given triangle using I.42 in 219 operations.
        Assumes that half the third line of triangle will be the base of the parallelogram
    
    Parameters
    ----------
    s :
        The Scene
    angle :
        A tuple containing the two lines assuming counterclockwise order
    triangle :
        A tuple of three lines containing the triangle assuming counterclockwise order
    time :
        how long it takes
    
    Returns
    -------
    a tuple of the four lines making the parallelogram
    """
    dt = time / 219

    line_AB = triangle[0]
    line_AC = triangle[1]
    line_BC = triangle[2]
    line_BC_bisector = bisect_line(s, line_BC, dt*16)
    point_E = Dot(line_BC_bisector.get_end())
    s.play(Create(point_E), FadeOut(line_BC_bisector), run_time=dt)
    
    line_CE = Line(line_AC.get_end(), point_E.get_center())
    s.add(line_CE)
    line_EF = equal_angle(s, line_CE, line_CE.get_end(), angle, 64*dt)

    line_AG = parallel_line(s, line_AB.get_start(), line_BC, 68*dt)

    line_CG = parallel_line(s, line_BC.get_end(), line_EF, 68*dt)

    point_G = line_intersection([line_AG.get_start(), line_AG.get_end()], [line_CG.get_start(), line_CG.get_end()])
    point_F = line_intersection([line_AG.get_start(), line_AG.get_end()], [line_EF.get_start(), line_EF.get_end()])

    s.play(
        ReplacementTransform(line_AG, Line(line_AG.get_start(), point_G)),
        ReplacementTransform(line_EF, Line(line_EF.get_start(), point_F)),
        ReplacementTransform(line_CG, Line(line_CG.get_start(), point_G)),
        run_time=dt)
    
    line_GF = Line(point_G, point_F)
    s.add(line_GF)

    line_EC = Line(line_CE.get_end(), line_CE.get_start())

    s.play(FadeOut(point_E), run_time=dt)

    return line_EC, line_CG, line_GF, Line(line_EF.get_end(), line_EF.get_start())

def parallelogram_from_angle_and_triangle_on_line(s: Scene, angle: tuple, triangle: tuple, line_AB: Line, time: float = 409) -> tuple:
    """Will construct a parallelogram from an angle and triangle on a given line using I.44 in 409 operations
    
    Parameters
    ----------
    s :
        The Scene
    angle :
        A tuple of two lines in counterclockwise order
    triangle :
        A tuple of three lines making a triangle in counterclockwise order
    line_AB :
        The line to build the parallelogram on
    time :
        how long to take
    
    Returns
    -------
    A tuple of the three remaining lines that make the parallelogram
    """
    dt = time / 409

    line_A_prime_E_prime = Line(line_AB.get_start() - line_AB.get_unit_vector()*triangle[0].get_length(), line_AB.get_end() + line_AB.get_unit_vector()*(triangle[1].get_length() + triangle[2].get_length()))
    s.play(Create(line_A_prime_E_prime), run_time=dt)
    line_A_prime, line_B_prime, line_C_prime = triangle_from_lines(s, line_A_prime_E_prime, triangle[0], triangle[1], triangle[2], 47*dt)

    line_BE, line_EF, line_GF, line_BG = parallelogram_from_angle_and_triangle(s, angle, (line_A_prime, line_B_prime, line_C_prime), 219*dt)

    s.play(FadeOut(line_A_prime, line_B_prime, line_C_prime, line_A_prime_E_prime), run_time=dt)

    line_AH = parallel_line(s, line_AB.get_start(), line_EF, 68*dt)

    point_H = line_intersection([line_AH.get_start(), line_AH.get_end()], [line_GF.get_start(), line_GF.get_end()])

    line_GH = Line(line_BG.get_end(), point_H)
    s.play(Create(line_GH), ReplacementTransform(line_AH, Line(line_AH.get_start(), point_H)), run_time=dt)

    line_HB = Line(point_H, line_AB.get_end())
    s.play(Create(line_HB), run_time=dt)

    point_K = line_intersection([line_HB.get_start(), line_HB.get_end()], [line_EF.get_start(), line_EF.get_end()])

    line_KM = parallel_line(s, point_K, line_GF, 68*dt)

    point_M = line_intersection([line_KM.get_start(), line_KM.get_end()], [line_BG.get_start(), line_BG.get_end()])
    line_MB = Line(point_M, line_AB.get_end())

    s.play(ReplacementTransform(line_KM, Line(line_KM.get_start(), point_M)), Create(line_BM), run_time=dt)

    point_L = line_intersection([line_KM.get_start(), line_KM.get_end()], [line_AH.get_start(), line_AH.get_end()])

    line_LM = Line(point_L, line_MB.get_start())
    line_AL = Line(line_AB.get_start(), point_L)

    s.play(Create(line_LM), Create(line_AL), run_time=dt)

    s.play(FadeOut(line_KM, line_HB, line_GH, line_AH, line_BE, line_EF, line_GF, line_BG), run_time=dt)

    return line_AL, line_LM, line_MB

def parallelogram_from_angle_and_rectilineal_figure(s: Scene, angle: tuple, rect_fig: tuple, line_KF: Line, time: float = 820) -> tuple:
    """Will construct a parallelogram from an angle and rectilineal figure from I.45 in 820 operations
    
    Parameters
    ----------
    s :
        The Scene
    angle : 
        a tuple of two lines in counterclockwise order
    rect_fig :
        A tuple of four lines making a rectilineal figure in counterclockwise order
    line_KF :
        The line to draw the parallelogram on
    time :
        The time is takes
    
    Returns
    -------
    a tuple of the other three Lines that make up the parallelogram in counterclockwise order
    """

    dt = time / 820

    line_AB, line_BC, line_CD, line_DA = rect_fig

    line_DB = Line(line_CD.get_end(), line_BC.get_start())
    s.play(Create(line_DB), run_time=dt)

    line_KH, line_GH, line_FG = parallelogram_from_angle_and_triangle_on_line(s, angle, (line_AB, line_DB, line_DA), line_KF, 409*dt)

    line_HM, line_LM, line_GL = parallelogram_from_angle_and_triangle_on_line(s, angle, (line_DB, line_BC, line_CD), line_GH, 409*dt)

    line_KM = Line(line_KH.get_start(), line_HM.get_end())
    line_FL = Line(line_KF.get_end(), line_LM.get_start())
    s.add(line_KM, line_FL)

    s.play(FadeOut(line_GH, line_DB, line_FG, line_GL, line_KH, line_HM), run_time=dt)

    return line_KM, Line(line_LM.get_end(), line_LM.get_start()), Line(line_FL.get_end(), line_FL.get_start())

def square_on_line(s: Scene, line_AB, time: float = 150) -> tuple:
    """Will construct a square on a Line using I.46 in _ operations
    
    Parameters
    ----------
    s :
        The Scene
    line_AB :
        The first line of the square
    time :
        How long it takes
    
    Returns
    -------
    a tuple of the three remaining lines of the square in clockwise order
    """

    dt = time / 150

    line_AC = perpendicular_from_point_on_line(s, line_AB, line_AB.get_start(), 9*dt)

    point_D = Dot(cut_coincident_line_to_length(s, line_AC, line_AB, 2*dt))
    s.play(Create(point_D), run_time=dt)

    line_AD = Line(line_AB.get_start(), point_D.get_center())

    line_DE = parallel_line(s, line_AD.get_end(), line_AB, 68*dt)

    line_BE = parallel_line(s, line_AB.get_end(), line_AD, 68*dt)

    point_E = line_intersection([line_DE.get_start(), line_DE.get_end()], [line_BE.get_start(), line_BE.get_end()])

    s.play(
        ReplacementTransform(line_DE, Line(line_DE.get_start(), point_E)),
        ReplacementTransform(line_BE, Line(line_BE.get_start(), point_E)),
        run_time=dt
    )

    s.play(FadeOut(line_AC, point_D), run_time=dt)

    return line_BE, Line(line_DE.get_end(), line_DE.get_start()), Line(line_AD.get_end(), line_AD.get_start())