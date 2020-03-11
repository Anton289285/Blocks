from window import *
game_tetris = Game()

game_tetris.tetris_window.root.bind('<Left>', game_tetris.move_left)
game_tetris.tetris_window.root.bind('<Right>', game_tetris.move_right)
game_tetris.tetris_window.root.bind('<Down>', game_tetris.rotate_right)
game_tetris.tetris_window.root.bind('<Up>', game_tetris.rotate_left)
game_tetris.tetris_window.root.bind('<r>', game_tetris.game_restart)
game_tetris.tetris_window.root.bind('<R>', game_tetris.game_restart)
game_tetris.tetris_window.root.bind('<KeyPress - p>', game_tetris.pause)
game_tetris.tetris_window.root.bind('<KeyPress - P>', game_tetris.pause)
game_tetris.tetris_window.root.bind('<space>', game_tetris.move_down_with_key)

game_tetris.number_of_current_set = randint(1, 7)
game_tetris.new_current_set()

game_tetris.number_of_next_set = randint(1, 7)
game_tetris.new_next_set()
game_tetris.move_down()

mainloop()
