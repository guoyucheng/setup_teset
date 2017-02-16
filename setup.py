from distutils.core import setup
import os

packages = []

current_dir = 'setup_test'
core_dir = "setup_test.core"
packages.append(current_dir)
packages.append(core_dir)
setup(
    name='setup_test', 
    version='1.0',
    url='',
    author='bert', 
    author_email='xx@qq.com',
    packages=packages
)