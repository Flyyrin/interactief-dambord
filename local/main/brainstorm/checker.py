# https://pypi.org/project/imparaai-checkers/
# sudo apt-get install chromium-chromedriver
from checkers.game import Game
import json
import platform
import time
import os
import keyboard
from selenium import webdriver
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()

RPI = platform.system() != "Windows"
print(RPI)

if RPI:
    import neopixel
    import board
    from gpiozero import Button
        
#     from controller import readController
# else:
#     from kcontroller import readController

if RPI:
    options.add_argument('--headless')
    pixels = neopixel.NeoPixel(board.D18, 128)
    driver = webdriver.Chrome('chromedriverrpi.exe', chrome_options=options)
    joystick_onder1 = Button(5, pull_up = 0)
    joystick_boven1 = Button(6, pull_up = 0)
    joystick_links1 = Button(13, pull_up = 0)
    joystick_rechts1 = Button(23, pull_up = 0)
    joystick_button1 = Button(24, pull_up = 0)
    joystick_onder2 = Button(26, pull_up = 0)
    joystick_boven2 = Button(21, pull_up = 0)
    joystick_links2 = Button(20, pull_up = 0)
    joystick_rechts2 = Button(16, pull_up = 0)
    joystick_button2 = Button(19, pull_up = 0)
else:
    driver = webdriver.Chrome('chromedriver.exe', chrome_options=options)

with open(r'local\main\brainstorm\layout.json') as layoutFile:
    layout = json.load(layoutFile)

joystick_boven1_pressed = False
joystick_onder1_pressed = False
joystick_links1_pressed = False
joystick_rechts1_pressed = False
joystick_button1_pressed = False
joystick_boven2_pressed = False
joystick_onder2_pressed = False
joystick_links2_pressed = False
joystick_rechts2_pressed = False
joystick_button2_pressed = False

show_moves = True
colors = {
    "e": "(255,0,0)",
    "h": "(255,0,0)",
    "c": "(255,0,0)",
    "p": "(255,0,0)",
    "1": "(255,0,0)",
    "2": "(255,0,0)",
    "3": "(255,0,0)",
    "4": "(255,0,0)"
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
        tile_color = eval(colors[str(color)])
        try:
            if old_board[tile] != color:
                led1 = tile*2
                led2 = tile*2+1
                if RPI:
                    pixels[led1] = tile_color
                    pixels[led2] = tile_color
                print(f"{tile}: {color}")
        except:
            led1 = tile*2
            led2 = tile*2+1
            if RPI:
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
running = False
def startGame():
    game = Game()
    global layout
    global running

    running = True
    started = False
    moves = []   
    selected = 0
    highlighted = {"x": 0, "y": 0}
    selected_tile = False
    while not game.is_over() and running:
        player = game.whose_turn()
        if started:
            controller = readController(player)
        else:
            controller = False
        started = True

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
                    print(game.get_possible_moves())
                if allowed:
                    if selected == new_selected:
                        selected = 0
                        selected_tile = False
                        moves.clear()
                    else:
                        selected = new_selected
                        selected_tile = highlighted_tile
                        if show_moves:
                            for move in game.get_possible_moves():
                                if selected == move[0]:
                                    moves.append(move)

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

    winner = game.get_winner()
    if winner != None:
        print(f"{winner} won!")
    start()


def start():
    driver.get(os.path.join(os.getcwd(), "local/main/brainstorm/gui/start.html"))
    driver.maximize_window()
    while True:
        value = driver.find_element(By.CLASS_NAME, "start").get_attribute('value')
        if value == "True":
            name1 = driver.find_element(By.CLASS_NAME, "player1name").get_attribute('value')
            name2 = driver.find_element(By.CLASS_NAME, "player2name").get_attribute('value')
            color1 = driver.find_element(By.CLASS_NAME, "color1").get_attribute('value')
            color2 = driver.find_element(By.CLASS_NAME, "color2").get_attribute('value')
            driver.get(os.path.join(os.getcwd(), "local/main/brainstorm/gui/game.html"))
            startGame()
        time.sleep(1)

def readController(player):
    global joystick_boven1_pressed
    global joystick_onder1_pressed
    global joystick_links1_pressed
    global joystick_rechts1_pressed
    global joystick_button1_pressed
    global joystick_boven2_pressed
    global joystick_onder2_pressed
    global joystick_links2_pressed
    global joystick_rechts2_pressed
    global joystick_button2_pressed

    global running

    any_pressed = False
    if RPI:
        while not any_pressed:
            value = driver.find_element(By.CLASS_NAME, "stop").get_attribute('value')
            if value == "True":
                running = False
                return
            if player == 1:
                if joystick_boven1.is_pressed:
                    if not joystick_boven1_pressed:
                        joystick_boven1_pressed = True
                        any_pressed = True
                        return "up"
                else:
                    joystick_boven1_pressed = False

                if joystick_onder1.is_pressed:
                    if not joystick_onder1_pressed:
                        joystick_onder1_pressed = True
                        any_pressed = True
                        return "down"
                else:
                    joystick_onder1_pressed = False

                if joystick_links1.is_pressed:
                    if not joystick_links1_pressed:
                        joystick_links1_pressed = True
                        any_pressed = True
                        return "left"
                else:
                    joystick_links1_pressed = False
                    
                if joystick_rechts1.is_pressed:
                    if not joystick_rechts1_pressed:
                        joystick_rechts1_pressed = True
                        any_pressed = True
                        return "right"
                else:
                    joystick_rechts1_pressed = False
                
                if joystick_button1.is_pressed:
                    if not joystick_button1_pressed:
                        joystick_button1_pressed = True
                        any_pressed = True
                        return "press"
                else:
                    joystick_button1_pressed = False

            if player == 2:
                if joystick_boven2.is_pressed:
                    if not joystick_boven2_pressed:
                        joystick_boven2_pressed = True
                        any_pressed = True
                        return "up"
                else:
                    joystick_boven2_pressed = False

                if joystick_onder2.is_pressed:
                    if not joystick_onder2_pressed:
                        joystick_onder2_pressed = True
                        any_pressed = True
                        return "down"
                else:
                    joystick_onder2_pressed = False

                if joystick_links2.is_pressed:
                    if not joystick_links2_pressed:
                        joystick_links2_pressed = True
                        any_pressed = True
                        return "left"
                else:
                    joystick_links2_pressed = False
                    
                if joystick_rechts2.is_pressed:
                    if not joystick_rechts2_pressed:
                        joystick_rechts2_pressed = True
                        any_pressed = True
                        return "right"
                else:
                    joystick_rechts2_pressed = False
                
                if joystick_button2.is_pressed:
                    if not joystick_button2_pressed:
                        joystick_button2_pressed = True
                        any_pressed = True
                        return "press"
                else:
                    joystick_button2_pressed = False
    else:
        while not any_pressed:
            if True:
                value = driver.find_element(By.CLASS_NAME, "stop").get_attribute('value')
                if value == "True":
                    running = False
                    return
                if keyboard.is_pressed('w'):
                    if not joystick_boven1_pressed:
                        joystick_boven1_pressed = True
                        any_pressed = True
                        return "up"
                else:
                    joystick_boven1_pressed = False

                if keyboard.is_pressed('s'):
                    if not joystick_onder1_pressed:
                        joystick_onder1_pressed = True
                        any_pressed = True
                        return "down"
                else:
                    joystick_onder1_pressed = False

                if keyboard.is_pressed('a'):
                    if not joystick_links1_pressed:
                        joystick_links1_pressed = True
                        any_pressed = True
                        return "left"
                else:
                    joystick_links1_pressed = False
                    
                if keyboard.is_pressed('d'):
                    if not joystick_rechts1_pressed:
                        joystick_rechts1_pressed = True
                        any_pressed = True
                        return "right"
                else:
                    joystick_rechts1_pressed = False
                
                if keyboard.is_pressed('q'):
                    if not joystick_button1_pressed:
                        joystick_button1_pressed = True
                        any_pressed = True
                        return "press"
                else:
                    joystick_button1_pressed = False


start()