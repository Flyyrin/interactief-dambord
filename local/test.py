from LEDboardController import LED_setTile, LED_clear

for x in range(8):
    for y in range(8):
        LED_setTile(x,y, "c")

LED_clear()