import board
import neopixel 
import json
import random

LED_board_opt = []
chosenTile = 0
pixels = neopixel.NeoPixel(board.D18, 128)
with open('local/config.json') as boardConfig:
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