import click
import os
import sys
from .utils import create_file, create_init, create_folder, create_venv, activate_venv
from colorama import init, Fore, Back, Style

import time

NEWLINE = '\n'
init()


@click.command()
@click.argument('project_name')
@click.option('--api', is_flag=True, default=False, help='Will create Flask app that resembles API.')
@click.option('--spa', is_flag=True, default=False, help='Will create Flask app that resembles Single Page applications (only 1 endpoint).')
@click.option('--nodb', is_flag=True, default=False, help='Will create Flask app without connecting to any database.')
def create_project(project_name, api, spa, nodb):
    if nodb:
        click.echo('no db')

    else:
        click.echo('yes db')

    try:
        create_folder(project_name)
        # create_init()
    except FileExistsError:
        click.echo(NEWLINE)
        click.echo(
            Fore.RED + 'That directory already exists. Please check your project name and try again.')
        click.echo(Style.RESET_ALL)
        sys.exit(1)

    #ante = click.prompt('unesite ime: ')
    # click.echo(ante)

    click.echo(NEWLINE + 'Creating a new Flask app in ' +
               Fore.GREEN + f'~/{project_name}.')
    click.echo(Style.RESET_ALL)

    create_venv(f'./{project_name}/venv/')

    if sys.platform == 'win32':
        activate_venv(f'./{project_name}/venv/Scripts')
    elif sys.platform == 'linux':
        activate_venv(project_name)
