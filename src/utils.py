import os
import shutil
import animation
from venv import EnvBuilder
from subprocess import call
from sys import exit
from click import echo
from termcolor import colored


"""Long running functions"""


@animation.wait('spinner')
def create_venv(dir: str):

    virtualenv = EnvBuilder(with_pip=True)
    virtualenv.create(f"./{dir}")


"""helper functions"""


def error_exit(message: str):
    """Prints error message and exits the app with exit code 1."""
    echo()
    echo(colored(message, 'red'))
    echo()
    exit(1)


def create_file(file_name: str):
    open(file_name, 'w').close()


def create_folder(folder_name: str):
    os.mkdir(folder_name)


def shell(command: str):
    command = command.split()
    call(command)


def copy_filetree(source: str, destination: str, symlinks=True, ignore=None):
    if not os.path.exists(destination):
        os.makedirs(destination)
    for item in os.listdir(source):
        s = os.path.join(source, item)
        d = os.path.join(destination, item)
        if os.path.isdir(s):
            copy_filetree(s, d, symlinks, ignore)
        else:
            if not os.path.exists(d) or os.stat(s).st_mtime - os.stat(d).st_mtime > 1:
                shutil.copy2(s, d)


def print_command(command: str, description: str):
    echo('\t' + colored(command, 'cyan'))
    echo('\t'*2 + description)
    echo('\n')
