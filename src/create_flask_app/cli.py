import click
import os
from utils import copy_filetree, create_file, create_folder, create_venv, error_exit, print_command, shell
from termcolor import colored
from platform import system


NEWLINE = '\n'


@click.command(context_settings={"ignore_unknown_options": True})
@click.argument('project_name')
@click.option('--default', is_flag=True, default=False, help='Create very simple Flask app with standard file structure.')
@click.option('--helloworld', is_flag=True, default=False, help='Create Flask Hello World example.')
@click.option('--api', is_flag=True, default=False, help='Create Flask app that resembles API.')
@click.option('--spa', is_flag=True, default=False, help='Create Flask app that resembles Single Page application.')
def create_project(project_name, default, helloworld, api, spa):
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

    # if none of the options was selected, fall back to default
    if [i for i in options.values()].count(True) == 0:
        options['default'] = True

    # seeing if there are more than 2 options selected
    elif [i for i in options.values()].count(True) > 1:
        error_exit("Please make sure only 1 option is selected and try again.")

    # seeing if project_name matches any of directories in the current directory
    try:
        create_folder(project_name)

    except FileExistsError:
        error_exit(
            'That directory already exists. Please check your project name and try again.')

    # printing when project creation is starting
    click.echo(NEWLINE + 'Creating a new Flask app in ' +
               colored(f'~/{project_name}', 'green') + '.')
    click.echo(NEWLINE)

    # create venv if helloworld option is not selected
    if not helloworld:
        create_venv(f'./{project_name}/venv/')

    # deciding which boilerplate to choose and creating it based on argument choice
    base_dir = os.path.dirname(__file__)

    # iterating over names and values in options dictionary
    for name, value in options.items():
        if value:
            choice = os.path.join(base_dir, name)
    # copy the boilerplate filetree to the project folder
    try:
        copy_filetree(choice, f"./{project_name}/")
    except Exception as e:
        error_exit(e)

    # output hell starts here
    click.echo(
        f'Success! Created app {project_name} in {os.getcwd()}'+f'/{project_name}')
    click.echo('Inside that directory you can run several commands:')
    click.echo(NEWLINE)

    # print commands and descriptions
    print_command('python run.py',
                  'Starts the server, default config is set to development.')
    if not helloworld:

        print_command('export secret_key=STRING',
                      'Sets the secret key for your app.')

        print_command('export PRODUCTION=True',
                      'Sets production config for your app. Setting it to False will set the development config.')

        print_command('source venv/bin/activate (unix) \n\t./venv/Scripts/activate  (windows)',
                      'Activate the virtual enviroment for the app.')

        print_command('pip install -r requirements.txt',
                      'Install the packages listed in requirements.txt into the venv.')

        click.echo('We suggest that you start by typing:')
        click.echo(colored('\tcd ', 'cyan') + colored(project_name, 'white'))
        click.echo(colored('\tsource venv/bin/activate' if not system()
                           == 'Windows' else '\t./venv/Scripts/activate', 'cyan'))
        click.echo(colored('\tpip install -r ', 'cyan') +
                   colored('requirements.txt', 'white'))
        click.echo(colored('\tpython run.py', 'cyan'))
    else:
        click.echo('We suggest that you start by typing:')
        click.echo(colored('\tcd ', 'cyan') + colored(project_name, 'white'))
        click.echo(colored('\tpip install flask ', 'cyan'))
        click.echo(colored('\tpython app.py'))

    click.echo(NEWLINE + 'Happy hacking!')
