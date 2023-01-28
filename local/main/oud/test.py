# # from boardFunctions import LED_setTile, readController, consolePrint
# # import random
# # from time import sleep

# # while True: 
# #     x = random.randint(0,8)
# #     y = random.randint(0,8)
# #     LED_setTile(x,y, "w")
# #     sleep(1)

# # LED_clear()

# str1 = ""
# for i in reversed(range(64)):
#     str1 += "{b[" + str(i) + "]} "
# print(str1)

string = "{b[63]} {b[62]} {b[61]} {b[60]} {b[59]} {b[58]} {b[57]} {b[56]} "
items = string.split(" ")
items.reverse()
new_str = ""
for item in items:
    new_str += item + " "

print(new_str)