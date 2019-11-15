import click
import os
import sys
from .utils import create_file, create_folder, create_venv, shell, error_exit, copy_filetree
from colorama import init, Fore, Back, Style


# initializing the screen for the colorama
init()
NEWLINE = '\n'


@click.command(context_settings={"ignore_unknown_options": True})
@click.argument('project_name')
@click.option('--default', is_flag=True, default=True, help='Create very simple Flask app with all code in one file.')
@click.option('-helloworld', 'hw', is_flag=True, default=False, help='Create Flask Hello World example.')
@click.option('--api', is_flag=True, default=False, help='Create Flask app that resembles API.')
@click.option('--spa', is_flag=True, default=False, help='Create Flask app that resembles Single Page applications (only 1 endpoint).')
def create_project(project_name, api, spa):
    """
    This function is responsible for interacting user with file creation.
    Args:
        project_name (string): This is the project name that will be used for project creation.
        api (bool): This flag says if project is going to have api-like boilerplate structure.
        spa (bool): This flag says if project is going to have spa-like boilerplate structure.

    Raises:
        FileExistsError: If project_name param has the same value as some of the directories in the current directory.

    """
    # getting arguments and options from the locals() function
    options = locals()
    # project_name is removed since we want to browse through options and project_name isn't necessary
    options.pop('project_name')

    # seeing if there are more than 2 options selected
    if [i for i in options.values()].count(True) > 1:
        error_exit("Please make sure only 1 option is selected and try again.")

    # seeing if project_name matches any of directories in the current directory
    try:
        create_folder(project_name)

    except FileExistsError:
        error_exit(
            'That directory already exists. Please check your project name and try again.')

    # printing when project creation is starting
    click.echo(NEWLINE + 'Creating a new Flask app in ' +
               Fore.GREEN + f'~/{project_name}.')
    click.echo(Style.RESET_ALL)

    create_venv(f'./{project_name}/venv/')

    # deciding which boilerplate to choose and creating it based on argument choice
    base_dir = os.path.dirname(__file__)
    #choice = ""
    # iterating over names and values in options dictionary
    for name, value in options.items():
        if value:
            choice = os.path.join(base_dir, name)

    copy_filetree(choice, f"./{project_name}/")
