"""
API waarmee de webInterface kan comuniceren met python code.
"""

# importeer nodioge modules en defineer alle basis variabelen
import webview
import os
import subprocess
import requests
import time

URL = "http://flyyrin.pythonanywhere.com/game"

# maak in de functie startWebInterface de class Api aan, deze kan gebruikt worden in de javascript van de webInterface
# dit wordt in een functie gedaan zodat we deze in een afzonderlijke thread kunnen uitvoeren
# de class Api heeft de volgende functies:
## exit: stuurt commando naar de server om spel stop te zetten, zet "exit" in de queue en sluit na 1 seconde het progamma af
## start: stuurt commando naar de server om spel te starten en zet "start|--doorgegeven player data--" in de queue
## color: zet "color|--doorgegeven kleur data--" in de queue
## stop: stuurt commando naar de server om spel stop te zetten en zet "stop" in de queue
# door een bug is minstens 1 parameter nodig, bij functies zonder parameters wordt een lege string doorgegeven om een error te voorkomen
def startWebInterface(queue):
    class Api:
        def __init__(self):
            pass

        def exit(self,nodig):
            requests.post(url = URL, params = {"type": "stop"})
            queue.put("exit")
            time.sleep(1)
            subprocess.Popen("killall sh", shell=True, stdout=subprocess.PIPE)
        
        def start(self,playerData):
            queue.put("start|"+playerData)
            requests.post(url = URL, params = {"type": "start"})

        def color(self,colorData):
            queue.put("color|"+colorData)
        
        def stop(self,nodig):
            queue.put("stop")
            requests.post(url = URL, params = {"type": "stop"})
    
    # stuurt commando naar de server om spel stop te zetten, mocht die nog op actief staan
    # start de webInterface in full screen modus en geef de Api class mee
    requests.post(url = URL, params = {"type": "stop"})
    api = Api()
    window = webview.create_window('Start', os.path.join(os.getcwd(), "/home/rpi/Documenten/GIP-2022-2023/main/webInterface/start.html"), js_api=api, fullscreen=True)
    webview.start()