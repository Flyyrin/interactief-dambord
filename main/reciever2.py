import time
import RPi.GPIO as GPIO
import subprocess

PIN = 27  # GPIO pin connected to the data pin of RF receiver

GPIO.setmode(GPIO.BCM)
GPIO.setup(PIN, GPIO.IN)

def receive_code():
    code = 0
    
    while GPIO.input(PIN) == 1:
        pass
    
    # Wait for the start bit
    while GPIO.input(PIN) == 0:
        pass
    
    # Read the received bits
    for i in range(0, 16):
        while GPIO.input(PIN) == 1:
            pass
        code <<= 1
        if GPIO.input(PIN) == 0:
            code |= 1
        while GPIO.input(PIN) == 0:
            pass
    
    return code

try:
    while True:
        received_code = receive_code()
        print("Received code:", received_code)
        # Do something with the received code
        
except KeyboardInterrupt:
    GPIO.cleanup()