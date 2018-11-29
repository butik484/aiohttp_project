import os

from fabric.api import local, task
from fabric.colors import green
from . import common
__all__ = [
    'install_dependencies',
    'compiledeps',
]


@task
def install_dependencies():
    """Install shell/cli dependencies

    Define your dependencies here, for example
    local('sudo npm -g install ngrok')
    """
    local('pip install --upgrade setuptools pip')


@task
def compiledeps(u=False):
    """Compile pip dependencies"""
    print(green(common.message(
        "Compile pip dependencies")))
    upgrade = '-U' if u else ''
    in_files = [
        'requirements/development.in',
    ]
    for in_file in in_files:
        local(
            'pip-compile {in_file} {upgrade}'.format(
                in_file=in_file,
                upgrade=upgrade)
        )

