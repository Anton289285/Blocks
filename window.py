from tkinter import *
from constants import *
from random import *


class MainWindow:
    root = Tk()
    frame_for_painting = Frame(root, bd=5, bg="black")
    canvas_for_painting = Canvas(frame_for_painting, width=quantity_of_columns * xy_resolutions,
                                 heigh=quantity_of_row * xy_resolutions, bg="blue2")
    frame_for_data = Frame(root, bd=5, bg="red")
    label_game_status = Label(frame_for_data, text='game over', font='arial 24', bg="red")
    label_score = Label(frame_for_data, text='score = 0000', font='arial 20', bg="green")
    label_next = Label(frame_for_data, text='next', font='arial 19', bg="white", bd=5)
    canvas_next = Canvas(frame_for_data, width=xy_resolutions * 4,
                         heigh=xy_resolutions * 4, bg="white")

    def __init__(self):
        self.root.title("Tetris")
        self.root.bind('<Escape>', quit)
        self.frame_for_painting.grid(column=0, row=0)
        self.canvas_for_painting.pack()

        self.frame_for_data.grid(column=1, row=0, sticky="n")
        self.label_score.grid(column=0, row=0)
        self.label_next.grid(column=0, row=1)
        self.canvas_next.grid(column=0, row=2, sticky="n")
        self.label_game_status.grid(column=0, row=3, sticky="s")
        for i in range(1, quantity_of_columns):
            self.canvas_for_painting.create_line(i * xy_resolutions, 0,
                                                 i * xy_resolutions, xy_resolutions * quantity_of_row, fill="red")
        for i in range(1, quantity_of_row):
            self.canvas_for_painting.create_line(0, i * xy_resolutions,
                                                 xy_resolutions * quantity_of_columns, i * xy_resolutions,
                                                 fill="red")

        for i in range(1, 4):
            self.canvas_next.create_line(0, xy_resolutions * i,
                                         xy_resolutions * 4, xy_resolutions * i, fill="red")
        for i in range(1, 4):
            self.canvas_next.create_line(xy_resolutions * i, 0,
                                         xy_resolutions * i, xy_resolutions * 4, fill="red")


class Cube():
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
                                                                 fill="red")

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



class Game():
    number_of_current_set = 0
    number_of_next_set = 0
    heap = []
    time_tik = 0

    def __init__(self):
        self.tetris_window = MainWindow()
        self.current_set = []
        self.next_set = []
        self.time_tik = time_tik_init

    def new_current_set(self):
        if (self.number_of_current_set == 1):
            self.zero_column = quantity_of_columns / 2 - 2
            self.zero_row = - 1
            self.current_set.append(Cube(self.tetris_window.canvas_for_painting, (quantity_of_columns / 2 - 2) + 0, 0))
            self.current_set.append(Cube(self.tetris_window.canvas_for_painting, (quantity_of_columns / 2 - 2) + 1, 0))
            self.current_set.append(Cube(self.tetris_window.canvas_for_painting, (quantity_of_columns / 2 - 2) + 2, 0))
            self.current_set.append(Cube(self.tetris_window.canvas_for_painting, (quantity_of_columns / 2 - 2) + 3, 0))
        elif (self.number_of_current_set == 2):
            self.zero_column = quantity_of_columns / 2 - 2
            self.zero_row = -1
            self.current_set.append(Cube(self.tetris_window.canvas_for_painting, (quantity_of_columns / 2 - 2) + 1, 0))
            self.current_set.append(Cube(self.tetris_window.canvas_for_painting, (quantity_of_columns / 2 - 2) + 1, 1))
            self.current_set.append(Cube(self.tetris_window.canvas_for_painting, (quantity_of_columns / 2 - 2) + 2, 0))
            self.current_set.append(Cube(self.tetris_window.canvas_for_painting, (quantity_of_columns / 2 - 2) + 2, 1))
        elif (self.number_of_current_set == 3):
            self.zero_column = quantity_of_columns / 2 - 1
            self.zero_row = 0
            self.current_set.append(Cube(self.tetris_window.canvas_for_painting, (quantity_of_columns / 2 - 2) + 1, 0))
            self.current_set.append(Cube(self.tetris_window.canvas_for_painting, (quantity_of_columns / 2 - 2) + 1, 1))
            self.current_set.append(Cube(self.tetris_window.canvas_for_painting, (quantity_of_columns / 2 - 2) + 2, 1))
            self.current_set.append(Cube(self.tetris_window.canvas_for_painting, (quantity_of_columns / 2 - 2) + 2, 2))
        elif (self.number_of_current_set == 4):
            self.zero_column = quantity_of_columns / 2 - 1
            self.zero_row = 0
            self.current_set.append(Cube(self.tetris_window.canvas_for_painting, (quantity_of_columns / 2 - 2) + 1, 1))
            self.current_set.append(Cube(self.tetris_window.canvas_for_painting, (quantity_of_columns / 2 - 2) + 2, 1))
            self.current_set.append(Cube(self.tetris_window.canvas_for_painting, (quantity_of_columns / 2 - 2) + 3, 1))
            self.current_set.append(Cube(self.tetris_window.canvas_for_painting, (quantity_of_columns / 2 - 2) + 2, 0))
        elif (self.number_of_current_set == 5):
            self.zero_column = quantity_of_columns / 2 - 1
            self.zero_row = 0
            self.current_set.append(Cube(self.tetris_window.canvas_for_painting, (quantity_of_columns / 2 - 2) + 2, 0))
            self.current_set.append(Cube(self.tetris_window.canvas_for_painting, (quantity_of_columns / 2 - 2) + 2, 1))
            self.current_set.append(Cube(self.tetris_window.canvas_for_painting, (quantity_of_columns / 2 - 2) + 1, 1))
            self.current_set.append(Cube(self.tetris_window.canvas_for_painting, (quantity_of_columns / 2 - 2) + 1, 2))
        elif (self.number_of_current_set == 6):
            self.zero_column = quantity_of_columns / 2 - 1
            self.zero_row = 0
            self.current_set.append(Cube(self.tetris_window.canvas_for_painting, (quantity_of_columns / 2 - 2) + 1, 1))
            self.current_set.append(Cube(self.tetris_window.canvas_for_painting, (quantity_of_columns / 2 - 2) + 2, 1))
            self.current_set.append(Cube(self.tetris_window.canvas_for_painting, (quantity_of_columns / 2 - 2) + 3, 1))
            self.current_set.append(Cube(self.tetris_window.canvas_for_painting, (quantity_of_columns / 2 - 2) + 3, 0))
        elif (self.number_of_current_set == 7):
            self.zero_column = quantity_of_columns / 2 - 1
            self.zero_row = 0
            self.current_set.append(Cube(self.tetris_window.canvas_for_painting, (quantity_of_columns / 2 - 2) + 1, 0))
            self.current_set.append(Cube(self.tetris_window.canvas_for_painting, (quantity_of_columns / 2 - 2) + 1, 1))
            self.current_set.append(Cube(self.tetris_window.canvas_for_painting, (quantity_of_columns / 2 - 2) + 2, 1))
            self.current_set.append(Cube(self.tetris_window.canvas_for_painting, (quantity_of_columns / 2 - 2) + 3, 1))

    def new_next_set(self):
        if (self.number_of_next_set == 1):
            self.next_set.append(Cube(self.tetris_window.canvas_next, 0, 1))
            self.next_set.append(Cube(self.tetris_window.canvas_next, 1, 1))
            self.next_set.append(Cube(self.tetris_window.canvas_next, 2, 1))
            self.next_set.append(Cube(self.tetris_window.canvas_next, 3, 1))
        elif (self.number_of_next_set == 2):
            self.next_set.append(Cube(self.tetris_window.canvas_next, 1, 1))
            self.next_set.append(Cube(self.tetris_window.canvas_next, 2, 1))
            self.next_set.append(Cube(self.tetris_window.canvas_next, 1, 2))
            self.next_set.append(Cube(self.tetris_window.canvas_next, 2, 2))
        elif (self.number_of_next_set == 3):
            self.next_set.append(Cube(self.tetris_window.canvas_next, 1, 0))
            self.next_set.append(Cube(self.tetris_window.canvas_next, 1, 1))
            self.next_set.append(Cube(self.tetris_window.canvas_next, 2, 1))
            self.next_set.append(Cube(self.tetris_window.canvas_next, 2, 2))
        elif (self.number_of_next_set == 4):
            self.next_set.append(Cube(self.tetris_window.canvas_next, 0, 1))
            self.next_set.append(Cube(self.tetris_window.canvas_next, 1, 1))
            self.next_set.append(Cube(self.tetris_window.canvas_next, 2, 1))
            self.next_set.append(Cube(self.tetris_window.canvas_next, 1, 0))
        elif (self.number_of_next_set == 5):
            self.next_set.append(Cube(self.tetris_window.canvas_next, 2, 0))
            self.next_set.append(Cube(self.tetris_window.canvas_next, 2, 1))
            self.next_set.append(Cube(self.tetris_window.canvas_next, 1, 1))
            self.next_set.append(Cube(self.tetris_window.canvas_next, 1, 2))
        elif (self.number_of_next_set == 6):
            self.next_set.append(Cube(self.tetris_window.canvas_next, 0, 1))
            self.next_set.append(Cube(self.tetris_window.canvas_next, 1, 1))
            self.next_set.append(Cube(self.tetris_window.canvas_next, 2, 1))
            self.next_set.append(Cube(self.tetris_window.canvas_next, 2, 0))
        elif (self.number_of_next_set == 7):
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
        if move_left_pass == False:
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
        if (move_right_pass == False):
            self.zero_column = self.zero_column + 1
            for i in range(len(self.current_set)):
                self.current_set[i].move_right()

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
            self.tetris_window.root.after(self.time_tik, self.move_down)
        else:
            for i in range(len(self.current_set)):
                self.heap.append(Cube(self.tetris_window.canvas_for_painting, self.current_set[i].column,
                                       self.current_set[i].row))
            self.check_heap()
            self.delete_current_set()
            self.number_of_current_set = self.number_of_next_set
            self.new_current_set()
            self.delete_next_set()
            self.number_of_next_set = randint(1, 7)
            self.new_next_set()
            if (self.check_game_over() == True):
                self.tetris_window.root.after(3000, self.game_restart)
            else:
                self.tetris_window.root.after(self.time_tik, self.move_down)

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
        while (number_of_row <= quantity_of_row):
            quantity_of_kubik_in_heap_in_row = 0
            for number_of_heap in range(len(self.heap)):
                if (self.heap[number_of_heap].row == number_of_row):
                    quantity_of_kubik_in_heap_in_row = quantity_of_kubik_in_heap_in_row + 1
            if (quantity_of_kubik_in_heap_in_row == quantity_of_columns):
                number_of_heap_for_delete = len(self.heap) - 1
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

    def check_game_over(self):
        check = False
        for number_of_kubik_in_current in range(len(self.current_set)):
            for number_of_kubik_in_heap in range(len(self.heap)):
                if (self.current_set[number_of_kubik_in_current].column == self.heap[
                    number_of_kubik_in_heap].column) and (
                        self.current_set[number_of_kubik_in_current].row == self.heap[number_of_kubik_in_heap].row):
                    check = True
        # print('check = ', check)
        return check

    def game_restart(self):
        self.tetris_window.label_game_status['text'] = 'game rest'
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
        self.tetris_window.root.after(1000, self.move_down)
