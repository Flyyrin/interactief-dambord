import webview
import os
import subprocess

# sudo apt install python3-gi python3-gi-cairo gir1.2-gtk-3.0 gir1.2-webkit2-4.0 pywebview


class Api:
    def __init__(self):
        pass


    def __init__(self):
        pass

    def exit(self,nodig):
        subprocess.Popen("killall python", shell=True, stdout=subprocess.PIPE)
    
    def start(self,nodig):
        print("test")

if __name__ == '__main__':
    api = Api()
    window = webview.create_window('Start', os.path.join(os.getcwd(), "local/main/brainstorm/gui/start.html"), js_api=api)