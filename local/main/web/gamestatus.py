import requests

URL = "http://flyyrin.pythonanywhere.com/game"

keuze = input("stop, start, win: ")

gameData = {
    "current-player": 1,
    "pieces": {
        "player1": {
            "pieces": 0,
            "kings": 0,
            "captured": 5
        },
        "player2": {
            "pieces": 0,
            "kings": 0,
            "captured": 0
        }
    }
}

if keuze == "win":
    r = requests.post(url = URL, params = {"type": "winner"}, json = {"winner": 1})
if keuze == "stop":
    r = requests.post(url = URL, params = {"type": "stop"})
if keuze == "start":
    r = requests.post(url = URL, params = {"type": "start"})
if keuze == "data":
    r = requests.post(url = URL, params = {"type": "gameData"}, json = {"gameData": gameData})
print(r.status_code)