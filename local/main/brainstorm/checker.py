from checkers.game import Game
from controller import readController
from board import color, refresh
import json
# https://pypi.org/project/imparaai-checkers/

with open(r'local\main\brainstorm\layout.json') as layoutFile:
    layout = json.load(layoutFile)

board = {}
old_board = {}
def color(tile, color):
    global board
    board[tile] = color

def refresh():
    global board
    global old_board
    for tile, color in board.items():
        try:
            if old_board[tile] != color:
                led1 = tile*2
                led2 = tile*2+1
                print(f"{tile}: {color}")

        except:
            led1 = tile*2
            led2 = tile*2+1
            print(f"{tile}: {color}")
    
    old_board = dict(board)

def startGame():
    game = Game()
    player = game.whose_turn()
    global layout
    
    selected = 0
    highlighted = {"x": 0, "y": 0}
    while not game.is_over():
        controller = readController(player)

        for i in range(64):
            color(i, "e")
        pieces = []
        for piece in game.board.pieces:
            color(layout['game'][str(piece.position)], piece.player)
            pieces.append(piece.position)

        empty = [x for x in [*range(1,33)] if x not in set(pieces)]    
        for position in empty:
            color(layout['game'][str(position)], "e")

        if controller == "up":
            if highlighted["y"] < 7:
                highlighted["y"] += 1
        if controller == "down":
            if 0 < highlighted["y"]:
                highlighted["y"] -= 1
        if controller == "left":
            if 0 < highlighted["x"]:
                highlighted["x"] -= 1
        if controller == "right":
            if highlighted["x"] < 7:
                highlighted["x"] += 1
        highlighted_tile = layout["board"][f"({highlighted['x']},{highlighted['y']})"]

        if controller == "press":
            if highlighted_tile in layout["game"].values():
                new_selected = [k for k, v in layout["game"].items() if v == highlighted_tile][0]
                if selected == new_selected:
                    selected = 0
                else:
                    selected = new_selected
                    color(highlighted_tile, "c")
        color(highlighted_tile, "h")

        print()
        refresh()
        print(highlighted)


    print(game.get_winner())

startGame()