import keyboard 

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

    if player == 1:
        if keyboard.is_pressed('z'):
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

        if keyboard.is_pressed('q'):
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

        if keyboard.is_pressed('a'):
            if not joystick_button1_pressed:
                joystick_button1_pressed = True
                any_pressed = True
                return "press"
        else:
            joystick_button1_pressed = False
    
    if player == 2:
        if keyboard.is_pressed('up'):
            if not joystick_boven1_pressed:
                joystick_boven1_pressed = True
                any_pressed = True
                return "up"
        else:
            joystick_boven1_pressed = False

        if keyboard.is_pressed('down'):
            if not joystick_onder1_pressed:
                joystick_onder1_pressed = True
                any_pressed = True
                return "down"
        else:
            joystick_onder1_pressed = False

        if keyboard.is_pressed('left'):
            if not joystick_links1_pressed:
                joystick_links1_pressed = True
                any_pressed = True
                return "left"
        else:
            joystick_links1_pressed = False
            
        if keyboard.is_pressed('right'):
            if not joystick_rechts1_pressed:
                joystick_rechts1_pressed = True
                any_pressed = True
                return "right"
        else:
            joystick_rechts1_pressed = False

        if keyboard.is_pressed('enter'):
            if not joystick_button1_pressed:
                joystick_button1_pressed = True
                any_pressed = True
                return "press"
        else:
            joystick_button1_pressed = False
