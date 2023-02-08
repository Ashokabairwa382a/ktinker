# title: To set the title of the widget.
# activebackground: to set the background color when widget is under the cursor.
# activeforeground: to set the foreground color when widget is under the cursor.
# bg: to set he normal background color.
# command: to call a function.
# font: to set the font on the button label.
# image: to set the image on the widget.

from tkinter import *
      
root = Tk()
menu = Menu(root)
root.config(menu=menu)
filemenu = Menu(menu)
menu.add_cascade(label='File', menu=filemenu)
filemenu.add_command(label='New')
filemenu.add_command(label='Open...')
filemenu.add_separator()
filemenu.add_command(label='Exit', command=root.quit)
helpmenu = Menu(menu)
menu.add_cascade(label='Help', menu=helpmenu)
helpmenu.add_command(label='About')
mainloop()