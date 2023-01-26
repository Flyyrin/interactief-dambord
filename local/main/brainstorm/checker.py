from checkers.game import Game
from controller import readController
import json
# https://pypi.org/project/imparaai-checkers/

with open(r'local\main\brainstorm\layout.json') as layoutFile:
    layout = json.load(layoutFile)

def startGame():
    game = Game()
    player = game.whose_turn()
    global layout

    selected = 0
    highlighted = {"x": 0, "y": 0}
    while not game.is_over():
        controller = readController(player)

        pieces = []
        for piece in game.board.pieces:
            print(f"Turn on {layout['game'][str(piece.position)]} with color {piece.player}")
            pieces.append(piece.position)

        empty = [x for x in [*range(1,33)] if x not in set(pieces)]    
        for position in empty:
            print(f"Turn on {layout['game'][str(position)]} with color empty")

        if controller == "up":
            if highlighted["y"] < 7:
                highlighted["y"] += 1
        if controller == "down":
            if 0 <= highlighted["y"]:
                highlighted["y"] -= 1
        if controller == "left":
            if 0 <= highlighted["x"]:
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
                    print(f"Turn on {highlighted_tile} with color empty")
                else:
                    selected = new_selected
                    print(f"Turn on {highlighted_tile} with color selected")
        print(f"Turn on {highlighted_tile} with color highlight")

    print(game.get_winner())

startGame()