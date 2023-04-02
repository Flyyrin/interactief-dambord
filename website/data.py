import requests
import time

playerData = {
    "player1": {
        "name": "Rafael",
        "color": "blue"
    },
    "player2": {
        "name": "Romeo",
        "color": "green"
    }
}

gameData = {
    "playing": 0,
    "pieces": {
        "player1": {
            "pieces": 12,
            "kings": 0,
            "captured": 0
        },
        "player2": {
            "pieces": 12,
            "kings": 0,
            "captured": 0
        }
    },
    "board": {
        "1": 1, 
        "2": 1, 
        "3": 1, 
        "4": 1, 
        "5": 1, 
        "6": 1, 
        "7": 1, 
        "8": 1, 
        "9": 1, 
        "10": 1, 
        "11": 1, 
        "12": 1, 
        "13": "e", 
        "14": "e", 
        "15": "e", 
        "16": "e", 
        "17": "e", 
        "18": "e", 
        "19": "e", 
        "20": "e", 
        "21": 2, 
        "22": 2, 
        "23": 2, 
        "24": 2, 
        "25": 2, 
        "26": 2, 
        "27": 2, 
        "28": 2, 
        "29": 2, 
        "30": 2, 
        "31": 2, 
        "32": 2
    }
}

gameData["playing"] = 1
gameData["np1"] = playerData["player1"]["name"]
gameData["np2"] = playerData["player2"]["name"]
gameData["cp1"] = playerData["player1"]["color"]
gameData["cp2"] = playerData["player2"]["color"]
gameData["startTime"]= int(time.time() * 1000)
requests.post(url = "https://flyyrin.pythonanywhere.com/game", params = {"type": "gameData"}, json = {"gameData": gameData})