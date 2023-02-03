# sudo apt install python3-gi python3-gi-cairo gir1.2-gtk-3.0 gir1.2-webkit2-4.0 pywebview
# sudo python3 local/main/brainstorm/gui/web.py
import webview
import os
import subprocess
import requests

URL = "http://flyyrin.pythonanywhere.com/"

class Api:
    def __init__(self):
        pass

    def exit(self,nodig):
        print("Board uit")
        subprocess.Popen("killall sh", shell=True, stdout=subprocess.PIPE)
        quit()
    
    def start(self,cp):
        np1,np2,cp1,cp2 = cp.split("&")
        print(np1,np2,cp1,cp2)
        requests.post(url = f"{URL}gameongoing", json = {'gameongoing': True, 'winner': 0})
    
    def stop(self,nodig):
        print("Reset board")
        requests.post(url = f"{URL}gameongoing", json = {'gameongoing': False, 'winner': 0})
    
if __name__ == '__main__':
    api = Api()
    window = webview.create_window('Start', os.path.join(os.getcwd(), "/home/rpi/Documents/GIP-2022-2023/local/main/brainstorm/gui/start.html"), js_api=api, fullscreen=True)

# win: requests.post(url = f"{URL}gameongoing", json = {'gameongoing': False, 'winner': winner})