# -*- coding: utf-8 -*-
"""
Created on Fri Feb 10 01:23:35 2023

@author: deep.shah
"""
import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name='aiart',
    version='0.0.1',
    author='Deep Shah',
    author_email='er.deep.shah@gmail.com',
    description='Server repo for theaiart.in colab server',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/erdeepshah/aiart',
    license='Apache License 2.0',
    packages=['aiart'],
    install_requires=['diffusers','transformers','scipy','ftfy','accelerate','flask','requests'],
)