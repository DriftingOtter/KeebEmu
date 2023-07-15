from pynput import keyboard

key_pressed = False

def on_press(key):
    global key_pressed
    try:
        if not key_pressed:
            key_pressed = True
            print('alphanumeric key {0} pressed'.format(key.char))

    except AttributeError:
        if not key_pressed:
            key_pressed = True
            print('special key {0} pressed'.format(key))

def on_release(key):
    global key_pressed
    print('{0} released'.format(key))
    key_pressed = False

    if key == keyboard.Key.esc:
        # Stop listener
        return False

listener = keyboard.Listener(on_press=on_press, on_release=on_release)

listener.start()

while True:
    pass

