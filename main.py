from pynput import keyboard

# Global Key Pressed State Variable 
key_pressed = False

def on_press(key):

    global key_pressed

    try:
        if not key_pressed:
            key_pressed = True
            print(f'Pressed: {key.char}')

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

listener = keyboard.Listener(on_press=on_press, on_release=on_release)

if __name__ == "__main__":
    listener.start()
    listener.join()

