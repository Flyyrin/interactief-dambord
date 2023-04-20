import requests

requests.post(url = "https://flyyrin.pythonanywhere.com/game", params = {"type": "winner"}, json = {"winner": 2})