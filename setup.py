# -*- coding: utf-8 -*-
from setuptools import setup, find_packages
import re, ast

with open('requirements.txt') as f:
	install_requires = f.read().strip().split('\n')

# get version from __version__ variable in custom_lcv/__init__.py
_version_re = re.compile(r'__version__\s+=\s+(.*)')

with open('custom_lcv/__init__.py', 'rb') as f:
	version = str(ast.literal_eval(_version_re.search(
		f.read().decode('utf-8')).group(1)))

setup(
	name='custom_lcv',
	version=version,
	description='Custom LCV Document for ERPNext V10 with additional functionality such as distribution by weight and automatic Journal Entry creation',
	author='Saif Ur Rehman',
	author_email='saifi0102@gmail.com',
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
