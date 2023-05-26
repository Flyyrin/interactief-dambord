import time
import RPi.GPIO as GPIO
from rpi_rf import RFDevice

rf_pin = 17 # GPIO pin connected to the RF receiver data pin
rf_device = RFDevice(rf_pin)
rf_device.enable_rx()



GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.OUT) # GPIO pin connected to an LED



try:
    while True:
        if rf_device.rx_code_timestamp != None:
        # Get the received data
        data = rf_device.rx_code
        # Interpret the data as true/false
        is_high = (chr(data) == 'H')
        # Perform actions based on the signal
        if is_high:
        print("Received HIGH signal")
        GPIO.output(18, GPIO.HIGH) # Turn on the LED
        else:
        print("Received LOW signal")
        GPIO.output(18, GPIO.LOW) # Turn off the LED
        rf_device.reset()
        time.sleep(0.1)
except KeyboardInterrupt:
 GPIO.cleanup()
 rf_device.cleanup()