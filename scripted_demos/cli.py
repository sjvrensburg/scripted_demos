from click.utils import echo
from scripted_demos.parse_line import parse
from scripted_demos.utilities import trigger
from pynput.keyboard import Controller
import sys
import click
import time

def main(input: str, keyboard, delay: int=5):
    time.sleep(delay)
    with open(input, 'r') as fname:
        for line in fname:
            parse(line, keyboard, kwargs={
        'wpm': 34, 'enter': False, 'init': 1,
        'prefix': '#'})

@click.command()
@click.argument('input')
@click.option(
    '-c', '--cmd', default='R',
    help='Command to listen for.')
@click.option(
    '-d', '--delay', default=5,
    help='Delay before reading input file.')
def demo(input: str, cmd: str='R', delay: int=5):
    keyboard = Controller()
    try:
        echo(f'Type  \"{cmd}\" and press \"Enter\" into the window\nwhere you want to run the demo.')
        if trigger(cmd):
            main(input, keyboard, delay)
    except KeyboardInterrupt:
        sys.exit('Process interrupted.')
    sys.exit()