# sudo apt install python3-gi python3-gi-cairo gir1.2-gtk-3.0 gir1.2-webkit2-4.0 pywebview
# sudo python3 local/main/brainstorm/gui/web.py
import webview
import os
import subprocess
import requests

URL = "http://flyyrin.pythonanywhere.com/game"

def startWeb(queue):
    class Api:
        def __init__(self):
            pass

        def exit(self,nodig):
            print("exit")
            requests.post(url = URL, params = {"type": "stop"})
            queue.put("stop")
            subprocess.Popen("killall sh", shell=True, stdout=subprocess.PIPE)
        
        def start(self,playerData):
            print("start")
            queue.put("start|"+playerData)
            print(playerData)
            np1,np2,cp1,cp2,assist = playerData.split("&")
            print(np1,np2,cp1,cp2,assist)
            requests.post(url = URL, params = {"type": "start"})

        def color(self,colorData):
            print("color")
            queue.put("color|"+colorData)
        
        def stop(self,nodig):
            print("stop")
            requests.post(url = URL, params = {"type": "stop"})
            queue.put("stop")
        
    requests.post(url = URL, params = {"type": "stop"})
    api = Api()
    window = webview.create_window('Start', os.path.join(os.getcwd(), "/home/rpi/Documents/GIP-2022-2023/local/main/web/start.html"), js_api=api, fullscreen=True) # /home/rpi/Documents/GIP-2022-2023/local/main/brainstorm/gui/start.html
    webview.start()