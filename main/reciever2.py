import time
from pyRH_ASK import RH_ASK

# Raspberry Pi pin connected to the receiver
RX_PIN = 27

# Create an instance of the RH_ASK driver
driver = RH_ASK.RH_ASK()

if not driver.init():
    print("RF module initialization failed.")
    exit(1)

while True:
    if driver.available():
        received_data = ""
        received_data_len = 0
        buf = []
        while driver.available():
            buf.append(chr(driver.recv()))
            received_data_len += 1
            if received_data_len >= 32:  # Limit the received data size
                break

        received_data = ''.join(buf)
        print("Received data:", received_data)
    time.sleep(1)
