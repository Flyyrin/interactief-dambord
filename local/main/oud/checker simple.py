from checkers.game import Game
from boardFunctionsTest import readController
# https://pypi.org/project/imparaai-checkers/

def startGame():
    game = Game()
    player = game.whose_turn()
    selected = 0
    highlighted = 1
    board_highlighted = 1
    while not game.is_over():
        controller = readController(game.whose_turn())
        if controller == "up":
            if (board_highlighted + 8) <= 64:
                board_highlighted += 8
                highlighted += 4
        if controller == "down":
            if (board_highlighted - 8) >= 1:
                board_highlighted -= 8
                highlighted -= 4
        if controller == "left":
            if (board_highlighted + 1) <= 64 :
                board_highlighted += 1
                highlighted += 0.5
        if controller == "right":
            if (board_highlighted - 1) >= 1:
                board -= 1
                highlighted -= 0.5
        if controller == "press":
            if highlighted == selected:
                selected = 0
            else:
                selected = highlighted

            if selected != 0:
                board[selected] = "c"
            board[board_highlighted] = "h"

        print(f"highlighted = {highlighted}")
        print(f"selected = {selected}")
  

startGame()