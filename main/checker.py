"""
Dit is de kern van het damspel, hier wordt de game en de webInterface vanuit bestuurd.
"""
# het inladen van de nodige modules
from checkers.game import Game
from controller import readController
import json
from queue import Queue
from webInterface import startWebInterface
from algorithm import getBestMove
import threading
import requests
import time
import datetime
import random
import board
import neopixel 

# stel de neopixel library in en  laad de json bestanden in
# deze json bestanden bevatten de kleuren voor het dambord en de layout voor het dambord met coördinaten
pixels = neopixel.NeoPixel(board.D18, 128, auto_write=False,brightness = 0.7)

with open(r'/home/rpi/Documents/GIP-2022-2023/main/json/config.json') as configFile:
    config = json.load(configFile)

with open(r'/home/rpi/Documents/GIP-2022-2023/main/json/layout.json') as layoutFile:
    layout = json.load(layoutFile)

# aanmaken van benodigden variabelen
show_moves = False
ai = False
difficult = False
cp1 = "red"
cp2 = "purple"
URL = "http://flyyrin.pythonanywhere.com/game"

# aanmaken van 3 dictonaries, playerData, boardData en gameData
# playerData slaat de gegevens van beide spelers op (naam en kleur)
# boardData bewaart de posities van ieder damstuk
# gameData slaat de gegevens op van de huidige game (of er een spel gespeeld wordt, hoeveel stukken er nog over zijn...)
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

boardData = {}

gameData = {
    "playing": 0,
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

# functie om de gegevens van de game te posten naar de pythonanywhere server
# op deze manier wordt er gepost wanneer er iemand wint en wie er wint, de posities op het dambord, als het spel gestopt wordt...
def postNoWait(URL, params, json):
    requests.post(url = URL, params = params, json = json)

# aanmaken van de dictonaries board en old board en een color functie
# de functie is om een vakje van het board te kleuren naar een bepaalde kleur. De positie en kleur worden doorgegeven als parameter
board = {}
old_board = {}
def color(tile, color):
    global board
    board[tile] = color

# functie om de bijbehorende kleuren van ieder vak toe te passen op het dambord 
# hiermee wordt de board dictonary doorlopen, als de kleur bij een speler hoort, krijgt dit vak de kleurwaarde die de speler gekozen heeft
# hoort de kleur niet bij een speler, wordt de waarde van de kleur uit het config bestand gehaald met vooraf aangegeven kleuren en toegekend aan het vakje
# hierna wordt ieder vakje aangepast naar de juiste kleurwaarde en zal deze huidige configuratie weer opgeslagen worden in een dictionary
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
        try:
            if old_board[tile] != color:
                led1 = tile*2
                led2 = tile*2+1
                pixels[led1] = tile_color
                pixels[led2] = tile_color
        except:
            led1 = tile*2
            led2 = tile*2+1
            pixels[led1] = tile_color
            pixels[led2] = tile_color
    old_board = dict(board)
    pixels.show()

# functie om de huidige board vakken en kleuren om te zetten naar de dictonary boardData
def refreshLive():
    global board
    global boardData
    for tile, color in board.items():
        boardData[tile] = color

# functie om de game te starten, hierin wordt alle informatie doorgeven die gekozen en aangepast is door de speler(s)
# deze informatie bestaat uit of de speler assists wil, of de speler
def startGame(queue):
    global layout
    global show_moves
    global ai
    global gameData
    global boardData
    global playerData
    global difficult
    global cp1,cp2

    start_time = datetime.datetime.now()
    game = Game()
    moves = []   
    history = []
    selected = 0
    highlighted = {"x": 0, "y": 0}
    selected_tile = False
    playing = True
    startup = True
    moved = False
    while playing:
        winner = game.get_winner()
        if winner:
            requests.post(url = URL, params = {"type": "winner"}, json = {"winner": winner})
            winData = dict(playerData)
            winData["winner"] = winner  
            winData["date"] = int(time.time() * 1000)
            winData["time"] = str(datetime.timedelta(0, int((datetime.datetime.now() - start_time).total_seconds())))[2:]
            winData["history"] = history
            requests.post(url = URL+"s" , json = winData)
            playing = False

            if winner == 1:
                r,g,b = eval(config["colors"][playerData["player1"]["color"]])
            elif winner == 2:
                r,g,b = eval(config["colors"][playerData["player2"]["color"]])

            on = []
            for i in range(64):
                on.append(i)
            
            while True:
                if len(on) != 0:
                    led = random.choice(on)
                    on.remove(led)
                    pixels[led * 2] = (r,g,b)
                    pixels[led*2+1] = (r,g,b)
                    pixels.show()
                    time.sleep(0.01)
                else: 
                    time.sleep(0.5)
                    break

            countDown = True
            ratio = 1
            waiting = True
            while waiting: 
                if countDown:
                    ratio = ratio - 0.01
                else:
                    ratio = ratio + 0.01
                for led in range(64):
                    pixels[led * 2] = (round(r*ratio),round(g*ratio),round(b*ratio))
                    pixels[led*2+1] = (round(r*ratio),round(g*ratio),round(b*ratio))
                if round(ratio, 2) == 0.1:
                    countDown = False
                if round(ratio,2) == 1:
                    countDown = True
                pixels.show()  

                try:
                    data = queue.get_nowait()
                    if data == "stop":
                        for i in range(32):
                            color(i, "red")
                        for i in range(32,64):
                            color(i, "purple")
                        refresh()
                        cp1,cp2 = "red","purple"
                        waiting = False
                        playing = False
                        exit()
                    if data == "exit":
                        for i in range(64):
                            color(i, "e")
                        refresh()
                        waiting = False
                        playing = False
                        exit()
                except:
                    pass

        player = game.whose_turn()
        controller = readController(player)

        if startup:
            gameData["playing"] = game.whose_turn()
            gameData["np1"] = playerData["player1"]["name"]
            gameData["np2"] = playerData["player2"]["name"]
            gameData["cp1"] = playerData["player1"]["color"]
            gameData["cp2"] = playerData["player2"]["color"]
            gameData["board"] = boardData
            requests.post(url = URL, params = {"type": "gameData"}, json = {"gameData": gameData})
            moved = True
            controller = "-"
            startup = False


            tiles = []
            for tile in range(64):
                if tile not in layout["game"].values() or tile in [31,29,27,25,33,35,37,39]:
                    tiles.append(tile)
       


            print(tiles)
            ratio = 1
            while True: 
                ratio = ratio - 0.01
                for led in range(32):
                    if led in tiles:
                        r,g,b = eval(config["colors"][playerData["player1"]["color"]])
                        pixels[led * 2] = (round(r*ratio),round(g*ratio),round(b*ratio))
                        pixels[led*2+1] = (round(r*ratio),round(g*ratio),round(b*ratio))
                for led in range(32,64):
                    if led in tiles:
                        r,g,b = eval(config["colors"][playerData["player2"]["color"]])
                        pixels[led * 2] = (round(r*ratio),round(g*ratio),round(b*ratio))
                        pixels[led*2+1] = (round(r*ratio),round(g*ratio),round(b*ratio))
                
                if round(ratio,2) == 0:
                    break
                pixels.show()  




        try:
            data = queue.get_nowait()
            if data == "stop":
                # for i in range(32):
                #     color(i, "red")
                # for i in range(32,64):
                #     color(i, "purple")
                # refresh()
                
                old_color1 = list(eval(config["colors"][str(cp1)]))
                old_color2 = list(eval(config["colors"][str(cp2)]))
                cp1,cp2 = "red","purple"
                new_color1 = list(eval(config["colors"][str(cp1)]))
                new_color2 = list(eval(config["colors"][str(cp2)]))

                p1_tiles = []
                p2_tiles = []
                p1k_tiles = []
                p2k_tiles = []
                h = []
                e = []
                c = []
                p = []

                for tile, color in boardData:
                    if color == 1:
                        p1_tiles.append(tile)
                    elif color == 2:
                        p2_tiles.append(tile)
                    elif color == 3:
                        p1k_tiles.append(tile)
                    elif color == 4:
                        p2k_tiles.append(tile)
                    elif color == "h":
                        h.append(tile)
                    elif color == "c":
                        c.append(tile)
                    elif color == "p":
                        p.append(tile)
                    elif color == "e":
                        e.append(tile)
                
                # if new_color1 != old_color1:
                #     end_rgb = new_color1
                #     start_rgb = old_color1
                #     led_range = range(32)
                # if new_color2 != old_color2:
                #     end_rgb = new_color2
                #     start_rgb = old_color2
                #     led_range = range(32,64)

                # if led_range: 
                #     # Calculate the maximum difference in any one color channel
                #     max_diff = max(abs(end_rgb[i] - start_rgb[i]) for i in range(3))

                #     # Define the number of steps in the transition based on the maximum difference
                #     num_steps = max_diff + 1

                #     # Calculate the step size for each color channel
                #     r_step = (end_rgb[0] - start_rgb[0]) / num_steps
                #     g_step = (end_rgb[1] - start_rgb[1]) / num_steps
                #     b_step = (end_rgb[2] - start_rgb[2]) / num_steps

                #     # Loop through each step and calculate the new RGB value
                #     for i in range(num_steps):
                #         r = int(start_rgb[0] + (i * r_step))
                #         g = int(start_rgb[1] + (i * g_step))
                #         b = int(start_rgb[2] + (i * b_step))
                #         for led in led_range:
                #             pixels[led * 2] = (r,g,b)
                #             pixels[led * 2 + 1] = (r,g,b)
                #         pixels.show()

                #     for led in led_range:
                #         pixels[led * 2] = end_rgb
                #         pixels[led * 2 + 1] = end_rgb
                #         pixels.show()

      
                # Calculate the maximum difference in any one color channel
                max_diff = max(abs(new_color1[i] - old_color1[i]) for i in range(3))

                # Define the number of steps in the transition based on the maximum difference
                num_steps = max_diff + 1

                # Calculate the step size for each color channel
                r_step = (new_color1[0] - old_color1[0]) / num_steps
                g_step = (new_color1[1] - old_color1[1]) / num_steps
                b_step = (new_color1[2] - old_color1[2]) / num_steps

                # Loop through each step and calculate the new RGB value
                for i in range(num_steps):
                    r = int(old_color1[0] + (i * r_step))
                    g = int(old_color1[1] + (i * g_step))
                    b = int(old_color1[2] + (i * b_step))
                    for led in p1_tiles:
                        pixels[led * 2] = (r,g,b)
                        pixels[led * 2 + 1] = (r,g,b)
                    pixels.show()

                for led in p1_tiles:
                    pixels[led * 2] = new_color1
                    pixels[led * 2 + 1] = new_color1
                    pixels.show()






                playing = False
                exit()
            if data == "exit":
                for i in range(64):
                    color(i, "e")
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

        if ai and player == 2:
            if difficult:
                move = getBestMove(game)
            else:
                move = random.choice(game.get_possible_moves())
            time.sleep(3)
            controller = "-"
            game.move(move)
            moved = True
        else:
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
                        if move in game.get_possible_moves():
                            selected = 0
                            selected_tile = False
                            moves.clear()
                            game.move(move)
                            moved = True
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
                                    if selected == move[0]:
                                        moves.append(move)

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
            gameData["playing"] = game.whose_turn()
            gameData["board"] = boardData
            threading.Thread(target=postNoWait, args=(URL, {"type": "gameData"}, {"gameData": gameData})).start()
     
        if moved:
            moved = False
            historyBoard = {}
            for i in range(64):
                historyBoard[i] = "e"
            for piece in game.board.pieces:
                if piece.position != None:
                    player_piece = piece.player
                    if piece.king:
                        player_piece += 2
                    historyBoard[layout['game'][str(piece.position)]] = player_piece
            history.append(historyBoard)       
        
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
                color(layout['game'][str(move[1])], "p")
            if selected_tile:
                color(selected_tile, "c")
            color(highlighted_tile, "h")
            refresh()
            refreshLive()

# functie die blijft runnen tijdens het spel. hierin krijgt het dambord de basiskleuren, wordt de informatie zoals speelhulp en AI ontvangen van het start scherm
# en wordt het spel hierop aangepast
def setupGame(queue):
    ratio = 0
    while True: 
        ratio = ratio + 0.01
        for led in range(32):
            r,g,b = eval(config["colors"]["red"])
            pixels[led * 2] = (round(r*ratio),round(g*ratio),round(b*ratio))
            pixels[led*2+1] = (round(r*ratio),round(g*ratio),round(b*ratio))
        for led in range(32,64):
            r,g,b = eval(config["colors"]["purple"])
            pixels[led * 2] = (round(r*ratio),round(g*ratio),round(b*ratio))
            pixels[led*2+1] = (round(r*ratio),round(g*ratio),round(b*ratio))
        
        if round(ratio,2) == 1:
            break
        pixels.show()  

    while True:
        try:
            global cp1,cp2
            data = queue.get()
            if "start" in data:
                global playerData
                global show_moves
                global ai
                global difficult
                np1,np2,cp1,cp2,assist,opponent_ai,difficult_ai = data.split("|")[1].split("&")
                playerData["player1"]["name"] = np1
                playerData["player2"]["name"] = np2
                playerData["player1"]["color"] = cp1
                playerData["player2"]["color"] = cp2
                if assist == "true":
                    show_moves = True
                if assist == "false":
                    show_moves = False
                if opponent_ai == "true":
                    ai = True
                if opponent_ai == "false":
                    ai = False
                if difficult_ai == "true":
                    difficult = True
                if difficult_ai == "false":
                    difficult = False
                startGame(queue)

            if "color" in data:
                cp1,cp2 = data.split("|")[1].split("&")
                new_color1 = list(eval(config["colors"][str(cp1)]))
                new_color2 = list(eval(config["colors"][str(cp2)]))
                old_color1 = pixels[0]
                old_color2 = pixels[127]
                if new_color1 != old_color1:
                    end_rgb = new_color1
                    start_rgb = old_color1
                    led_range = range(32)
                if new_color2 != old_color2:
                    end_rgb = new_color2
                    start_rgb = old_color2
                    led_range = range(32,64)

                if led_range: 
                    # Calculate the maximum difference in any one color channel
                    max_diff = max(abs(end_rgb[i] - start_rgb[i]) for i in range(3))

                    # Define the number of steps in the transition based on the maximum difference
                    num_steps = max_diff + 1

                    # Calculate the step size for each color channel
                    r_step = (end_rgb[0] - start_rgb[0]) / num_steps
                    g_step = (end_rgb[1] - start_rgb[1]) / num_steps
                    b_step = (end_rgb[2] - start_rgb[2]) / num_steps

                    # Loop through each step and calculate the new RGB value
                    for i in range(num_steps):
                        r = int(start_rgb[0] + (i * r_step))
                        g = int(start_rgb[1] + (i * g_step))
                        b = int(start_rgb[2] + (i * b_step))
                        for led in led_range:
                            pixels[led * 2] = (r,g,b)
                            pixels[led * 2 + 1] = (r,g,b)
                        pixels.show()

                    for led in led_range:
                        pixels[led * 2] = end_rgb
                        pixels[led * 2 + 1] = end_rgb
                        pixels.show()
   
            if data == "stop":
                exit()
            if data == "exit":
                ratio = 1
                while True: 
                    ratio = ratio - 0.01
                    for led in range(32):
                        r,g,b = eval(config["colors"][str(cp1)])
                        pixels[led * 2] = (round(r*ratio),round(g*ratio),round(b*ratio))
                        pixels[led*2+1] = (round(r*ratio),round(g*ratio),round(b*ratio))
                    for led in range(32,64):
                        r,g,b = eval(config["colors"][str(cp2)])
                        pixels[led * 2] = (round(r*ratio),round(g*ratio),round(b*ratio))
                        pixels[led*2+1] = (round(r*ratio),round(g*ratio),round(b*ratio))
                    
                    if round(ratio,2) == 1:
                        break
                    pixels.show()  


                exit()
        except:
            pass

queue = Queue()
gameThread = threading.Thread(target=setupGame, args=(queue,))
gameThread.start()
startWebInterface(queue)