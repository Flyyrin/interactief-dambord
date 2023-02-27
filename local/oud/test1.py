import time
playerData = {
    "player1": {
        "name": "",
        "color": ""
    },
    "player2": {
        "name": "",
        "color": ""
    }
}

winner = 1
if winner:
    winData = dict(playerData)
    winData["winner"] = winner  
    winData["date"] = int(time.time() * 1000)
    print(winData)