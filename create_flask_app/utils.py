import os
import animation
import venv


"""Long running functions"""

@animation.wait('spinner')
def create_venv(dir: str):
    virtualenv = venv.EnvBuilder(with_pip=True)
    virtualenv.create(f"./{dir}")
    activate_venv()



"""helper functions"""

def create_file(file_name: str):
    file = open(file_name, 'w').close()


def create_folder(folder_name: str):
    os.mkdir(folder_name)


def create_init(directory: str='./'):
    file = open(directory + '__init__.py', 'w').close()


def activate_venv():
    #activate_this = '/path/to/env/bin/activate_this.py'
    #exec(open(this_file).read(), {'__file__': this_file})
    # https://paste.pythondiscord.com/esokixuret.py
    pass
