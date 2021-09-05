import time
import random
import click
from pynput.keyboard import Key, Listener
from click import echo


class Trigger:
    def __init__(self, key_list, verbose=False) -> None:
        self.index = 0
        self.keys = key_list
        self.list = []
        self.verbose = verbose
    
    def return_key(self, key):
        try:
            # Alphanumeric key
            res = key.char
        except AttributeError:
            # Special key
            res = key
        return res
    
    def check(self, key):
        self.list.append(key)
        if self.return_key(key) == self.keys[self.index]:
                self.index = self.index + 1
        else:
            self.index = 0
        ans = self.index != len(self.keys)
        if len(self.list) > 10:
            return False
        if self.verbose:
            echo(f'Keys pressed since started monitoring, {len(self.list)}.')
            echo(f'Pressed "{self.return_key(key)}", index is {self.index}')
        return ans


# Typing: We need a function that simulates typing a string.
def type_str(line: str, keyboard, wpm: int=35, enter: bool=True, init: int=1) -> None:
    time.sleep(init)
    for letter in line:
        keyboard.type(letter)
        time.sleep(random.random()*10.0/wpm)
    if enter:
        keyboard.press(Key.enter)
        keyboard.release(Key.enter)


# Display: Print the entire line to the screen without delay.
def display(line: str, keyboard, prefix: str='#', enter: bool=True, init: int=1) -> None:
    time.sleep(init)
    keyboard.type(f'{prefix} {line}')
    if enter:
        keyboard.press(Key.enter)
        keyboard.release(Key.enter)


# Pause: Pause for specified seconds
def pause(t: float=1):
    time.sleep(t)


# Pause until...
def wait(continue_key=Key.enter):
    click.echo(
        click.style(f'Paused. Press "{continue_key}" to continue.', blink=True, bold=True))
    with Listener(on_press=lambda key: key != continue_key) as listener:
        listener.join()
    click.echo(
        click.style('Unpaused.', bold=True))
    click.clear()


# Clear: Clear the screen
def clear(keyboard):
    keyboard.press(Key.ctrl_l)
    keyboard.press('l')
    keyboard.release('l')
    keyboard.release(Key.ctrl_l)


# Function to listen for a string of letters.
def trigger(word:str, continue_key=Key.enter) -> bool:
    # Key sequence to listen for...
    keys = []
    for letter in word:
        keys.append(letter)
    keys.append(continue_key)
    trigger_obj = Trigger(keys)
    with Listener(on_press=trigger_obj.check) as listener:
        listener.join()
    return True