import time
import RPi.GPIO as GPIO
import virtualwire

# Raspberry Pi pin connected to the receiver data pin
RX_PIN = 18

def setup():
    # Initialize the virtual wire library
    GPIO.setmode(GPIO.BCM)
    vw = virtualwire.VirtualWire(RX_PIN, 2000)  # Transmission rate in bits per second
    vw.begin()
    vw.enableTransmit(False)  # Set to False for receiving

def loop():
    while True:
        message = virtualwire.getMessage()  # Wait for a message to be received
        if message:
            print("Received key:", chr(message[0]))

if __name__ == '__main__':
    try:
        setup()
        loop()
    except KeyboardInterrupt:
        pass
    finally:
        GPIO.cleanup()

# git clone https://github.com/lucsmall/VirtualWire.git
# cd VirtualWire
# sudo python setup.py install