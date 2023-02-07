# sudo apt install python3-gi python3-gi-cairo gir1.2-gtk-3.0 gir1.2-webkit2-4.0 pywebview
# sudo python3 local/main/brainstorm/gui/web.py
import webview
import os
import subprocess
import requests

URL = "http://flyyrin.pythonanywhere.com/game"

class Api:
    def __init__(self):
        pass

    def exit(self,nodig):
        print("exit")
        # subprocess.Popen("killall sh", shell=True, stdout=subprocess.PIPE)
    
    def start(self,playerData):
        print("start")
        np1,np2,cp1,cp2 = playerData.split("&")
        print(np1,np2,cp1,cp2)
        requests.post(url = URL, params = {"type": "start"})
    
    def stop(self,nodig):
        print("stop")
        requests.post(url = URL, params = {"type": "stop"})
    
if __name__ == '__main__':
    requests.post(url = URL, params = {"type": "stop"})
    api = Api()
    window = webview.create_window('Start', os.path.join(os.getcwd(), "C:/Users/bounc/Documents/GitHub/GIP-2022-2023/local/main/web/start.html"), js_api=api, fullscreen=True) # /home/rpi/Documents/GIP-2022-2023/local/main/brainstorm/gui/start.html
    webview.start()