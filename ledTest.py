import board
import neopixel 
import random

pixels = neopixel.NeoPixel(board.D18, 128)

while True:
    pixels[random.randint(0,127)] = (random.randint(0,254),random.randint(0,254),random.randint(0,254))