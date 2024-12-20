import click
from textPlay.colors import *

import atexit

from autoruncmd.run import runScript
from autoruncmd.c_init import createConfig
from autoruncmd.add import addtoScript
from autoruncmd.find import findLine
from autoruncmd.v_n import __version__, __title__

def terminate():
    print(f"\nHappy Coding!")

atexit.register(terminate)

@click.group()
@click.version_option(version= __version__ , prog_name= __title__)
def cli():
    print(f"\n\t{MAGENTA}{__title__}{RESET} {MAGENTA}v{__version__}{RESET}\n")
    pass

@click.command(help="Create config file")
@click.argument("header", type=click.STRING, required=False, help="Header of the scripts to run")
def init(header=None):
    createConfig(header)

@click.command(help="Run script from config file")
@click.argument("header", type=click.STRING, required=True, help="Header of the scripts to run")
@click.option("--config", "-c", help="Specify config file", type=click.STRING, required=False)
@click.option("--pipe", "-p", help="Pipe the commands execting", type=click.BOOL, is_flag=True)
def cmd(header=None, config=None, pipe=False):
    runScript(header, config, pipe)

@click.command(help="Add script to config file")
@click.option("--config", "-c", help="Specify config file", type=click.STRING, default=".pyscripts")
@click.option("--header", "-h", help="Specify header name", prompt="Header name", type=click.STRING, required=True)
@click.option("--script", "-s", help="Specify script name", prompt="Script name", type=click.STRING, required=True)
def add(header, script, config=".pyscripts"):
    addtoScript(config, header, script)

@click.command(help="Find line in config file")
@click.option("--config", "-c", help="Specify config file", type=click.STRING, default=".pyscripts")
@click.option("--header", "-h", help="Specify header name", type=click.STRING, required=True)
@click.option("--line", "-l", help="Specify line number", type=click.STRING, required=False)
def find(config, line, header):
    findLine(config, line, header)

cli.add_command(init)
cli.add_command(cmd)
cli.add_command(add)
cli.add_command(find)
