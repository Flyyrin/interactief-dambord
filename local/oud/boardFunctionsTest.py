import keyboard
from itertools import islice

def chunks(data, SIZE=10000):
   it = iter(data)
   for i in range(0, len(data), SIZE):
      yield {k:data[k] for k in islice(it, SIZE)}

joystick_boven1_pressed = False
joystick_onder1_pressed = False
joystick_links1_pressed = False
joystick_rechts1_pressed = False
joystick_button1_pressed = False
joystick_boven2_pressed = False
joystick_onder2_pressed = False
joystick_links2_pressed = False
joystick_rechts2_pressed = False
joystick_button2_pressed = False

def readController(player):
    global joystick_boven1_pressed
    global joystick_onder1_pressed
    global joystick_links1_pressed
    global joystick_rechts1_pressed
    global joystick_button1_pressed
    global joystick_boven2_pressed
    global joystick_onder2_pressed
    global joystick_links2_pressed
    global joystick_rechts2_pressed
    global joystick_button2_pressed

    any_pressed = False
    while not any_pressed:
        if True:
            if keyboard.is_pressed('w'):
                if not joystick_boven1_pressed:
                    joystick_boven1_pressed = True
                    any_pressed = True
                    return "up"
            else:
                joystick_boven1_pressed = False

            if keyboard.is_pressed('s'):
                if not joystick_onder1_pressed:
                    joystick_onder1_pressed = True
                    any_pressed = True
                    return "down"
            else:
                joystick_onder1_pressed = False

            if keyboard.is_pressed('a'):
                if not joystick_links1_pressed:
                    joystick_links1_pressed = True
                    any_pressed = True
                    return "left"
            else:
                joystick_links1_pressed = False
                
            if keyboard.is_pressed('d'):
                if not joystick_rechts1_pressed:
                    joystick_rechts1_pressed = True
                    any_pressed = True
                    return "right"
            else:
                joystick_rechts1_pressed = False
            
            if keyboard.is_pressed('q'):
                if not joystick_button1_pressed:
                    joystick_button1_pressed = True
                    any_pressed = True
                    return "press"
            else:
                joystick_button1_pressed = False

def updateLedBoard(board):
    board_list = []
    for item in chunks(board, 8):
        row = []
        for piece in item.values():
            row.append(str(piece))
        row.reverse()
        board_list.append(row)
    
    board_list.reverse()

    for row in board_list:
        print(row)
