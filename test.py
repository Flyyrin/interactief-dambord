import threading
import time
import board
import neopixel 

pixels = neopixel.NeoPixel(board.D18, 128)

r1 = 0
g1 = 0
b1 = 0

r2 = 100
g2 = 255
b2 = 255


def changered(red,speed):
    global r1, g1, b1
    if red > r1:
        for x in range (r1,red):
            print(f"r: {x}")
            
            time.sleep(speed)
    else:
        down = r1 - red
        for x in range (0,down):
            print(f"r: {r1 - x}")
            time.sleep(speed)
    r1 = red

def changegreen(green,speed):
    global r1, g1, b1
    if(green > g1):
            for x in range (g1,green):
                print(f"g: {x}")
                time.sleep(speed)
    else:
            down = g1 - green
            for x in range (0,down):
                print(f"g: {g1 - x}")
                time.sleep(speed)
    g1 = green

def changeblue(blue,speed):
    global r1, g1, b1
    if(blue > b1):
            for x in range (b1,blue):
                print(f"b: {x}")
                time.sleep(speed)
    else:
            down = b1 - blue
            for x in range (0,down):
                print(f"b: {b1 - x}")
                time.sleep(speed)
    b1 = blue


if r2 == r1 or r2 == 0:
    rx = r1 + 1
else:
    rx = abs(r2-r1)
if g2 == g1 or g2 == 0:
    gx = g1 + 1
else:
    gx = abs(g2-g1)
if b2 == b1 or b2 == 0:
    bx = b1 + 1
else:
    bx = abs(b2-b1)

rs = 0.8/rx
gs = 0.8/gx
bs = 0.8/bx

threading.Thread(target=changered, args=(r2,rs)).start()
threading.Thread(target=changegreen, args=(g2,gs)).start()
threading.Thread(target=changeblue, args=(b2,bs)).start()
