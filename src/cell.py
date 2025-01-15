from graphics import Point, Line


class Cell:
    def __init__(self, win=None):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self.visited = False
        self.__x1 = None
        self.__x2 = None
        self.__y1 = None
        self.__y2 = None
        self.__win = win

    def draw(self, x1, y1, x2, y2):
        self.__x1 = x1
        self.__x2 = x2
        self.__y1 = y1
        self.__y2 = y2
        color = (
            "black" if self.has_left_wall else "white",
            "black" if self.has_top_wall else "white",
            "black" if self.has_right_wall else "white",
            "black" if self.has_bottom_wall else "white"
        )

        line = Line(Point(x1, y1), Point(x1, y2))
        self.__win.draw_line(line, color[0])
        line = Line(Point(x1, y1), Point(x2, y1))
        self.__win.draw_line(line, color[1])
        line = Line(Point(x2, y1), Point(x2, y2))
        self.__win.draw_line(line, color[2])
        line = Line(Point(x1, y2), Point(x2, y2))
        self.__win.draw_line(line, color[3])

    def get_center_point(self):
        return Point((self.__x1 + self.__x2) / 2, (self.__y1 + self.__y2) / 2)

    def draw_move(self, to_cell, undo=False):
        from_center = self.get_center_point()
        to_center = to_cell.get_center_point()
        color = "gray" if undo else "red"
        line = Line(from_center, to_center)
        self.__win.draw_line(line, color)
