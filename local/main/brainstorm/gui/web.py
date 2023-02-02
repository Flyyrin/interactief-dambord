import webview
import os

class Api:
    def __init__(self):
        pass

    # def destroy(self):
    #     print("close")

    def __init__(self):
        self._window = None

    def set_window(self, window):
        self._window = window

    def destroy(self):
        self._window.destroy()

if __name__ == '__main__':
    api = Api()
    window = webview.create_window('Start', os.path.join(os.getcwd(), "local/main/brainstorm/gui/start.html"), js_api=api)
    api.set_window(window)
    webview.start()