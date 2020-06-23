#!/usr/bin/env python
import os


if __name__ == '__main__':

    if 'Not open source' == '{{ cookiecutter.license }}':
        os.remove('LICENSE')

    if 'no' == '{{ cookiecutter.travis }}':
        os.remove('.travis.yml')

    if 'no' == '{{ cookiecutter.tox }}':
        os.remove('tox.ini')
