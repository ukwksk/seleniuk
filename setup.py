# -*- coding:utf-8 -*-
from __future__ import absolute_import
from __future__ import unicode_literals
import os

from setuptools import setup, find_packages

package = 'seleniuk'

here = os.path.dirname(os.path.abspath(__file__))
version = next((line.split('=')[1].strip().replace("'", '') for line in
                open(os.path.join(here, package, '__init__.py'))
                if line.startswith('__version__ = ')), '0.0.dev0')
email = next((line.split('=')[1].strip() for line in
                open(os.path.join(here, '.env'))
                if line.startswith('email=')), '')
readme = os.path.join(here, 'README.md')


def _requires_from_file(filename):
    return open(filename).read().splitlines()


setup(
    name=package,
    version=version,
    url='https://github.com/ukwksk/' + package,
    author='ukwksk',
    author_email=email,
    maintainer='ukwksk',
    maintainer_email=email,
    description='Selenium Wrapper',
    long_description=readme,
    packages=find_packages(),
    install_requires=_requires_from_file('requirements.txt'),
    license="MIT",
    classifiers=[
        'Programming Language :: Python :: 3.6',
        'License :: OSI Approved :: MIT License',
    ],
)
