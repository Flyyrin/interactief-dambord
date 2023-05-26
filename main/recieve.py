import RPi.GPIO as GPIO
import time
from rpi_rf import RFDevice

GPIO.setmode(GPIO.BCM)

rf_receiver = RFDevice(26)
rf_receiver.enable_rx()

timestamp = None

while True:
    if rf_receiver.rx_code_timestamp != timestamp:
        timestamp = rf_receiver.rx_code_timestamp
        received_data = rf_receiver.rx_code
        print(received_data)

        if received_data == "KEY1":
            # Handle KEY1 action here
            print("Received KEY1")

        elif received_data == "KEY2":
            # Handle KEY2 action here
            print("Received KEY2")

        # Add more key conditions as needed

    time.sleep(0.01)

rf_receiver.cleanup()