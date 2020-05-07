from pynput.keyboard import Key, Controller
import time

keyboard = Controller()

while True:
    keyboard.type("pls meme")
    keyboard.press(Key.enter)
    time.sleep(3.1)
