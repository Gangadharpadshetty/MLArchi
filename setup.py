# Ensure the current working directory is in the sys.path
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))

from setuptools import setup, find_packages
from typing import List
import os
import sys
def get_requirements(file_path: str) -> List[str]:
    with open(file_path, 'r') as file:
        return file.read().splitlines()
    

setup(
name='MLops',
version='0.1',
description='A machine learning operations project',
author='gangadhar',
packages=find_packages(),
install_requires=get_requirements('requirement.txt'),                
)