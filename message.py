# bd: to set the border around the indicator.
# bg: to set he normal background color.
# font: to set the font on the button label.
# image: to set the image on the widget.
# width: to set the width of the widget.
# height: to set the height of the widget.

from tkinter import *
main = Tk()
ourMessage ='Hey  Ashoka'
messageVar = Message(main, text = ourMessage)
messageVar.config(bg='yellow')
messageVar.pack( )
main.mainloop( )