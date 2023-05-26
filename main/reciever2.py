# sudo apt install pigpio

import time
import pigpio

RX_PIN = 17

def receive_data():
    pi = pigpio.pi()
    if not pi.connected:
        return None
    
    pi.set_mode(RX_PIN, pigpio.INPUT)
    pi.bb_serial_read_open(RX_PIN, 2000)  # Baud rate: 2000
    
    data = ""
    start_time = time.time()
    
    while (time.time() - start_time) < 10:  # Timeout after 10 seconds
        count, data = pi.bb_serial_read(RX_PIN)
        if count:
            break
    
    pi.bb_serial_read_close(RX_PIN)
    pi.stop()
    
    return data.decode('utf-8')

# Main program
while True:
    received_data = receive_data()
    if received_data:
        print("Received data:", received_data)
    time.sleep(1)