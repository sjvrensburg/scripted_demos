from scripted_demos.parse_line import parse
from scripted_demos.utilities import trigger
from pynput.keyboard import Controller
from more_itertools import pairwise
import sys
import click
import time

def main(input: str, keyboard, wpm: int=34, delay: int=5):
    with open(input, 'r') as fname:
        lines = ['']
        for line in fname:
            lines.append(line)
        lines.append('')
        time.sleep(delay)
        i = 0
        for line, nextline in pairwise(lines):
            if i > 0 and i % 10 == 0:
                click.clear()
            click.echo(nextline, nl=False)
            if i > 0:
                parse(
                    line, 
                    keyboard, kwargs={
                        'wpm': wpm, 'enter': False, 'init': 1,
                        'prefix': '#'})
            i += 1

@click.command()
@click.argument('input')
@click.option(
    '-c', '--cmd', default='R',
    help='Command to listen for.')
@click.option(
    '-d', '--delay', default=5,
    help='Delay before reading input file.')
@click.option(
    '-s', '--speed', default=34,
    help='Typing speed (default 34)')
def demo(input: str, cmd: str='R', delay: int=5, speed: int=34):
    keyboard = Controller()
    try:
        click.echo(
            f'Type  \"{cmd}\" and press \"Enter\" into the window\nwhere you want to run the demo.')
        if trigger(cmd):
            click.clear()
            main(input, keyboard, speed, delay)
    except KeyboardInterrupt:
        sys.exit('Process interrupted.')
    click.echo(click.style('DONE!', bold=True))
    sys.exit()