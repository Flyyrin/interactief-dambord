import requests

URL = "http://flyyrin.pythonanywhere.com/"
r = requests.post(url = f"{URL}gameongoing", json = {'gameongoing': False, 'winner': 1})
print(r.status_code)