from graphics import Window
from maze import Maze


def main():
    num_rows = 14
    num_cols = 20
    screen_width = 800
    screen_height = 600

    margin = 10

    cell_size_x = (screen_width - 2 * margin) / num_cols
    cell_size_y = (screen_height - 2 * margin) / num_rows

    win = Window(screen_width, screen_height)

    _maze = Maze(margin, margin, num_rows, num_cols, cell_size_x, cell_size_y, win)

    win.wait_for_close()


if __name__ == "__main__":
    main()
