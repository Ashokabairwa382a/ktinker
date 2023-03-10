# activebackground: To set the background when mouse is over the widget.
# activeforeground: To set the foreground when mouse is over the widget.
# bg: to set he normal background color.
# bd: to set the size of border around the indicator.
# cursor: To appear the cursor when the mouse over the menubutton.
# image: to set the image on the widget.
# width: to set the width of the widget.
# height: to set the height of the widget.
# highlightcolor: To set the color of the focus highlight when widget has to be focused.

from tkinter import *

top = Tk()
mb = Menubutton( top, text = &quot; GfG&quot;)
mb.grid()
mb.menu = Menu ( mb, tearoff = 0 )
mb[&quot;menu&quot;] = mb.menu
cVar = IntVar()
aVar = IntVar()
mb.menu.add_checkbutton ( label ='Contact', variable = cVar )
mb.menu.add_checkbutton ( label = 'About', variable = aVar )
mb.pack()
top.mainloop()
