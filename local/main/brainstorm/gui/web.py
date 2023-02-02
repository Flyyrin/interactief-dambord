import webview
import os

# sudo apt install python3-gi python3-gi-cairo gir1.2-gtk-3.0 gir1.2-webkit2-4.0 pywebview


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