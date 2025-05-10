"""Projeto-PyDirDbJson - setup.py

Script para criação do setup do pypi

"""
from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name='pydirdbjson',
    version='1.0.0',
    packages=find_packages(),
    description='Project Database in JSON on directory',
    author='Ricardo P Ferreras',
    author_email='ricardo.ferreras@gmail.com',
    url='https://github.com/FerrerasRP',
    license='MIT',
    long_description=long_description,
    long_description_content_type='text/markdown'
)
