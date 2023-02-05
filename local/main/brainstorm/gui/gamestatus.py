import requests

URL = "http://flyyrin.pythonanywhere.com/"
r = requests.post(url = f"{URL}gameongoing", json = {'gameongoing': True, 'winner': 0})
print(r.status_code)