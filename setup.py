#!/usr/bin/python
from distutils.core import setup

setup(
	name = "b2btest",
	version = "1.0",
	requires=['wavefile'],
	description = "Light framework to setup back-to-back test scripts",
	author = "David Garcia Garzon",
	author_email = "voki@canvoki.net",
	url = "https://github.com/vokimon/back2back",
	packages=[
		'b2btest',
		],
	)

