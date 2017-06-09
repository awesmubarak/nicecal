from setuptools import setup
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.rst'), encoding='utf-8') as file:
    long_description = file.read()

setup(
     name='nicecal',
     version='1.0.0',
     description='Create a simple, aesthetically pleasing ascii calendar.',
     long_description=long_description,
     url='https://github.com/abactel/nicecal',
     author='abactel',
     author_email='abactel@protonmail.com',
     license='MIT',
     classifiers=[
         'Development Status :: 5 - Production/Stable',
         'Intended Audience :: End Users/Desktop',
         'Operating System :: OS Independent',
         'Topic :: Utilities',
         'License :: OSI Approved :: MIT License',
         'Programming Language :: Python'
     ],
     keywords='calendar cal ascii',
     packages=['nicecal']
)
