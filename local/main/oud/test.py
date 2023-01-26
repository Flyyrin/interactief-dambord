# from boardFunctions import LED_setTile, readController, consolePrint
# import random
# from time import sleep

# while True: 
#     x = random.randint(0,8)
#     y = random.randint(0,8)
#     LED_setTile(x,y, "w")
#     sleep(1)

# LED_clear()

str = ""
for i in reversed(range(32)):
    str += f"{i+1}, 0, "
print(str)