import webview
import os

class Api:
    def __init__(self):
        pass

    def start(self, name1, name2, color1, color2):
        print(name1, name2, color1, color2)

if __name__ == '__main__':
    api = Api()
    window = webview.create_window('Start', os.path.join(os.getcwd(), "local/main/brainstorm/gui/start.html"), js_api=api)
    webview.start()