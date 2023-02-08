# width: to set the width of the widget.
# activebackground: To set the background when mouse is over the widget.
# bg: to set he normal background color.
# bd: to set the size of border around the indicator.
# cursor: To appear the cursor when the mouse over the menubutton.



from tkinter import *

root = Tk()
scrollbar = Scrollbar(root)
scrollbar.pack( side = LEFT, fill = Y )
mylist = Listbox(root, yscrollcommand = scrollbar.set )
for line in range(2220):
   mylist.insert(END, 'My name is Ashoka :' + str(line))
mylist.pack( side = LEFT, fill = BOTH )
scrollbar.config( command = mylist.yview )
mainloop()