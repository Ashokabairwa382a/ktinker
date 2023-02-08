# highlightcolor: To set the color of the focus highlight when widget has to be focused.
# bg: to set he normal background color.
# bd: to set the border width in pixels.
# font: to set the font on the button label.
# image: to set the image on the widget.
# width: to set the width of the widget.
# height: to set the height of the widget.

from tkinter import *

top = Tk()
Lb = Listbox(top)
Lb.insert(1, 'Python')
Lb.insert(2, 'Java')
Lb.insert(3, 'C++')
Lb.insert(4, 'Dart')
Lb.insert(5, 'C#')
Lb.insert(6, 'PHP')
Lb.insert(7, 'Ruby')
Lb.insert(8, 'all')
Lb.pack()
top.mainloop()
