import board
import neopixel 
import json
import time

pixels = neopixel.NeoPixel(board.D18, 128)

config = {
    "colors": {
        "e": "(0,0,0)",
        "h": "(255,255,255)",
        "c": "(0,255,255)",
        "p": "(255,122,0)",

        "red": "(255,0,0)",
        "king-red": "(100,0,0)",

        "blue": "(0,0,255)",
        "king-blue": "(0,0,100)",

        
        "green": "(0,255,0)",
        "king-green": "(0,100,0)",
        
        "yellow": "(255,255,0)",
        "king-yellow": "(127,127,0)",

        "purple": "(255,0,255)",
        "king-purple": "(100,0,100)",

        "king-ai": "(75,200,75)",
        "ai": "(50,205,50)"
    }
}

tile = 0
for color in config["colors"].values():
    print(color)
    led1 = tile*2
    led2 = tile*2+1
    pixels[led1] = eval(color)
    pixels[led2] = eval(color)
    tile += 1

while True:
    for color in config["colors"].values():
        for i in range(64):
            pixels[i] = eval(color)
        time.sleep(0.5)