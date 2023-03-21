highlighted = {"x": 0, "y": 0}
t1 = {"x": 3, "y": 3}
t2 = {"x": 5, "y": 5}

import time 

while True:
    time.sleep(0.5)
    if highlighted != t1:
        if highlighted["x"] < t1["x"]:
            highlighted["x"] += 1
            print(f"up: {highlighted}")
        elif highlighted["x"] > t1["x"]:
            highlighted["x"] -= 1
            print(f"down: {highlighted}")
        elif highlighted["y"] > t1["y"]:
            highlighted["y"] -= 1
            print(f"left: {highlighted}")
        elif highlighted["y"] < t1["y"]:
            highlighted["y"] += 1
            print(f"right: {highlighted}")        