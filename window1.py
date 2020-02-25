from tkinter import *
from random import *
from constants import *

def load():
    main_window = Tk()
    main_window.title("Tetris")
    main_window.bind('<Escape>', quit)
    frame_for_painting = Frame(main_window, bd = 5, bg = "black")
    canvas_current = Canvas(frame_for_painting, width = xy_resolutions * quantity_of_columns,
                                 height = xy_resolutions * quantity_of_row,
                                 bg = "blue2")
    frame_for_painting.grid(column = 0, row = 0)
    canvas_current.pack()
    for i in range(1, quantity_of_columns):
        canvas_current.create_line(i * xy_resolutions,0 , i * xy_resolutions,
                                   xy_resolutions * quantity_of_row, fill = "red")
    for i in range(1, quantity_of_row):
        canvas_current.create_line(0, i * xy_resolutions,
                                        xy_resolutions * quantity_of_columns, i * xy_resolutions,
                                        fill = "red")
    frame_for_data = Frame(main_window, bd = 5, bg = "green")
    frame_for_data.grid(column = 1, row = 0)
    canvas_next = Canvas(frame_for_data, width = xy_resolutions * 4,
                         height = xy_resolutions * 4, bg = "white")
    canvas_next.grid(column = 0, row = 0)
    for i in range(1, 4):
        canvas_next.create_line(i * xy_resolutions, 0, i * xy_resolutions,
                                4 *xy_resolutions, fill = "red")
    for i in range(1, 4):
        canvas_next.create_line( 0, i * xy_resolutions,
                                 4 *xy_resolutions,i * xy_resolutions,
                                 fill = "red")

    canvas_next.create_rectangle(0,0,20,20,fill = "red")


class brick():
    column = 0
    row = 0


    def __init__(self, column, row):
        self.column = column
        self.row = row
        self.some_brick = canvas_next.create_rectangle(0,0,20,20,fill = "red")

