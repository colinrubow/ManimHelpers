from manim import *
from ManimHelpers.constant_suppliments import *

class MarkedLine(VMobject):
    """A line with ticks to represent congruency and arrows to represent parrelelism
    
    Parameters
    ----------
    start :
        where the line starts
    end :
        where the line ends
    cong_mark_num :
        the number of ticks on the line
    parrel_mark_num :
        the number of arrows on the line
    length :
        the length of the marks
    mark_origin :
        where the marks are centered on. 0.5 is the middle
    mark_layout_width :
        the percentage of the line of which the marks are to be layed out on
    **kwargs :
        the parameters to pass on
    """

    def __init__(self, line: Line, cong_mark_num: int = 0, parrel_mark_num: int = 0, length: float = 0.125, mark_origin: float = 0.5, mark_layout_width: float = 0.25, **kwargs):
        self.cong_mark_num = cong_mark_num
        self.parrel_mark_num = parrel_mark_num
        self.mark_length = length
        self.mark_origin = mark_origin
        self.mark_layout_width = mark_layout_width
        self.line = line.copy()

        VMobject.__init__(self, **kwargs)

        self.add(self.line)
        angle_main_line = self.line.get_angle()

        # number of marks
        num_ten_ticks = int(cong_mark_num/10)
        num_five_ticks = int((cong_mark_num - 10*num_ten_ticks)/5)
        num_one_ticks = cong_mark_num - 10*num_ten_ticks - 5*num_five_ticks
        
        num_ten_arrows = int(parrel_mark_num/10)
        num_five_arrows = int((parrel_mark_num - 10*num_ten_arrows)/5)
        num_one_arrows = parrel_mark_num - 10*num_ten_arrows - 5*num_five_arrows

        num_marks = num_ten_ticks + num_five_ticks + num_one_ticks + num_ten_arrows + num_five_arrows + num_one_arrows

        if num_marks != 0:
            # the percentage of length between marks
            mark_spacing = mark_layout_width / num_marks

            # start + start_to_next_mark = location of first mark at first
            start = self.line.get_start()
            end = self.line.get_end()
            start_to_next_mark = (end - start)*(mark_origin - mark_spacing*(num_marks-1)/2)
            mark_width = 3
            for i in range(num_ten_ticks):
                self.add(Line(
                    start = start + start_to_next_mark + self.rot(PI/2 + angle_main_line)@(length*RIGHT),
                    end = start + start_to_next_mark + self.rot(-PI/2 + angle_main_line)@(length*RIGHT),
                    stroke_width = mark_width
                ))
                self.add(Line(
                    start = start + start_to_next_mark + self.rot(PI/3 + angle_main_line)@(length*RIGHT),
                    end = start + start_to_next_mark + self.rot(-PI/2 - PI/6 + angle_main_line)@(length*RIGHT),
                    stroke_width = mark_width
                ))
                self.add(Line(
                    start = start + start_to_next_mark + self.rot(PI/2 + PI/6 + angle_main_line)@(length*RIGHT),
                    end = start + start_to_next_mark + self.rot(-PI/3 + angle_main_line)@(length*RIGHT),
                    stroke_width = mark_width
                ))
                start_to_next_mark += mark_spacing*(end - start)
            for i in range(num_five_ticks):
                self.add(Line(
                    start = start + start_to_next_mark + self.rot(PI/3 + angle_main_line)@(length*RIGHT),
                    end = start + start_to_next_mark + self.rot(-PI/2 - PI/6 + angle_main_line)@(length*RIGHT),
                    stroke_width = mark_width
                ))
                self.add(Line(
                    start = start + start_to_next_mark + self.rot(PI/2 + PI/6 + angle_main_line)@(length*RIGHT),
                    end = start + start_to_next_mark + self.rot(-PI/3 + angle_main_line)@(length*RIGHT),
                    stroke_width = mark_width
                ))
                start_to_next_mark += mark_spacing*(end - start)
            for i in range(num_one_ticks):
                self.add(Line(
                    start = start + start_to_next_mark + self.rot(PI/2 + angle_main_line)@(length*RIGHT),
                    end = start + start_to_next_mark + self.rot(-PI/2 + angle_main_line)@(length*RIGHT),
                    stroke_width = mark_width
                ))
                start_to_next_mark += mark_spacing*(end - start)
            for i in range(num_ten_arrows):
                self.add(Line(
                    start = start + start_to_next_mark + self.rot(PI/2 + angle_main_line)@(length*RIGHT),
                    end = start + start_to_next_mark + self.rot(-PI/2 + angle_main_line)@(length*RIGHT),
                    stroke_width = mark_width
                ))
                self.add(Line(
                    start = start + start_to_next_mark,
                    end = start + start_to_next_mark + self.rot(PI/2 + PI/3 + angle_main_line)@(length*RIGHT),
                    stroke_width = mark_width
                ))
                self.add(Line(
                    start = start + start_to_next_mark,
                    end = start + start_to_next_mark + self.rot(-PI/2 - PI/3 + angle_main_line)@(length*RIGHT),
                    stroke_width = mark_width
                ))
                self.add(Line(
                    start = start + start_to_next_mark,
                    end = start + start_to_next_mark + self.rot(PI/2 + PI/6 + angle_main_line)@(length*RIGHT),
                    stroke_width = mark_width
                ))
                self.add(Line(
                    start = start + start_to_next_mark,
                    end = start + start_to_next_mark + self.rot(-PI/2 - PI/6 + angle_main_line)@(length*RIGHT),
                    stroke_width = mark_width
                ))
                start_to_next_mark += mark_spacing*(end - start)
            for i in range(num_five_arrows):
                self.add(Line(
                    start = start + start_to_next_mark,
                    end = start + start_to_next_mark + self.rot(PI/2 + PI/3 + angle_main_line)@(length*RIGHT),
                    stroke_width = mark_width
                ))
                self.add(Line(
                    start = start + start_to_next_mark,
                    end = start + start_to_next_mark + self.rot(-PI/2 - PI/3 + angle_main_line)@(length*RIGHT),
                    stroke_width = mark_width
                ))
                self.add(Line(
                    start = start + start_to_next_mark,
                    end = start + start_to_next_mark + self.rot(PI/2 + PI/6 + angle_main_line)@(length*RIGHT),
                    stroke_width = mark_width
                ))
                self.add(Line(
                    start = start + start_to_next_mark,
                    end = start + start_to_next_mark + self.rot(-PI/2 - PI/6 + angle_main_line)@(length*RIGHT),
                    stroke_width = mark_width
                ))
                start_to_next_mark += mark_spacing*(end - start)
            for i in range(num_one_arrows):
                self.add(Line(
                    start = start + start_to_next_mark,
                    end = start + start_to_next_mark + self.rot(PI/2 + PI/3 + angle_main_line)@(length*RIGHT),
                    stroke_width = mark_width
                ))
                self.add(Line(
                    start = start + start_to_next_mark,
                    end = start + start_to_next_mark + self.rot(-PI/2 - PI/3 + angle_main_line)@(length*RIGHT),
                    stroke_width = mark_width
                ))
                start_to_next_mark += mark_spacing*(end - start)

    def rot(self, angle):
        return np.array([[np.cos(angle), -np.sin(angle), 0], [np.sin(angle), np.cos(angle), 0], [0, 0, 1]])
    
    def get_length(self):
        return self.line.get_length()
    
    def get_start(self):
        return self.line.get_start()
    
    def get_end(self):
        return self.line.get_end()

    def get_unit_vector(self):
        return self.line.get_unit_vector()