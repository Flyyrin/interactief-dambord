from gpiozero import Button
from time import sleep

joystick_onder = Button(5, pull_up = 0) #rood
joystick_boven = Button(6, pull_up = 0) #zwart
joystick_links = Button(13, pull_up = 0) #blauw
joystick_rechts = Button(23, pull_up = 0) #groen
joystick_button = Button(24, pull_up = 0) #wit
#oranje en grijs op 5v!

def trackJoystick():
    joystick_boven_pressed = False
    joystick_onder_pressed = False
    joystick_links_pressed = False
    joystick_rechts_pressed = False
    joystick_button_pressed = False
    while True: 
        sleep(0.2)
        if joystick_boven.is_pressed:
            if not joystick_boven_pressed:
                joystick_boven_pressed = True
                print("Boven")
        else:
            joystick_boven_pressed = False

        if joystick_onder.is_pressed:
            if not joystick_onder_pressed:
                joystick_onder_pressed = True
                print("Onder")
        else:
            joystick_onder_pressed = False

        if joystick_links.is_pressed:
            if not joystick_links_pressed:
                joystick_links_pressed = True
                print("Links")
        else:
            joystick_links_pressed = False
            
        if joystick_rechts.is_pressed:
            if not joystick_rechts_pressed:
                joystick_rechts_pressed = True
                print("Rechts")
        else:
            joystick_rechts_pressed = False
        
        if joystick_button.is_pressed:
            if not joystick_button_pressed:
                joystick_button_pressed = True
                print("Knop")
        else:
            joystick_button_pressed = False