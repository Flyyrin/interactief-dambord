from boardFunctionsV2 import readController, showboard

highlighted = {"x": 0, "y": 0}
selected = {"x": -1, "y": -1}

while True:
    board = [
    [" ", " ", " ", " ", " ", " ", " ", " ", ],
    [" ", " ", " ", " ", " ", " ", " ", " ", ],
    [" ", " ", " ", " ", " ", " ", " ", " ", ],
    [" ", " ", " ", " ", " ", " ", " ", " ", ],
    [" ", " ", " ", " ", " ", " ", " ", " ", ],
    [" ", " ", " ", " ", " ", " ", " ", " ", ],
    [" ", " ", " ", " ", " ", " ", " ", " ", ],
    [" ", " ", " ", " ", " ", " ", " ", " ", ],
    ]
    controller = readController(1)
    if controller == "up":
        if highlighted["y"] < 8:
            highlighted["y"] += 1
    if controller == "down":
        if 0 < highlighted["y"]:
            highlighted["y"] -= 1
    if controller == "left":
        if 0 < highlighted["x"]:
            highlighted["x"] -= 1
    if controller == "right":
        if highlighted["x"] < 8:
            highlighted["x"] += 1
    if controller == "press":
        if selected == highlighted:
            selected = {"x": -1, "y": -1}
        selected = highlighted

    print(highlighted)


