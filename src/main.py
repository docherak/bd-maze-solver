from window import Window, Cell


def main():
    win = Window(800, 600)

    cell = Cell(win)
    cell.draw(50, 50, 100, 100)

    other_cell = Cell(win)
    other_cell.draw(200, 200, 400, 400)

    cell.draw_move(other_cell)

    cell = Cell(win)
    cell.draw(200, 20, 400, 100)

    other_cell = Cell(win)
    other_cell.draw(300, 500, 700, 600)

    cell.draw_move(other_cell, undo=True)

    win.wait_for_close()


if __name__ == "__main__":
    main()
