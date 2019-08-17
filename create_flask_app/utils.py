import subprocess
import animation
import venv
import sys
import os
#from shellingham import detect_shell


"""Long running functions"""


@animation.wait('spinner')
def create_venv(dir: str):
    virtualenv = venv.EnvBuilder(with_pip=True)
    virtualenv.create(f"./{dir}")


"""helper functions"""


def create_file(file_name: str):
    open(file_name, 'w').close()


def create_folder(folder_name: str):
    os.mkdir(folder_name)


def create_init(directory: str = './'):
    open(directory + '__init__.py', 'w').close()


def activate_venv(project_name: str):
    #shell = detect_shell()
    if sys.platform == "win32":
        subprocess.Popen(
            f"{project_name}\\venv\\Scripts\\activate.bat", shell=True)
    elif sys.platform == "linux":
        subprocess.Popen(
            f". {project_name}/venv/bin/activate", shell=True)
    # FIXME: figure out how to execute shell commands within current shell
