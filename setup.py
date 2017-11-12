#!/usr/bin/env python3

from codecs import open
from os import path
from setuptools import setup

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.rst'), encoding='utf-8') as file:
    long_description = file.read()

setup(
    name='nicecal',
    version='1.1.3',
    description='Create good looking plain text calendars using box-drawing characters.',
    long_description=long_description,
    url='https://github.com/awesmubarak/nicecal',
    author='Awes Mubarak',
    author_email='awes.mubarak@awesmubarak.com',
    license='MIT',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: End Users/Desktop',
        'Operating System :: OS Independent',
        'Topic :: Utilities',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python'
    ],
    keywords='nicecal calendar cal unicode',
    packages=['nicecal']
)
