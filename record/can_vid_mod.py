from tkinter import Tk, Canvas, Label, Frame, Entry

class Canvas_widjet:


    def __init__(self, some_quantity_of_column_row, some_size_column_row,
                 some_canvas, some_window, some_name):
        self.root_window = some_window
        self.canvas = some_canvas
        self.canvas_centr_xy = int(some_quantity_of_column_row
                                  * some_size_column_row/2)

    def draw(self, some_record, some_name):
        self.record = some_record
        self.entry_string = some_name
        self.frame = Frame(self.canvas)
        self.window_on_canvas = self.canvas.create_window(self.canvas_centr_xy,
                                                          self.canvas_centr_xy,
                                                          height = 220,
                                                          width = 220,
                                                          window = self.frame)
        self.label1 = Label(self.frame, text = "Congratulations !!", font = "arial 20")
        self.entry = Entry(self.frame, width = 10, font = "arial 20")
        self.entry.insert(0, self.entry_string)
        self.label2 = Label(self.frame, text = "Your record: " + str(some_record),
                            font = "arial 20")
        self.label1.grid(column = 0, row = 0)
        self.entry.grid(column = 0, row = 1)
        self.label2.grid(column = 0, row = 2)

    def erase(self):
        self.label1.destroy()
        self.label2.destroy()
        self.entry.destroy()
        self.frame.destroy()
        self.canvas.delete(self.window_on_canvas)

    def hide(self):
        self.canvas.itemconfig(self.window_on_canvas, state = HIDDEN)

    def show(self):
        self.canvas.itemconfig(self.window_on_canvas, state = NORMAL)



