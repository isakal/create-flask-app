import click
import os
import sys
from .utils import create_file, create_init, create_folder

import time

#TODO: create these 2 functions


@click.command()
@click.argument('project_name')
@click.option('--nodb', is_flag=True, default=False, help='Will make a database and link it with flask app.')
def create_project(nodb, project_name):
    if nodb:
        click.echo('no db')

    else:
        click.echo('yes db')
    #create_file(project_name)
    click.echo(f'{project_name} is created')
    #create_init()
