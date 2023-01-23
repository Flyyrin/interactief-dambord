import board
import neopixel 
import json
import random

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