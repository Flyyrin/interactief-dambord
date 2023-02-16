# # # # from boardFunctions import LED_setTile, readController, consolePrint
# # # # import random
# # # # from time import sleep

# # # # while True: 
# # # #     x = random.randint(0,8)
# # # #     y = random.randint(0,8)
# # # #     LED_setTile(x,y, "w")
# # # #     sleep(1)

# # # # LED_clear()

# # # str1 = ""
# # # for i in reversed(range(64)):
# # #     str1 += "{b[" + str(i) + "]} "
# # # print(str1)

# # string = "{b[63]} {b[62]} {b[61]} {b[60]} {b[59]} {b[58]} {b[57]} {b[56]} "
# # items = string.split(" ")
# # items.reverse()
# # new_str = ""
# # for item in items:
# #     new_str += item + " "

# # print(new_str)

# dicti =  {
#         "1": 0,
#         "2": 2,
#         "3": 4,
#         "4": 6,

#         "5": 14,
#         "6": 12,
#         "7": 10,
#         "8": 8,

#         "9": 16,
#         "10" : 18,
#         "11" : 20,
#         "12" : 22,

#         "13" : 30,
#         "14" : 28,
#         "15" : 26,
#         "16" : 24,

#         "17" : 32,
#         "18" : 34,
#         "19" : 36,
#         "20" : 38,

#         "21" : 46,
#         "22" : 44,
#         "23" : 42,
#         "24" : 40,

#         "25" : 48,
#         "26" : 50,
#         "27" : 52,
#         "28" : 54,

#         "29" : 62,
#         "30" : 60,
#         "31" : 58,
#         "32" : 56
#     }

# secdict = {}

# for key, value in dicti.items():
#     secdict[key] = value + 1

# print(secdict)

for i in range(32,64):
    print(i)