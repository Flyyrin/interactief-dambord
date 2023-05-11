import board
import neopixel 

pixels = neopixel.NeoPixel(board.D18, 128)


pixels[20] = (255,255,255)