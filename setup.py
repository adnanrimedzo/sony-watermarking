# -*- coding: utf-8 -*-

from setuptools import setup, find_packages


with open('README.rst') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='sony.watermarking',
    version='0.1.0',
    description='Watermarking core application for Sony',
    long_description=readme,
    author='Adnan Ozdemir',
    author_email='adnanrimedzo@hotmail.com',
    url='https://github.com/adnanrimedzo/sonyWaterMarking',
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)

