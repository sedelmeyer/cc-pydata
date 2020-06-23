#!/usr/bin/env python
import os


if __name__ == '__main__':

    if 'Not open source' == '{{ cookiecutter.license }}':
        os.remove('LICENSE')
