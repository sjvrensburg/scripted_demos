from typing import Any, Dict
from scripted_demos.utilities import type_str, display
from scripted_demos.utilities import pause, wait, clear
from copy import copy
from pynput.keyboard import Key
from click import echo
import re

# If the line:
#   1. is empty, then pause.
#   2. starts with #!! then wait until 'enter' key
#   3. starts with #<< then display all
#   4. starts with #cls then clear screen
#   5. starts with #{t} then pause for t seconds.

wait_ptrn = re.compile(r'^#!{2}')
display_ptrn = re.compile(r'^#<{2}\s(.*)')
clear_ptrn = re.compile(r'^#cls')
pause_ptrn = re.compile(r'^#\{(.*)\}')

def parse(
    line: str,
    keyboard,
    kwargs: Dict[str, Any]={
        'wpm': 40, 'enter': False, 'init': 1,
        'prefix': '#'},
    t = 1, key = Key.ctrl) -> None:
    line_kwargs = copy(kwargs)
    line_kwargs.pop('prefix', None)
    display_kwargs = copy(kwargs)
    display_kwargs.pop('wpm', None)

    if wait_ptrn.search(line):
        return wait(key)
    
    if display_ptrn.search(line):
        line = display_ptrn.match(line).group(1)
        line = f'{line}\n'
        return display(line, keyboard, **display_kwargs)
    
    if clear_ptrn.search(line):
        return clear(keyboard)

    if pause_ptrn.search(line):
        t = pause_ptrn.match(line).group(1)
        return pause(float(t))
    
    if len(line.strip()) == 0:
        return pause(t)

    return type_str(line, keyboard, **line_kwargs)