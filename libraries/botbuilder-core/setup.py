# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.

import os
from setuptools import setup

REQUIRES = [
    'botbuilder-schema>=4.0.0.a5',
    'botframework-connector>=4.0.0.a5']

root = os.path.abspath(os.path.dirname(__file__))

with open(os.path.join(root, 'botbuilder', 'core', 'about.py')) as f:
    package_info = {}
    info = f.read()
    exec(info, package_info)

setup(
    name=package_info['__title__'],
    version=package_info['__version__'],
    url=package_info['__uri__'],
    author=package_info['__author__'],
    description=package_info['__description__'],
    keywords=['BotBuilderCore', 'bots', 'ai', 'botframework', 'botbuilder'],
    long_description=package_info['__summary__'],
    license=package_info['__license__'],
    packages=['botbuilder.core'],
    install_requires=REQUIRES,
    classifiers=[
        'Programming Language :: Python :: 3.6',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Development Status :: 3 - Alpha',
        'Topic :: Scientific/Engineering :: Artificial Intelligence',
    ]
)
