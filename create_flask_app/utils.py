import os
import animation


@animation.wait('spinner')
def create_file(file_name: str):
    file = open(file_name, 'w').close()
    return


@animation.wait('spinner')
def create_folder(folder_name):
    os.mkdir(folder_name)
    return

@animation.wait('spinner')
def create_init(directory: str='./'):
    file = open(directory + '__init__.py', 'w').close()
    return
