try:
    import tkinter
except ImportError:  # python 2
    import Tkinter as tkinter

main_window = tkinter.Tk()

main_window.title("Hello World!")
main_window.geometry("640x480+500+200")  # controls size of window, place it pops up

label = tkinter.Label(main_window, text="Hello World!")
# label.pack(side="top")
label.grid(row=0, column=0)  # place uses absolute locations

left_frame = tkinter.Frame(main_window)
# left_frame.pack(side="left", anchor="n", fill=tkinter.Y, expand=False)
left_frame.grid(row=1, column=1)


canvas = tkinter.Canvas(left_frame, relief="raised", borderwidth=1)
canvas.grid(row=1, column=0)

right_frame = tkinter.Frame(main_window)
right_frame.grid(row=1, column=2, sticky="n")  # like anchor in pack()

button_1 = tkinter.Button(right_frame, text="Button 1")
button_2 = tkinter.Button(right_frame, text="Button 2")
button_3 = tkinter.Button(right_frame, text="Button 3")
button_1.grid(row=0, column=0)
button_2.grid(row=1, column=0)
button_3.grid(row=2, column=0)

# configure columns
main_window.columnconfigure(0, weight=1)
main_window.columnconfigure(1, weight=1)
main_window.grid_columnconfigure(2, weight=1)  # the same method basically

left_frame.config(relief="sunken", borderwidth=1)
right_frame.config(relief="sunken", borderwidth=1)
left_frame.grid(sticky="ns")
right_frame.grid(sticky="new")  # north, east, west

right_frame.columnconfigure(0, weight=1)  # makes button 2 fill width of frame
button_2.grid(sticky="ew")

# this needs to be the last entry
main_window.mainloop()  # pass control to tk
