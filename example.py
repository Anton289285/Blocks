from tkinter import *

root = Tk()


def change(event):
    b['fg'] = "red"
    b['activeforeground'] = "red"


b = Button(text='RED', width=10, height=3)
b.bind('<Button-1>', change)
b.bind('<Return>', change)

b.pack()

root.mainloop()