from gpiozero import Button
import board
import neopixel 
import json
import random

# joystick
joystick_onder1 = Button(5, pull_up = 0) #rood
joystick_boven1 = Button(6, pull_up = 0) #zwart
joystick_links1 = Button(13, pull_up = 0) #blauw
joystick_rechts1 = Button(23, pull_up = 0) #groen
joystick_button1 = Button(24, pull_up = 0) #wit
joystick_onder2 = Button(26, pull_up = 0) #rood
joystick_boven2 = Button(21, pull_up = 0) #zwart
joystick_links2 = Button(20, pull_up = 0) #blauw
joystick_rechts2 = Button(16, pull_up = 0) #groen
joystick_button2 = Button(19, pull_up = 0) #wit
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

    any_pressed = False
    while not any_pressed:
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

# leds
LED_board_opt = []
chosenTile = 0
pixels = neopixel.NeoPixel(board.D18, 128)

with open('local/main/config.json') as boardConfig:
    BOARDCONFIG = json.load(boardConfig)
    board = dict(BOARDCONFIG["board"])

def LEDboardController(tileList):
    for tile in tileList:
        if tile not in LED_board_opt:
            LED_board_opt.append(tile)
            x = tile['x']
            y = tile['y']
            new_x = x
            new_y = y
            cell = BOARDCONFIG["board"][f"({new_x},{new_y})"]
            led1 = cell*2
            led2 = cell*2+1
            tile_color = eval(BOARDCONFIG["colors"][tile["content"]])
            pixels[led1] = tile_color
            pixels[led2] = tile_color
            with open('console.txt', 'a') as console:
                console.write(f"[LED_CONTROLLER] set cell {cell} to {tile['content']} = {tile_color}\n")
    LED_board_opt.clear()

LED_board_dict = {}
LED_board = []
def LED_setTile(x,y,content):
    try:
        old_content = LED_board_dict[f"({x},{y})"]
        if old_content != content:
            LED_board.append({
                "x": x,
                "y": y,
                "content": content.replace(" ","e")
            })
    except:
        LED_board.append({
            "x": x,
            "y": y,
            "content": content.replace(" ","e")
        })
                 
    LED_board_dict[f"({x},{y})"] = content
    LEDboardController(LED_board)
    LED_board.clear()

def LED_clear():
    for x in range(8):
        for y in range(8):
            LED_setTile(x,y,"e")

# console print
def consolePrint(text):
    with open('console.txt', 'a') as console:
        console.write(f"{text}\n")