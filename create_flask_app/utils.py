import os
import animation
import venv


#helper functions



def create_file(file_name: str):
    file = open(file_name, 'w').close()
    return


def create_folder(folder_name):
    os.mkdir(folder_name)
    return


def create_init(directory: str='./'):
    file = open(directory + '__init__.py', 'w').close()
    return
