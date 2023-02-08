# cursor: To change the cursor pattern when the mouse is over the widget.
# activebackground: To set the background of the widget when mouse is over the widget.
# bg: to set he normal background color.
# orient: Set it to HORIZONTAL or VERTICAL according to the requirement.
# from_: To set the value of one end of the scale range.
# to: To set the value of the other end of the scale range.
# image: to set the image on the widget.
# width: to set the width of the widget.

from tkinter import *
from token import CIRCUMFLEX
master = Tk()
w = Scale(master, from_=0, to=100)
w.pack()
w = Scale(master, from_=0, to=200, orient=VERTICAL)
w.pack()
w = Scale(master, from_=0, to=500, orient=HORIZONTAL)
w.pack()
mainloop()