from tkinter import Tk, BOTH, Canvas


class Window:
    def __init__(self, width, height):
        self.__root = Tk()
        self.__root.title = "Maze solver"
        self.__canvas = Canvas(self.__root, width=width, height=height, bg="white")
        self.__canvas.pack(fill=BOTH, expand=1)
        self.__running = False
        self.__root.protocol("WM_DELETE_WINDOW", self.close)

    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()

    def wait_for_close(self):
        self.__running = True
        while self.__running:
            self.redraw()

    def close(self):
        self.__running = False

    def draw_line(self, line, fill_color="black"):
        line.draw(self.__canvas, fill_color)


class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y


class Line:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def draw(self, canvas, fill_color="black"):
        canvas.create_line(
            self.a.x, self.a.y, self.b.x, self.b.y, fill=fill_color, width=2
        )


class Cell:
    def __init__(self, win):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
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
        if self.has_left_wall:
            line = Line(Point(x1, y1), Point(x1, y2))
            self.__win.draw_line(line)
        if self.has_top_wall:
            line = Line(Point(x1, y1), Point(x2, y1))
            self.__win.draw_line(line)
        if self.has_right_wall:
            line = Line(Point(x2, y1), Point(x2, y2))
            self.__win.draw_line(line)
        if self.has_bottom_wall:
            line = Line(Point(x1, y2), Point(x2, y2))
            self.__win.draw_line(line)
