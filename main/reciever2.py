import time
import rpi_rf

# GPIO pin connected to the receiver
RX_PIN = 27

# Create an instance of the RF device
rf_device = rpi_rf.RFDevice(RX_PIN)

# Enable the RF device
rf_device.enable_rx()

while True:
    if rf_device.rx_code_timestamp != None:
        received_data = rf_device.rx_code
        print("Received data:", received_data)
        rf_device.reset()

    time.sleep(0.01)

rf_device.cleanup()