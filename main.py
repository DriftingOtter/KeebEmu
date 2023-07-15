from pynput import keyboard
from playsound import playsound
import os
import sys


# Global Key Pressed State Variable 
key_pressed = False

script_args = sys.argv
sound_directory = str(script_args[1])

file_names = os.listdir(sound_directory)


def on_press(key):
    global key_pressed

    try:
        if not key_pressed:
            key_pressed = True
            print(f'Pressed: {key.char}')
            play_key_sound(key)

    # For Special Chars
    except AttributeError:

        if not key_pressed:
            key_pressed = True
            print(f'Pressed: {key}')
            play_key_sound()


def on_release(key):
    global key_pressed

    key_pressed = False

    if key == keyboard.Key.esc:
        # Stop listener
        return False


def play_key_sound(key):

    global sound_directory

    try:
        keyname = str(key.char).upper().replace("'", "")
        print(keyname)

        print(f'{sound_directory}/{keyname}.mp3')
        playsound(f'{sound_directory}/{keyname}.mp3')

    except AttributeError:

        keyname = str(key).upper().replace("'", "")
        print(keyname)

        print(f'{sound_directory}/{keyname}.mp3')
        playsound(f'{sound_directory}/{keyname}.mp3')


# Create Keyboard Listern
listener = keyboard.Listener(on_press=on_press, on_release=on_release)

if __name__ == "__main__":
    listener.start()
    listener.join()

