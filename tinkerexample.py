from tkinter import *

window = Tk()

mylable = Label(window,text="revathi")
mylable2= Label(window,text="hello world")

mylable.grid(row=0,column=0)
mylable2.grid(row=1,column=1)



window.mainloop()