highlighted = {"x": 0, "y": 0}
t1 = {"x": 3, "y": 3}
t2 = {"x": 5, "y": 5}
t1_complete = False
t2_complete = False

import time 

while True:
    time.sleep(0.5)
    if highlighted != t1 or t1_complete:
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
    else:
        t1_complete = True
    
    if highlighted != t2  or t2_complete:
        if highlighted["x"] < t2["x"]:
            highlighted["x"] += 1
            print(f"up: {highlighted}")
        elif highlighted["x"] > t2["x"]:
            highlighted["x"] -= 1
            print(f"down: {highlighted}")
        elif highlighted["y"] > t2["y"]:
            highlighted["y"] -= 1
            print(f"left: {highlighted}")
        elif highlighted["y"] < t2["y"]:
            highlighted["y"] += 1
            print(f"right: {highlighted}")
    else:
        t2_complete = True
