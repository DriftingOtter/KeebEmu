from pynput import keyboard
import sys
import os
from playsound import playsound


# Global Key Pressed State Variable 
key_pressed = False

sound_directory = '/Documents/CreamSwitchesRyan'
file_names = os.listdir(sound_directory)


def on_press(key):
    global key_pressed

    try:
        if not key_pressed:
            key_pressed = True
            print(f'Pressed: {key.char}')

    # For Special Chars
    except AttributeError:
        if not key_pressed:
            key_pressed = True
            print(f'Pressed: {key}')


def on_release(key):
    global key_pressed

    key_pressed = False

    if key == keyboard.Key.esc:
        # Stop listener
        return False


def check_for_correct_sound(key):

    global sound_directory, files_names

    for file_name in file_names:

        if key.char.toupper() or key.toupper() == file_name[:-4]:
            playsound(f'{sound_directory}/{key.toupper()}.mp3')

listener = keyboard.Listener(on_press=on_press, on_release=on_release)

if __name__ == "__main__":
    listener.start()
    listener.join()

