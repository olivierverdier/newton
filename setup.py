#!/usr/bin/env python
# coding: UTF-8


from distutils.core import setup

setup(
	name         = 'newton',
	version      = '0.1',
	description  = 'Wrapper around a nonlinear solver',
	author = 'Olivier Verdier',
	url = 'https://github.com/olivierverdier/newton',
	license      = 'MIT',
	keywords = ['Math', 'Nonlinear solver', 'Newton',],
	packages=['newton',],
	classifiers = [
	'Development Status :: 4 - Beta',
	'Intended Audience :: Science/Research',
	'License :: OSI Approved :: BSD License',
	'Operating System :: OS Independent',
	'Programming Language :: Python',
	'Topic :: Scientific/Engineering :: Mathematics',
	],
	)
