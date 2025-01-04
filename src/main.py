from window import Window, Point, Line


def main():
    win = Window(800, 600)

    a = Point(x=40, y=100)
    b = Point(x=600, y=300)

    line = Line(a, b)

    win.draw_line(line, "blue")

    win.wait_for_close()


if __name__ == "__main__":
    main()
