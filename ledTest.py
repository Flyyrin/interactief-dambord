import board
import neopixel 
import time

pixels = neopixel.NeoPixel(board.D18, 128, auto_write=False, brightness= 0.5)

countDown = False
ratio = 0
while True: 
    if countDown:
        ratio = ratio - 0.01
    else:
        ratio = ratio + 0.01
    for led in range(64):
        pixels[led * 2] = (round(127*ratio),0,round(255*ratio))
        pixels[led*2+1] = (round(127*ratio),0,round(255*ratio))
    if round(ratio, 2) == 0.1:
        countDown = False
    if round(ratio,2) == 1:
        countDown = True
    pixels.show()