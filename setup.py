"""Installation file"""

from setuptools import setup, find_packages

with open('requirements.txt', encoding='UTF-8') as f:
    requirements = f.read().splitlines()

setup(name='ibm-translator-project',
      version='1.0',
      description='IBM translator project for evaluation',
      author='Henri Saubatte',
      packages=find_packages(),
      install_requires=requirements
      )
