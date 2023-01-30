# # from boardFunctionsTest import readController

# # highlighted = {"x": 0, "y": 0}
# # selected = {"x": -1, "y": -1}

# # while True:
# #     controller = readController(1)
# #     if controller == "up":
# #         if highlighted["y"] < 8:
# #             highlighted["y"] += 1
# #     if controller == "down":
# #         if 0 < highlighted["y"]:
# #             highlighted["y"] -= 1
# #     if controller == "left":
# #         if 0 < highlighted["x"]:
# #             highlighted["x"] -= 1
# #     if controller == "right":
# #         if highlighted["x"] < 8:
# #             highlighted["x"] += 1
# #     if controller == "press":
# #         if selected == highlighted:
# #             selected = {"x": -1, "y": -1}
# #         selected = highlighted
# game_board = [
#     [2, 2, 2, 2],
#     [2, 2, 2, 2],
#     [2, 2, 2, 2],
#     [' ', ' ', ' ', ' '],
#     [' ', ' ', ' ', ' '],
#     [1, 1, 1, 1],
#     [1, 1, 1, 1],
#     [1, 1, 1, 1],
# ]

# for y in range(8):
#     for i, player in enumerate(game_board[y]):
#         if y % 2 == 0: # if border columns
#             x = i * 2
#         else: # else altering columns
#             x = i * 2 + 1
#         print(x, y, player)

# https://pypi.org/project/imparaai-checkers/
# sudo apt-get install chromium-chromedriver

from selenium import webdriver

options = webdriver.ChromeOptions()
# options.add_argument('--headless')

driver = webdriver.Chrome('local\main\brainstorm\chromedriver.exe', chrome_options=options)

driver.get(r"C:\Users\bounc\Documents\GitHub\GIP-2022-2023\local\main\brainstorm\gui\index.html")
driver.maximize_window()

input()