def readController(ser, player):
    if ser.in_waiting > 0:
        data = ser.readline().decode('utf-8').rstrip()

        command_player = int(data.split("_")[0])
        command = data.split("_")[1]

        if player == command_player:
            return command