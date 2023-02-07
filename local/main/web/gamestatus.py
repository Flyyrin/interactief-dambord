import requests

URL = "http://flyyrin.pythonanywhere.com/game"

keuze = input("stop, start, win: ")

if keuze == "win":
    r = requests.post(url = URL, params = {"type": "winner"}, json = {"winner": 1})
if keuze == "stop":
    r = requests.post(url = URL, params = {"type": "stop"})
if keuze == "start":
    r = requests.post(url = URL, params = {"type": "start"})
print(r.status_code)