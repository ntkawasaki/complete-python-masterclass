# more functions!
# function can use variables from main program
# main program cannot use local variables in a function

import math
try:
    import tkinter
except ImportError:  # python 2
    import Tkinter as tkinter


def parabola(page, size):
    """
    Returns parabola or y = x^2 from param x.
    :param page:
    :param size
    :return parabola:
    """

    for x_coor in range(size):
        y_coor = x_coor * x_coor / size
        plot(page, x_coor, y_coor)
        plot(page, -x_coor, y_coor)


# modify the circle function so that it allows the color
# of the circle to be specified and defaults to red
def circle(page, radius, g, h, color="red"):
    """ Create a circle. """

    for x in range(g * 100, (g + radius) * 100):
        page.create_oval(g + radius, h + radius, g - radius, h - radius, outline=color, width=2)

        # x /= 100
        # print(x)
        # y = h + (math.sqrt(radius ** 2 - ((x - g) ** 2)))
        # plot(page, x, y)
        # plot(page, x, 2 * h - y)
        # plot(page, 2 * g - x, y)
        # plot(page, 2 * g - x, 2 * h - y)


def draw_axis(page):
    """
    Draws a horizontal and vertical line through middle of window to be used as
    the x and y axis.
    :param page:
    :return:
    """

    page.update()  # allows you to use winfo_width/height
    x_origin = page.winfo_width() / 2
    y_origin = page.winfo_height() / 2
    page.configure(scrollregion=(-x_origin, -y_origin, x_origin, y_origin))

    # create_line(x1, y1, x2, y2)
    page.create_line(-x_origin, 0, x_origin, 0, fill="black")  # horizontal
    page.create_line(0, y_origin, 0, -y_origin, fill="black")  # vertical

    # shows all local variables in this function
    print(locals())


def plot(page, x_plot, y_plot):
    """
    Plots points on canvas from params x and y.

    :param page:
    :param x_plot:
    :param y_plot:
    :return:
    """

    page.create_line(x_plot, -y_plot, x_plot + 1, -y_plot + 1, fill="red")


# window
main_window = tkinter.Tk()
main_window.title("Parabola")
main_window.geometry("640x480")

# canvas
canvas = tkinter.Canvas(main_window, width=640, height=480, background="gray")
canvas.grid(row=0, column=0)

# call function
draw_axis(canvas)

parabola(canvas, 300)
parabola(canvas, 20)

circle(canvas, 100, 100, 100, color="blue")
circle(canvas, 100, 100, 100, color="yellow")
circle(canvas, 100, 100, 100, color="green")

circle(canvas, 10, 30, 30, color="black")

main_window.mainloop()
