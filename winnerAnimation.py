import board
import neopixel 
import random
import time
pixels = neopixel.NeoPixel(board.D18, 128, auto_write=False)
on = []
for i in range(64):
    on.append(i)
    
while True:
    if len(on) is not 0:
        led = random.choice(on)
        print(led, on)
        on.remove(led)
        pixels[led * 2] = (0,0,255)
        pixels[led*2+1] = (0,0,255)
        time.sleep(0.01)
        pixels.show()
    else:
        time.sleep(0.5) 
        break
countDown = True
ratio = 1
while True: 
    if countDown:
        ratio = ratio - 0.01
    else:
        ratio = ratio + 0.01
    for led in range(64):
        pixels[led * 2] = (round(0*ratio),0,round(255*ratio))
        pixels[led*2+1] = (round(0*ratio),0,round(255*ratio))
    if round(ratio, 2) == 0.1:
        countDown = False
    if round(ratio,2) == 1:
        countDown = True
    pixels.show()