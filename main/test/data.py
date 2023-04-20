import requests
import time

playerData = {
    "player1": {
        "name": "Romeo",
        "color": "green"
    },
    "player2": {
        "name": "Rafael",
        "color": "red"
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
        "0":"e",
        "1":1,
        "2":"e",
        "3":"p",
        "4":"e",
        "5":1,
        "6":"e",
        "7":1,
        "8":"e",
        "9":1,
        "10":"e",
        "11":1,
        "12":"e",
        "13":1,
        "14":"e",
        "15":1,
        "16":"e",
        "17":1,
        "18":"e",
        "19":1,
        "20":"e",
        "21":1,
        "22":"e",
        "23":1,
        "25":"e",
        "26":"e",
        "27":"e",
        "28":"e",
        "29":"e",
        "30":"e",
        "31":"e",
        "32":"e",
        "33":"e",
        "34":"e",
        "35":"e",
        "36":"e",
        "37":"e",
        "38":"e",
        "39":"e",
        "41":2,
        "42":"e",
        "43":2,
        "44":"e",
        "45":2,
        "46":"e",
        "47":2,
        "48":"e",
        "49":2,
        "50":"e",
        "51":2,
        "52":"e",
        "53":2,
        "54":"e",
        "55":2,
        "56":"e",
        "57":2,
        "58":"e",
        "59":2,
        "60":"e",
        "61":2,
        "62":"e",
        "63":2
    }
}

gameData["playing"] = 1
gameData["np1"] = playerData["player1"]["name"]
gameData["np2"] = playerData["player2"]["name"]
gameData["cp1"] = playerData["player1"]["color"]
gameData["cp2"] = playerData["player2"]["color"]
requests.post(url = "https://flyyrin.pythonanywhere.com/game", params = {"type": "gameData"}, json = {"gameData": gameData})