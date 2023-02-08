from tkinter import *
master = Tk()
w = Canvas(master, width=40, height=60)
w.pack()
canvas_height=20
canvas_width=200
y = int(canvas_height / 2)
w.create_line(0, y, canvas_width, y )
mainloop()




#bd: to set the border width in pixels.
# bg: to set the normal background color.
# cursor: to set the cursor used in the canvas.
# highlightcolor: to set the color shown in the focus highlight.
# width: to set the width of the widget.
# height: to set the height of the widget.