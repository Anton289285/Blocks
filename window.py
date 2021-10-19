from tkinter import *
from constants import *
from random import *
import rec_mod
import can_vid_mod

class MainWindow:
    root = Tk()
    frame_for_painting = Frame(root, bd=5, bg="DarkGoldenrod3")
    canvas_for_painting = Canvas(frame_for_painting, width=quantity_of_columns * xy_resolutions,
                                 heigh=quantity_of_row * xy_resolutions, bg="SkyBlue3")
    frame_for_data = Frame(root, bd=5, bg="Light Slate Grey")
    label_game_status = Label(frame_for_data, text='play', font='arial 18', bg="light grey")
    label_score = Label(frame_for_data, text='score: 0', font='arial 16', bg="light grey")
    label_next = Label(frame_for_data, text='next', font='arial 14', bg="light slate grey", bd=5)
    canvas_next = Canvas(frame_for_data, width=xy_resolutions * 4,
                         heigh=xy_resolutions * 4, bg="SkyBlue3")
    label_line = Label(frame_for_data, text='line: 0', font='arial 14', bg="light slate grey", bd=5)
    label_set = Label(frame_for_data, text='set: 0', font='arial 14', bg="light slate grey", bd=5)
    label_speed = Label(frame_for_data, text='speed: 1', font='arial 14', bg="light slate grey", bd=5)


    def __init__(self):
        self.root.title("Tetris")
        self.root.bind('<Escape>', quit)
        self.frame_for_painting.grid(column=0, row=0)
        self.canvas_for_painting.pack()
        self.frame_for_data.grid(column=1, row=0, sticky="n")
        self.label_score.grid(column=0, row=0, sticky="w")
        self.label_next.grid(column=0, row=1)
        self.canvas_next.grid(column=0, row=2, sticky="n")
        self.label_game_status.grid(column=0, row=3, sticky="s")
        self.label_line.grid(column=0, row=4, sticky="w")
        self.label_set.grid(column=0, row=5, sticky="w")
        self.label_speed.grid(column=0, row=6, sticky="w")
        for i in range(1, quantity_of_columns):
            self.canvas_for_painting.create_line(i * xy_resolutions, 0,
                                                 i * xy_resolutions, xy_resolutions * quantity_of_row, fill="SkyBlue4")
        for i in range(1, quantity_of_row):
            self.canvas_for_painting.create_line(0, i * xy_resolutions,
                                                 xy_resolutions * quantity_of_columns, i * xy_resolutions,
                                                 fill="SkyBlue4")

        for i in range(1, 4):
            self.canvas_next.create_line(0, xy_resolutions * i,
                                         xy_resolutions * 4, xy_resolutions * i, fill="SkyBlue4")
        for i in range(1, 4):
            self.canvas_next.create_line(xy_resolutions * i, 0,
                                         xy_resolutions * i, xy_resolutions * 4, fill="SkyBlue4")



class Cube:
    column = 0
    row = 0
    coordx = 0
    coordy = 0

    def __init__(self, some_canvas, column, row):
        self.canvas_for_Cube = some_canvas
        self.column = column
        self.row = row
        self.some_Cube = self.canvas_for_Cube.create_rectangle(column * xy_resolutions,
                                                               row * xy_resolutions,
                                                               (column + 1) * xy_resolutions,
                                                               (row + 1) * xy_resolutions,
                                                               fill=Cube_color, outline = "gray24")

    def move_down(self):
        self.column = self.column + 0
        self.row = self.row + 1
        self.canvas_for_Cube.move(self.some_Cube, 0, xy_resolutions)

    def move_up(self):
        self.column = self.column + 0
        self.row = self.row - 1
        self.canvas_for_Cube.move(self.some_Cube, 0, - xy_resolutions)

    def move_right(self):
        self.column = self.column + 1
        self.row = self.row + 0
        self.canvas_for_Cube.move(self.some_Cube, xy_resolutions, 0)

    def move_left(self):
        self.column = self.column - 1
        self.row = self.row + 0
        self.canvas_for_Cube.move(self.some_Cube, -xy_resolutions, 0)

    def delete(self):
        self.canvas_for_Cube.delete(self.some_Cube)

    def change_color(self, color):
        self.canvas_for_Cube.itemconfig(self.some_Cube, fill=color)


class Game:
    number_of_current_set = 0
    number_of_next_set = 0
    heap = []
    time_tik = 0
    game_status = "play"
    score = 0
    score_line = 0
    score_set = 0
    score_speed = 1

    def __init__(self):
        self.tetris_window = MainWindow()
        self.current_set = []
        self.next_set = []
        self.time_tik = time_tik_init
        self.tetris_window.label_game_status['text'] = 'play'
        self.count_pause = 3
        self.record = rec_mod.Some_record("./record/record.txt")
        self.canvas_vidjet = can_vid_mod.Canvas_widjet(quantity_of_columns,
                                                       quantity_of_row,
                                                       xy_resolutions,
                                                       self.tetris_window.canvas_for_painting,
                                                       self.tetris_window.root,
                                                       self.record.recordsman)



    def new_current_set(self):
        if self.number_of_current_set == 1:
            self.zero_column = quantity_of_columns / 2 - 2
            self.zero_row = - 1
            self.current_set.append(Cube(self.tetris_window.canvas_for_painting, (quantity_of_columns / 2 - 2) + 0, 0))
            self.current_set.append(Cube(self.tetris_window.canvas_for_painting, (quantity_of_columns / 2 - 2) + 1, 0))
            self.current_set.append(Cube(self.tetris_window.canvas_for_painting, (quantity_of_columns / 2 - 2) + 2, 0))
            self.current_set.append(Cube(self.tetris_window.canvas_for_painting, (quantity_of_columns / 2 - 2) + 3, 0))
        elif self.number_of_current_set == 2:
            self.zero_column = quantity_of_columns / 2 - 2
            self.zero_row = -1
            self.current_set.append(Cube(self.tetris_window.canvas_for_painting, (quantity_of_columns / 2 - 2) + 1, 0))
            self.current_set.append(Cube(self.tetris_window.canvas_for_painting, (quantity_of_columns / 2 - 2) + 1, 1))
            self.current_set.append(Cube(self.tetris_window.canvas_for_painting, (quantity_of_columns / 2 - 2) + 2, 0))
            self.current_set.append(Cube(self.tetris_window.canvas_for_painting, (quantity_of_columns / 2 - 2) + 2, 1))
        elif self.number_of_current_set == 3:
            self.zero_column = quantity_of_columns / 2 - 1
            self.zero_row = 0
            self.current_set.append(Cube(self.tetris_window.canvas_for_painting, (quantity_of_columns / 2 - 2) + 1, 0))
            self.current_set.append(Cube(self.tetris_window.canvas_for_painting, (quantity_of_columns / 2 - 2) + 1, 1))
            self.current_set.append(Cube(self.tetris_window.canvas_for_painting, (quantity_of_columns / 2 - 2) + 2, 1))
            self.current_set.append(Cube(self.tetris_window.canvas_for_painting, (quantity_of_columns / 2 - 2) + 2, 2))
        elif self.number_of_current_set == 4:
            self.zero_column = quantity_of_columns / 2 - 1
            self.zero_row = 0
            self.current_set.append(Cube(self.tetris_window.canvas_for_painting, (quantity_of_columns / 2 - 2) + 1, 1))
            self.current_set.append(Cube(self.tetris_window.canvas_for_painting, (quantity_of_columns / 2 - 2) + 2, 1))
            self.current_set.append(Cube(self.tetris_window.canvas_for_painting, (quantity_of_columns / 2 - 2) + 3, 1))
            self.current_set.append(Cube(self.tetris_window.canvas_for_painting, (quantity_of_columns / 2 - 2) + 2, 0))
        elif self.number_of_current_set == 5:
            self.zero_column = quantity_of_columns / 2 - 1
            self.zero_row = 0
            self.current_set.append(Cube(self.tetris_window.canvas_for_painting, (quantity_of_columns / 2 - 2) + 2, 0))
            self.current_set.append(Cube(self.tetris_window.canvas_for_painting, (quantity_of_columns / 2 - 2) + 2, 1))
            self.current_set.append(Cube(self.tetris_window.canvas_for_painting, (quantity_of_columns / 2 - 2) + 1, 1))
            self.current_set.append(Cube(self.tetris_window.canvas_for_painting, (quantity_of_columns / 2 - 2) + 1, 2))
        elif self.number_of_current_set == 6:
            self.zero_column = quantity_of_columns / 2 - 1
            self.zero_row = 0
            self.current_set.append(Cube(self.tetris_window.canvas_for_painting, (quantity_of_columns / 2 - 2) + 1, 1))
            self.current_set.append(Cube(self.tetris_window.canvas_for_painting, (quantity_of_columns / 2 - 2) + 2, 1))
            self.current_set.append(Cube(self.tetris_window.canvas_for_painting, (quantity_of_columns / 2 - 2) + 3, 1))
            self.current_set.append(Cube(self.tetris_window.canvas_for_painting, (quantity_of_columns / 2 - 2) + 3, 0))
        elif self.number_of_current_set == 7:
            self.zero_column = quantity_of_columns / 2 - 1
            self.zero_row = 0
            self.current_set.append(Cube(self.tetris_window.canvas_for_painting, (quantity_of_columns / 2 - 2) + 1, 0))
            self.current_set.append(Cube(self.tetris_window.canvas_for_painting, (quantity_of_columns / 2 - 2) + 1, 1))
            self.current_set.append(Cube(self.tetris_window.canvas_for_painting, (quantity_of_columns / 2 - 2) + 2, 1))
            self.current_set.append(Cube(self.tetris_window.canvas_for_painting, (quantity_of_columns / 2 - 2) + 3, 1))

    def new_next_set(self):
        if self.number_of_next_set == 1:
            self.next_set.append(Cube(self.tetris_window.canvas_next, 0, 1))
            self.next_set.append(Cube(self.tetris_window.canvas_next, 1, 1))
            self.next_set.append(Cube(self.tetris_window.canvas_next, 2, 1))
            self.next_set.append(Cube(self.tetris_window.canvas_next, 3, 1))
        elif self.number_of_next_set == 2:
            self.next_set.append(Cube(self.tetris_window.canvas_next, 1, 1))
            self.next_set.append(Cube(self.tetris_window.canvas_next, 2, 1))
            self.next_set.append(Cube(self.tetris_window.canvas_next, 1, 2))
            self.next_set.append(Cube(self.tetris_window.canvas_next, 2, 2))
        elif self.number_of_next_set == 3:
            self.next_set.append(Cube(self.tetris_window.canvas_next, 1, 0))
            self.next_set.append(Cube(self.tetris_window.canvas_next, 1, 1))
            self.next_set.append(Cube(self.tetris_window.canvas_next, 2, 1))
            self.next_set.append(Cube(self.tetris_window.canvas_next, 2, 2))
        elif self.number_of_next_set == 4:
            self.next_set.append(Cube(self.tetris_window.canvas_next, 0, 1))
            self.next_set.append(Cube(self.tetris_window.canvas_next, 1, 1))
            self.next_set.append(Cube(self.tetris_window.canvas_next, 2, 1))
            self.next_set.append(Cube(self.tetris_window.canvas_next, 1, 0))
        elif self.number_of_next_set == 5:
            self.next_set.append(Cube(self.tetris_window.canvas_next, 2, 0))
            self.next_set.append(Cube(self.tetris_window.canvas_next, 2, 1))
            self.next_set.append(Cube(self.tetris_window.canvas_next, 1, 1))
            self.next_set.append(Cube(self.tetris_window.canvas_next, 1, 2))
        elif self.number_of_next_set == 6:
            self.next_set.append(Cube(self.tetris_window.canvas_next, 0, 1))
            self.next_set.append(Cube(self.tetris_window.canvas_next, 1, 1))
            self.next_set.append(Cube(self.tetris_window.canvas_next, 2, 1))
            self.next_set.append(Cube(self.tetris_window.canvas_next, 2, 0))
        elif self.number_of_next_set == 7:
            self.next_set.append(Cube(self.tetris_window.canvas_next, 0, 0))
            self.next_set.append(Cube(self.tetris_window.canvas_next, 0, 1))
            self.next_set.append(Cube(self.tetris_window.canvas_next, 1, 1))
            self.next_set.append(Cube(self.tetris_window.canvas_next, 2, 1))

    def move_left(self, event):
        move_left_pass = False
        for i in range(len(self.current_set)):
            if (self.current_set[i].column - 1) < 0:
                move_left_pass = True
            for j in range(len(self.heap)):
                if ((self.current_set[i].column - 1 == self.heap[j].column) and
                        (self.current_set[i].row == self.heap[j].row)):
                    move_left_pass = True
        if self.game_status == "play":
            if (move_left_pass == False):
                self.zero_column = self.zero_column - 1
                for i in range(len(self.current_set)):
                    self.current_set[i].move_left()

    def move_right(self, event):
        move_right_pass = False
        for i in range(len(self.current_set)):
            if (self.current_set[i].column + 1) > (quantity_of_columns - 1):
                move_right_pass = True
            for j in range(len(self.heap)):
                if ((self.current_set[i].column + 1 == self.heap[j].column) and
                        (self.current_set[i].row == self.heap[j].row)):
                    move_right_pass = True
        if self.game_status == "play":
            if (move_right_pass == False):
                self.zero_column = self.zero_column + 1
                for i in range(len(self.current_set)):
                        self.current_set[i].move_right()

    def move_down_with_key(self, event):
        move_down_pass = False
        for i in range(len(self.current_set)):
            if (self.current_set[i].row + 1 >= quantity_of_row):
                move_down_pass = True
            for j in range(len(self.heap)):
                if (((self.current_set[i].row + 1) == self.heap[j].row) and (
                        (self.current_set[i].column) == self.heap[j].column)):
                    move_down_pass = True
        if (move_down_pass == False) and (self.game_status == "play"):
            self.zero_row = self.zero_row + 1
            for i in range(len(self.current_set)):
                self.current_set[i].move_down()

    def move_down(self):
        move_down_pass = False
        for i in range(len(self.current_set)):
            if (self.current_set[i].row + 1 >= quantity_of_row):
                move_down_pass = True
            for j in range(len(self.heap)):
                if (((self.current_set[i].row + 1) == self.heap[j].row) and (
                        (self.current_set[i].column) == self.heap[j].column)):
                    move_down_pass = True
        if (move_down_pass == False):
            self.zero_row = self.zero_row + 1
            for i in range(len(self.current_set)):
                self.current_set[i].move_down()
            self.solve = self.tetris_window.root.after(self.time_tik, self.move_down)
        else:
            for i in range(len(self.current_set)):
                self.heap.append(Cube(self.tetris_window.canvas_for_painting, self.current_set[i].column,
                                      self.current_set[i].row))
                self.heap[len(self.heap) - 1].change_color(heap_color)
            self.check_heap()
            self.delete_current_set()
            self.number_of_current_set = self.number_of_next_set
            self.new_current_set()
            self.score_set = self.score_set + 1
            self.print_score()
            self.delete_next_set()
            self.number_of_next_set = randint(1, 7)
            self.new_next_set()
            if (self.check_game_over() == True):
                if (self.record.apple < self.score):
                    self.game_status = "enter record"
                    self.canvas_vidjet.draw(self.score, self.record.recordsman)
                    self.tetris_window.root.bind("<Return>", self.enter_record)

                self.tetris_window.label_game_status["text"] = "restart press R"
                self.game_status = "game_over"
            else:
                self.solve = self.tetris_window.root.after(self.time_tik, self.move_down)

    def enter_record(self, event):
        string = self.canvas_vidjet.entry.get()
        self.record.update(string, self.score)
        self.canvas_vidjet.erase()
        self.tetris_window.root.unbind("<Return>")


    def rotate_right(self, event):
        rotate_right_pass = False

        if (self.number_of_current_set == 1) or (self.number_of_current_set == 2):
            strange_coefficient = 3
        else:
            strange_coefficient = 2

        for i in range(len(self.current_set)):
            moveX = strange_coefficient - (
                    self.current_set[i].column - self.zero_column + self.current_set[i].row - self.zero_row)
            moveY = self.current_set[i].column - self.zero_column - self.current_set[i].row + self.zero_row
            new_column = self.current_set[i].column
            new_row = self.current_set[i].row
            for j in range(int(abs(moveX))):
                if (moveX > 0):
                    new_column = new_column + 1
                elif (moveX < 0):
                    new_column = new_column - 1
            for j in range(int(abs(moveY))):
                if (moveY > 0):
                    new_row = new_row + 1
                elif (moveY < 0):
                    new_row = new_row - 1

            if (new_column < 0) or (new_column > (quantity_of_columns - 1)) or (new_row < 0) or (
                    new_row > (quantity_of_row - 1)):
                rotate_right_pass = True

            for heap_number in range(len(self.heap)):
                if (self.heap[heap_number].column == new_column) and (self.heap[heap_number].row == new_row):
                    rotate_right_pass = True

        if (rotate_right_pass == False):
            for i in range(len(self.current_set)):
                moveX = strange_coefficient - (
                        self.current_set[i].column - self.zero_column + self.current_set[i].row - self.zero_row)
                moveY = self.current_set[i].column - self.zero_column - self.current_set[i].row + self.zero_row
                if self.game_status == "play":
                    for j in range(int(abs(moveX))):
                        if (moveX > 0):
                            self.current_set[i].move_right()
                        elif (moveX < 0):
                            self.current_set[i].move_left()
                    for j in range(int(abs(moveY))):
                        if (moveY > 0):
                            self.current_set[i].move_down()
                        elif (moveY < 0):
                            self.current_set[i].move_up()

    def rotate_left(self, event):
        rotate_left_pass = False

        if (self.number_of_current_set == 1) or (self.number_of_current_set == 2):
            strange_coefficient = 3
        else:
            strange_coefficient = 2

        for i in range(len(self.current_set)):
            moveX = (self.current_set[i].row - self.zero_row) - (self.current_set[i].column - self.zero_column)
            moveY = strange_coefficient - ((self.current_set[i].column - self.zero_column) +
                                           (self.current_set[i].row - self.zero_row))
            new_column = self.current_set[i].column
            new_row = self.current_set[i].row
            for j in range(int(abs(moveX))):
                if (moveX > 0):
                    new_column = new_column + 1
                elif (moveX < 0):
                    new_column = new_column - 1
            for j in range(int(abs(moveY))):
                if (moveY > 0):
                    new_row = new_row + 1
                elif (moveY < 0):
                    new_row = new_row - 1

            if (new_column < 0) or (new_column > (quantity_of_columns - 1)) or (new_row < 0) or (
                    new_row > (quantity_of_row - 1)):
                rotate_left_pass = True

            for heap_number in range(len(self.heap)):
                if (self.heap[heap_number].column == new_column) and (self.heap[heap_number].row == new_row):
                    rotate_left_pass = True

        if (rotate_left_pass == False):
            for i in range(len(self.current_set)):
                moveX = (self.current_set[i].row - self.zero_row) - (self.current_set[i].column - self.zero_column)
                moveY = strange_coefficient - ((self.current_set[i].column - self.zero_column) +
                                               (self.current_set[i].row - self.zero_row))
                if self.game_status == "play":
                    for j in range(int(abs(moveX))):
                        if (moveX > 0):
                            self.current_set[i].move_right()
                        elif (moveX < 0):
                            self.current_set[i].move_left()
                    for j in range(int(abs(moveY))):
                        if (moveY > 0):
                            self.current_set[i].move_down()
                        elif (moveY < 0):
                            self.current_set[i].move_up()

    def delete_current_set(self):
        for i in range(len(self.current_set)):
            self.current_set[i].delete()
        for i in range(len(self.current_set)):
            self.current_set.pop()

    def delete_next_set(self):
        for i in range(len(self.next_set)):
            self.next_set[i].delete()
        for i in range(len(self.next_set)):
            self.next_set.pop()

    def check_heap(self):
        number_of_row = 0
        quantity_of_row_in_one_check = 0
        while (number_of_row <= quantity_of_row):
            quantity_of_kubik_in_heap_in_row = 0
            for number_of_heap in range(len(self.heap)):
                if (self.heap[number_of_heap].row == number_of_row):
                    quantity_of_kubik_in_heap_in_row = quantity_of_kubik_in_heap_in_row + 1
            if (quantity_of_kubik_in_heap_in_row == quantity_of_columns):
                number_of_heap_for_delete = len(self.heap) - 1
                self.score_line = self.score_line + 1
                self.score_speed = 1 + (self.score_line//10)#10 - количество линий когда будет происходить увеличение скорости
                quantity_of_row_in_one_check = quantity_of_row_in_one_check + 1
                while (number_of_heap_for_delete >= 0):
                    if (self.heap[number_of_heap_for_delete].row == number_of_row):
                        self.heap[number_of_heap_for_delete].delete()
                        self.heap.pop(number_of_heap_for_delete)
                        number_of_heap_for_delete = number_of_heap_for_delete - 1
                    else:
                        number_of_heap_for_delete = number_of_heap_for_delete - 1
                for number_of_kubik_for_move_down in range(len(self.heap)):
                    if (self.heap[number_of_kubik_for_move_down].row < number_of_row):
                        self.heap[number_of_kubik_for_move_down].move_down()
            number_of_row = number_of_row + 1
        self.time_tik = self.speed_to_tik(self.score_speed)
        self.score = self.score + self.check_score(quantity_of_row_in_one_check)
        self.print_score()

    def check_game_over(self):
        check = False
        for number_of_kubik_in_current in range(len(self.current_set)):
            for number_of_kubik_in_heap in range(len(self.heap)):
                if (self.current_set[number_of_kubik_in_current].column == self.heap[
                    number_of_kubik_in_heap].column) and (
                        self.current_set[number_of_kubik_in_current].row == self.heap[number_of_kubik_in_heap].row):
                    check = True
        return check

    def game_restart(self, event):
        self.tetris_window.root.after_cancel(self.solve)
        self.score = 0
        self.score_line = 0
        self.score_set = 0
        self.score_speed = 1
        self.time_tik = time_tik_init
        self.print_score()

        for number_of_kubik_in_current in range(len(self.current_set)):
            self.current_set[len(self.current_set) - 1].delete()
            self.current_set.pop()
        for number_of_kubik_in_heap in range(len(self.heap)):
            self.heap[len(self.heap) - 1].delete()
            self.heap.pop()
        for number_of_kubik_in_next in range(len(self.next_set)):
            self.next_set[len(self.next_set) - 1].delete()
            self.next_set.pop()
        self.number_of_next_set = randint(1, 7)
        self.new_next_set()
        self.number_of_current_set = randint(1, 7)
        self.new_current_set()
        self.solve = self.tetris_window.root.after(1000, self.move_down)
        self.tetris_window.label_game_status["text"] = 'play'
        self.game_status = "play"

    def pause(self, event):
        if self.game_status == "play":
            self.tetris_window.root.after_cancel(self.solve)
            self.game_status = "pause"
            self.tetris_window.label_game_status["text"] = "pause"
        elif self.game_status == "pause":
            self.move_down()
            self.game_status = "play"
            self.tetris_window.label_game_status["text"] = "play"

    def print_score(self):
        self.tetris_window.label_score["text"] = 'score: ' + str(self.score)
        self.tetris_window.label_line["text"] = 'line: ' + str(self.score_line)
        self.tetris_window.label_set["text"] = 'set: ' + str(self.score_set)
        self.tetris_window.label_speed["text"] = 'speed: ' + str(self.score_speed)

    def speed_to_tik(self, some_speed):
        some_tik = time_tik_init*1000
        for i in range((some_speed - 1)):
            some_tik = some_tik - some_tik//5 # 4 это на сколько  увеличиться скрость( на четверть)
        if some_tik//1000 < 1:
            some_tik = 1
        else: some_tik = int(some_tik//1000)
        return some_tik

    def check_score(self, some_quantity_of_row_in_check):
        some_score = 0
        if some_quantity_of_row_in_check == 1:
            some_score = 100
        elif some_quantity_of_row_in_check == 2:
            some_score = 200
        elif some_quantity_of_row_in_check == 3:
            some_score = 500
        elif some_quantity_of_row_in_check == 4:
            some_score = 200
        some_score = some_score*self.score_speed
        return some_score



