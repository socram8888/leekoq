#!/usr/bin/env python3

# Copyright 2020 Marcos Del Sol Vives <marcos@orca.pet>
# SPDX-License-Identifier: WTFPL

import os.path
from setuptools import setup, find_packages

def read(file):
	this_directory = os.path.abspath(os.path.dirname(__file__))
	with open(os.path.join(this_directory, file), encoding='utf-8') as f:
		content = f.read()
	return content

setup(
	name='leekoq',
	packages=['leekoq'],
	version='1.0',
	license='WTFPL',

	description='Python implementation of Keeloq encryption algorithm',
	long_description=read('README.md'),
	long_description_content_type='text/markdown',
	keywords='keeloq microchip code-hopping rolling-code',
	classifiers=[
		'Topic :: Security',
		'Topic :: Security :: Cryptography',
		'License :: Freely Distributable'
	],

	url='https://github.com/socram8888/leekoq',
	project_urls={
		'Bug Tracker': 'https://github.com/socram8888/leekoq/issues',
		'Source Code': 'https://github.com/socram8888/leekoq'
	},

	author='Marcos Del Sol Vives',
	author_email='marcos@orca.pet',
)
