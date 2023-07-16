from pynput import keyboard
from playsound import playsound
import os
import sys
import charRef

# Global Key Pressed State Variable 
key_pressed = False

# Used to pull sound pack location (test*)
script_args = sys.argv
sound_directory = str(script_args[1])

# Get all file names in sound pack directory
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

    global sound_directory, file_names

    try:
        # Remove Quotes From Pynput & Make Text Upper Case To Match File Naming
        keyname = str(key.char).upper().replace("'", "")

        if keyname.isalnum():

            print(f'{sound_directory}/NORMAL.mp3')
            playsound(f'{sound_directory}/NORMAL.mp3')   

        elif "KEY" in str(keyname):

            for files in file_names:
                if keyname == file_names:
                    print(f'{sound_directory}/{keyname}.mp3')
                    playsound(f'{sound_directory}/{keyname}.mp3')

        else:

            print(f'{sound_directory}/{charRef.specialChar_mapping.get(keyname, keyname)}.mp3')
            playsound(f'{sound_directory}/{charRef.specialChar_mapping.get(keyname, keyname)}.mp3')

    except Exception:
        pass


if __name__ == "__main__":
    listener = keyboard.Listener(on_press=on_press, on_release=on_release)

    listener.start()
    listener.join()

