#!/usr/bin/env python2.7
from pynput import keyboard # pip install pynput
import pyautogui # pip install pyautogui
import time
import threading

print("Shakira will begin shaking when 's' is pressed.")
print("To pause shaking, press 'p'.")
print("To quit, press 'q' or Escape.")

shake_active = False
is_shaking = False
ticker = threading.Event()

def shake():
    global shake_active
    global is_shaking

    if shake_active == True and not is_shaking:
        is_shaking = True
        pyautogui.moveRel(None, 10)
        time.sleep(.250)
        pyautogui.moveRel(-10, None)
        time.sleep(.250)
        pyautogui.moveRel(None, -10)
        time.sleep(.250)
        pyautogui.moveRel(10, None)
        is_shaking = False

def on_press(key):
    pass

def on_release(key):
    global shake_active
    global ticker

    try: k = key.char
    except: k = key.name

    if key == keyboard.Key.esc or k == 'q':
        shake_active = False
        ticker.set()
        return False
    elif k == 's':
        shake_active = True
        print('Shaking: Started')
    elif k == 'p':
        shake_active = False
        print('Shaking: Paused')

key_listener = keyboard.Listener(
    on_press=on_press,
    on_release=on_release
)
key_listener.start()

while not ticker.wait(45):
    shake()