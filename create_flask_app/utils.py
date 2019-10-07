from configparser import ConfigParser
from os import mkdir
import animation
from venv import EnvBuilder


"""Long running functions"""


@animation.wait('spinner')
def create_venv(dir: str):
    virtualenv = EnvBuilder(with_pip=True)
    virtualenv.create(f"./{dir}")


"""helper functions"""


def create_file(file_name: str):
    open(file_name, 'w').close()


def create_folder(folder_name: str):
    mkdir(folder_name)


def create_init(directory: str = './'):
    open(directory + '__init__.py', 'w').close()
