
from tkinter import *
root = Tk()
v = IntVar()
Radiobutton(root, text='Ashoka', variable=v, value=1).pack(anchor=W)
Radiobutton(root, text='Ashok', variable=v, value=2).pack(anchor=W)
mainloop()


# activebackground: to set the background color when widget is under the cursor.
# activeforeground: to set the foreground color when widget is under the cursor.
# bg: to set he normal background color.
# command: to call a function.
# font: to set the font on the button label.
# image: to set the image on the widget.
# width: to set the width of the label in characters.
# height: to set the height of the label in characters.