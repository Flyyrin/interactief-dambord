# chromedriver --version
# sudo wget https://github.com/electron/electron/releases/download/v9.0.2/chromedriver-v9.0.2-linux-armv7l.zip
# sudo apt-get install unzip
# unzip chromedriver-v9.0.2-linux-armv7l.zip
# in  /usr/lib/chromium-browser/.
# pip3 install pyvirtualdisplay
# chmod -R 777 /path/to/file  of   --no-sandbox

from pyvirtualdisplay import Display

display = Display(visible=0, size=(800, 600))
display.start()
driver = webdriver.Chrome(‘/usr/lib/chromium-browser/chromedriver’)