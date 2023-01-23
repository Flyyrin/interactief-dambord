from LEDboardController import LED_setTile, LED_clear
import random
from time import sleep

while True: 
    x = random.randint(0,8)
    y = random.randint(0,8)
    LED_setTile(x,y, "w")
    sleep(1)

LED_clear()