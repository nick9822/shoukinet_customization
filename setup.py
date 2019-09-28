# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

with open('requirements.txt') as f:
	install_requires = f.read().strip().split('\n')

# get version from __version__ variable in shoukinet_customization/__init__.py
from shoukinet_customization import __version__ as version

setup(
	name='shoukinet_customization',
	version=version,
	description='Customzitaion for Shoukinet',
	author='GoElite',
	author_email='contact@goelite.in',
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
