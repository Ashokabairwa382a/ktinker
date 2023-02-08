from tkinter import *
master = Tk()
w = Spinbox(master, from_ = 0, to = 10)
w.pack()
w = Spinbox(master, from_ = 10, to = 20)
w.pack()
w = Spinbox(master, from_ = 20, to = 30)
w.pack()
w = Spinbox(master, from_ = 40, to = 50)
w.pack()
mainloop()



# bg: to set he normal background color.
# bd: to set the size of border around the indicator.
# cursor: To appear the cursor when the mouse over the menubutton.
# command: To call a function.
# width: to set the width of the widget.
# activebackground: To set the background when mouse is over the widget.
# disabledbackground: To disable the background when mouse is over the widget.
# from_: To set the value of one end of the range.
# to: To set the value of the other end of the range.