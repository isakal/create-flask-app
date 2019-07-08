import click
import os
import sys
from creator import create_files, create_database

#TODO: create these 2 functions


@click.command()
@click.argument('project_name')
@click.option('--nodb', is_flag=True, default=False, help='Will make a database and link it with flask app.')
def create_project(nodb, project_name):
    if nodb:
        click.echo('no db')

    else:
        click.echo('yes db')
    click.echo(f'{project_name} is the project name')



if __name__ == '__main__':
    create_project()
