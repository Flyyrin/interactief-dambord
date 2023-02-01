from checkers.game import Game
from boardFunctionsTestSmooth import readController, updateLedBoard, chunks
# https://pypi.org/project/imparaai-checkers/

def expand(board):
    board_list = []
    for item in chunks(board, 8):
        row = []
        for piece in item.values():
            row.append(str(piece))
        row.reverse()
        board_list.append(row)
    board_list.reverse()
    for row in board_list[::2]:
        row.reverse()
    
    num = 1
    board_dict = {}
    for row_index, row in enumerate(board_list):
        for piece_index, piece in enumerate(row):
            board_dict[num] = board_list[row_index][piece_index]
            num += 1
    return board_dict

def shrink(position):
    return position/2

def startGame():
    game = Game()
    player = game.whose_turn()
    selected = 0
    highlighted = 1
    while not game.is_over():
        controller = readController(game.whose_turn())
        if controller == "up":
            if (highlighted + 4) <= 32:
                highlighted += 4
        if controller == "down":
            if (highlighted - 4) >= 1:
                highlighted -= 4
        if controller == "left":
            if (highlighted + 1) <= 32 :
                highlighted += 1
        if controller == "right":
            if (highlighted - 1) >= 1:
                highlighted -= 1
        if controller == "press":
            if highlighted == selected:
                selected = 0
            else:
                selected = highlighted

        print(f"highlighted = {highlighted}")
        print(f"selected = {selected}")

        board = {}
        for i in range(1, 33):
            board[i] = " "
        for piece in game.board.pieces:
            board[piece.position] = piece.player
        
        if selected != 0:
            board[selected] = "c"
        board[highlighted] = "h"

        updateLedBoard(board)  

startGame()