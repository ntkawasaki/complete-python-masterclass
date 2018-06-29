# Write a GUI program to create a simple calculator
# layout that looks like the screenshot.
#
# Try to be as Pythonic as possible - it's ok if you
# end up writing repeated Button and Grid statements,
# but consider using lists and a for loop.
#
# There is no need to store the buttons in variables.
#
# As an optional extra, refer to the documentation to
# work out how to use minsize() to prevent your window
# from being shrunk so that the widgets vanish from view.
#
# Hint: You may want to use the widgets .winfo_height() and
# winfo_width() methods, in which case you should know that
# they will not return the correct results unless the window
# has been forced to draw the widgets by calling its .update()
# method first.
#
# If you are using Windows you will probably find that the
# width is already constrained and can't be resized too small.
# The height will still need to be constrained, though.

try:
    import tkinter
except ImportError:
    import Tkinter as tkinter

keys = [
        [("C", 1), ("CE", 1)],  # row 0
        [("7", 1), ("8", 1), ("9", 1), ("+", 1)],  # row 1
        [("4", 1), ("5", 1), ("6", 1), ("-", 1)],  # row 2
        [("1", 1), ("2", 1), ("3", 1), ("*", 1)],  # row 3
        [("0", 1), ("=", 1), ("/", 1)]  # row 4
       ]

main_window = tkinter.Tk()
main_window.title("Calculator")
main_window.geometry("240x300-0-0")

main_window_padding = 8
main_window["padx"] = main_window_padding

# widget to display result
result = tkinter.Entry(main_window)
result.grid(row=0, column=0, sticky="nsew")  # stick makes buttons fill width of its cell

key_pad = tkinter.Frame(main_window)
key_pad.grid(row=1, column=0, sticky="nsew")

row = 0
# loop through each row containing multiple keys
# note: this is a list, so index 0 = first value "C", 1 = second value 1
for key_row in keys:

    # place each key in respective row/column per row
    col = 0
    for key in key_row:
        tkinter.Button(key_pad, text=key[0]).grid(row=row, column=col, columnspan=key[1], sticky=tkinter.E + tkinter.W)
        col += 1
    row += 1

main_window.update()
main_window.minsize(key_pad.winfo_width() + main_window_padding, result.winfo_height() + key_pad.winfo_height())
main_window.maxsize(key_pad.winfo_width() + 50 + main_window_padding, result.winfo_height() + 50 + key_pad.winfo_height())
main_window.mainloop()
