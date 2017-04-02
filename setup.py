#!/usr/bin/env python
#coding:utf-8
"""
  Author:   --<v1ll4n>
  Purpose: Installer
  Created: 03/29/17
"""

from codecs import open as copen
from setuptools import setup, find_packages

packages = find_packages()

requires = ['g3ar',]

version = '0.3.5'

#
# LOAD README.md
#
try:
    readme = None
    with copen('README.md',  encoding='utf-8') as f:
        readme = f.read()

except:
    readme = 'Python2 fuzzkit 模版与字符 fuzz \n' + \
        'Github: https://github.com/VillanCh/fuzzkit'


    
setup(
    name='fuzzkit',
    version=version,
    description='Python2 Fuzzkit.',
    long_description=readme + '\n\n',
    author='v1ll4n',
    author_email='v1ll4n@villanch.top',
    url='https://github.com/VillanCh/fuzzkit',
    packages=packages,
    package_data={"":["LICENSE", 'README.md',]},
    package_dir={'fuzzkit':'fuzzkit'},
    include_package_data=True,
    install_requires=requires,
    license='BSD 2-Clause License',
    zip_safe=False,
)
