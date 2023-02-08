# highlightcolor: To set the color of the focus highlight when widget has to be focused.
# insertbackground: To set the background of the widget.
# bg: to set he normal background color.
# font: to set the font on the button label.
# image: to set the image on the widget.
# width: to set the width of the widget.
# height: to set the height of the widget.

from tkinter import *
root = Tk()
T = Text(root, height=100, width=200)
T.pack()
T.insert(END, 'Ashoka bairwa\ngood boy\n')
mainloop()