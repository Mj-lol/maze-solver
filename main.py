from graphics import Window, Line, Point, Cell


def main():
    win = Window(800, 600)




    l = Line(Point(50, 50), Point(400, 400))
    win.draw_line(l, "black")



    c = Cell(win)
    c.has_left_wall = False
    c.draw(50, 50, 100, 100)

    c = Cell(win)
    c.has_right_wall = False
    c.draw(125, 125, 200, 200)

    c = Cell(win)
    c.has_bottom_wall = False
    c.draw(225, 225, 250, 250)

    c = Cell(win)
    c.has_top_wall = False
    c.draw(300, 300, 500, 500)




    win.wait_for_close()


main()
