import click
import getpass
import os
import sys

from segmind_track.lite_extensions.client_utils import LoginError, fetch_token
from segmind_track.utils import cyan_print, green_print, red_print

# import jsonpickle
# from click import UsageError


@click.group()
def cli():
    pass


@cli.command()
def config():
    cyan_print('Please enter your credentials for https://track.segmind.com')

    email = input('Enter Email-id :: ')
    password = getpass.getpass('Enter Password :: ')

    try:
        fetch_token(email, password)
    except LoginError:
        red_print('Log-In failed !!! Invalid credentials')
        sys.exit()

    folder_path = os.path.join(os.path.expanduser('~'), '.segmind')
    os.makedirs(folder_path, exist_ok=True)

    file_path = os.path.join(folder_path, 'secret.file')

    with open(file_path, 'w') as file:
        file.write('[secret]\n')
        file.write('email={}\n'.format(email))
        file.write('password={}\n'.format(password))

    green_print('Log-In Successful !!!')
