import serial

ser = serial.Serial('/dev/ttyACM0', 9600, timeout=1)
ser.reset_input_buffer()

def readController(player):
    if ser.in_waiting > 0:
        data = ser.readline().decode('utf-8').rstrip()
        print(data)

        command_player = int(data.split("_")[0])
        command = data.split("_")[1]

        if player == command_player:
            return command

while True:
    readController(1)