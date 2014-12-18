#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys


try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

import travelfiles
version = travelfiles.__version__

setup(
    name='travelfiles',
    version=version,
    author='',
    author_email='kuldeepkrishi@gmail.com',
    packages=[
        'travelfiles',
    ],
    include_package_data=True,
    install_requires=[
        'Django>=1.7.1',
    ],
    zip_safe=False,
    scripts=['travelfiles/manage.py'],
)
