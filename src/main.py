from window import Window, Cell


def main():
    win = Window(800, 600)

    cell = Cell(win)
    cell.draw(200, 200, 400, 400)

    cell = Cell(win)
    cell.has_left_wall = False
    cell.draw(300, 30, 400, 40)

    cell = Cell(win)
    cell.has_right_wall = False
    cell.draw(400, 100, 500, 200)

    cell = Cell(win)
    cell.has_bottom_wall = False
    cell.draw(20, 300, 300, 500)

    cell = Cell(win)
    cell.has_top_wall = False
    cell.draw(100, 50, 150, 100)

    win.wait_for_close()


if __name__ == "__main__":
    main()
