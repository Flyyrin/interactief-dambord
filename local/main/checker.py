from checkers.game import Game
from controller import readController
import json
from queue import Queue
from web import startWeb
import threading
import requests
import time
import board
import neopixel 
# https://pypi.org/project/imparaai-checkers/

pixels = neopixel.NeoPixel(board.D18, 128)

URL = "http://flyyrin.pythonanywhere.com/game"

with open(r'/home/rpi/Documents/GIP-2022-2023/local/main/json/config.json') as configFile:
    config = json.load(configFile)

with open(r'/home/rpi/Documents/GIP-2022-2023/local/main/json/layout.json') as layoutFile:
    layout = json.load(layoutFile)

show_moves = True


playerData = {
    "player1": {
        "name": "",
        "color": ""
    },
    "player2": {
        "name": "",
        "color": ""
    }
}

gameData = {
    "current-player": 0,
    "pieces": {
        "player1": {
            "pieces": 12,
            "kings": 0,
            "captured": 0
        },
        "player2": {
            "pieces": 12,
            "kings": 0,
            "captured": 0
        }
    }
}

board = {}
old_board = {}
def color(tile, color):
    global board
    board[tile] = color

def refresh():
    global board
    global old_board
    for tile, color in board.items():
        if color == 1:
            tile_color = eval(config["colors"][playerData["player1"]["color"]])
        elif color == 2:
            tile_color = eval(config["colors"][playerData["player2"]["color"]])
        elif color == 3:
            tile_color = eval(config["colors"]["king-"+playerData["player1"]["color"]])
        elif color == 4:
            tile_color = eval(config["colors"]["king-"+playerData["player2"]["color"]])
        else:
            tile_color = eval(config["colors"][str(color)])
        print(tile_color)
        try:
            if old_board[tile] != color:
                led1 = tile*2
                led2 = tile*2+1
                pixels[led1] = tile_color
                pixels[led2] = tile_color
                print(f"{tile}: {color}")

        except:
            led1 = tile*2
            led2 = tile*2+1
            pixels[led1] = tile_color
            pixels[led2] = tile_color
            print(f"{tile}: {color}")
    
    old_board = dict(board)

    b = board
    print(f"""     
        {b[56]} {b[57]} {b[58]} {b[59]} {b[60]} {b[61]} {b[62]} {b[63]} 
        {b[55]} {b[54]} {b[53]} {b[52]} {b[51]} {b[50]} {b[49]} {b[48]} 
        {b[40]} {b[41]} {b[42]} {b[43]} {b[44]} {b[45]} {b[46]} {b[47]} 
        {b[39]} {b[38]} {b[37]} {b[36]} {b[35]} {b[34]} {b[33]} {b[32]} 
        {b[24]} {b[25]} {b[26]} {b[27]} {b[28]} {b[29]} {b[30]} {b[31]} 
        {b[23]} {b[22]} {b[21]} {b[20]} {b[19]} {b[18]} {b[17]} {b[16]} 
        {b[8]} {b[9]} {b[10]} {b[11]} {b[12]} {b[13]} {b[14]} {b[15]} 
        {b[7]} {b[6]} {b[5]} {b[4]} {b[3]} {b[2]} {b[1]} {b[0]}    
    """)

def startGame(queue):
    game = Game()
    global layout

    moves = []   
    selected = 0
    highlighted = {"x": 0, "y": 0}
    selected_tile = False
    playing = True
    startup = True
    while playing:
        winner = game.get_winner()
        if winner:
            requests.post(url = URL, params = {"type": "winner"}, json = {"winner": winner})
            winData = dict(playerData)
            winData["winner"] = winner  
            winData["date"] = int(time.time() * 1000)
            requests.post(url = URL+"s" , json = winData)
            playing = False
            for i in range(64):
                color(i, str(winner))
            refresh()
            exit()
        player = game.whose_turn()
        controller = readController(player)

        if startup:
            gameData["current-player"] = game.whose_turn()
            requests.post(url = URL, params = {"type": "gameData"}, json = {"gameData": gameData})
            controller = "-"
            startup = False

        try:
            if queue.get_nowait() == "stop":
                for i in range(64):
                    color(i, "c")
                refresh()
                playing = False
                exit()
        except:
            pass
        
        pieces = []
        player1pieces = []
        player2pieces = []
        for piece in game.board.pieces:
            if piece.position != None:
                pieces.append(piece.position)
                if piece.player == 1:
                    player1pieces.append(piece.position)
                if piece.player == 2:
                    player2pieces.append(piece.position)

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
                allowed = False
                new_selected = int([k for k, v in layout["game"].items() if v == highlighted_tile][0])
                if player == 1 and new_selected in player1pieces:
                    allowed = True
                if player == 2 and new_selected in player2pieces:
                    allowed = True
                if selected:
                    move = [selected, new_selected]
                    print(move)
                    if move in game.get_possible_moves():
                        selected = 0
                        selected_tile = False
                        moves.clear()
                        print("Posible move")
                        game.move(move)
                        # if game.whose_turn() == 1:
                        #     highlighted = {"x": 3, "y": 0}
                        # if game.whose_turn() == 2:
                        #     highlighted = {"x": 5, "y": 7}
                    print(game.get_possible_moves())
                if allowed:
                    if selected == new_selected:
                        selected = 0
                        selected_tile = False
                        moves.clear()
                    else:
                        moves.clear()
                        selected = new_selected
                        selected_tile = highlighted_tile
                        if show_moves:
                            for move in game.get_possible_moves():
                                if selected == move[0] or len(game.get_possible_moves()) == 1:
                                    moves.append(move)

            try:
                player1piecesAmount = 0
                player2piecesAmount = 0
                player1kingsAmount = 0
                player2kingsAmount = 0
                for piece in game.board.pieces:
                    if piece.position != None:
                        if piece.player == 1:
                            if piece.king:
                                player1kingsAmount += 1
                            else:
                                player1piecesAmount += 1
                        if piece.player == 2:
                            if piece.king:
                                player2kingsAmount += 1
                            else:
                                player2piecesAmount += 1
            
                gameData["pieces"]["player1"]["pieces"] = player1piecesAmount
                gameData["pieces"]["player2"]["pieces"] = player2piecesAmount
                gameData["pieces"]["player1"]["kings"] = player1kingsAmount
                gameData["pieces"]["player2"]["kings"] = player2kingsAmount
                gameData["pieces"]["player1"]["captured"] = 12 - (player2piecesAmount + player2kingsAmount)
                gameData["pieces"]["player2"]["captured"] = 12 - (player1piecesAmount + player1kingsAmount)
            except Exception as e:
                print(e)
            gameData["current-player"] = game.whose_turn()
            requests.post(url = URL, params = {"type": "gameData"}, json = {"gameData": gameData})
        
        
        if controller:
            for i in range(64):
                color(i, "e")
            for piece in game.board.pieces:
                if piece.position != None:
                    player_piece = piece.player
                    if piece.king:
                        player_piece += 2
                    color(layout['game'][str(piece.position)], player_piece)
            
            for move in moves:
                print(move)
                color(layout['game'][str(move[1])], "p")
            if selected_tile:
                color(selected_tile, "c")
            color(highlighted_tile, "h")

            refresh()

def setupGame(queue):
    for i in range(64):
        color(i, "c")
    refresh()
    while True:
        try:
            data = queue.get()
            if "start" in data:
                global playerData
                np1,np2,cp1,cp2 = data.split("|")[1].split("&")
                playerData["player1"]["name"] = np1
                playerData["player2"]["name"] = np2
                playerData["player1"]["color"] = cp1
                playerData["player2"]["color"] = cp2
                startGame(queue)
            if "color" in data:
                print("color 2")
                cp1,cp2 = data.split("|")[1].split("&")
                print(cp1,cp2)
                color1 = eval(config["colors"][str(cp1)])
                color2 = eval(config["colors"][str(cp2)])
                print(color1, color2)
                for i in range(32):
                    color(i, color1)
                for i in range(32,64):
                    color(i, color2)
        except:
            pass

queue = Queue()
gameThread = threading.Thread(target=setupGame, args=(queue,))
gameThread.start()
startWeb(queue)