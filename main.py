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

    except AttributeError:

        if not key_pressed:
            key_pressed = True

            print(f'Pressed: {key}')
            play_key_sound()


def on_release(key):
    global key_pressed

    key_pressed = False

    if key == keyboard.Key.esc:
        return False


def play_key_sound(key):

    global sound_directory

    try:

        # Remove Quotes From Pynput & Make Text Upper Case To Match File Naming
        keyname = str(key.char).upper().replace("'", "")
        print(keyname)

        print(f'{sound_directory}/{keyname}.mp3')
        
        try:
            playsound(f'{sound_directory}/{keyname}.mp3')
        except:
            pass


    except AttributeError:
        
        # Remove Quotes From Pynput & Make Text Upper Case To Match File Naming
        keyname = str(key).upper().replace("'", "")
        print(keyname)

        print(f'{sound_directory}/{keyname}.mp3')

        try:
            playsound(f'{sound_directory}/{keyname}.mp3')
        except:
            pass


if __name__ == "__main__":
    listener = keyboard.Listener(on_press=on_press, on_release=on_release)

    listener.start()
    listener.join()

