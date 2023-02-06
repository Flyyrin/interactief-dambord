import requests

URL = "http://flyyrin.pythonanywhere.com/"
jsondata = {
    "gameongoing": True, 
    "winner": 0, 
    "player": 1,
    "game": {
        "p1": {
            "pieces": 16,
            "kings": 2,
            "captured": 5
        },
        "p2": {
            "pieces": 13,
            "kings": 0,
            "captured": 0
        }
    }
}
r = requests.post(url = f"{URL}gameongoing", json = jsondata)
print(r.status_code)