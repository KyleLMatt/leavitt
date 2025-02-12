#!/usr/bin/env python

#from distutils.core import setup
from setuptools import setup, find_packages

setup(name='Leavitt',
      version='1.0.0',
      description='Variable star fitting code',
      author='Kyle Matt, David Nidever',
      author_email='kylematt@montana.edu',
      url='https://github.com/KyleLMatt/leavitt',
      packages=find_packages(exclude=["tests"]),
      scripts=['bin/leavitt'],
      install_requires=['numpy','astropy(>=4.0)','scipy','dlnpyutils(>=1.0.3)'],
      #install_requires=['numpy','astropy(>=4.0)','scipy','the-cannon','dlnpyutils(>=1.0.2)','emcee','corner'],
      include_package_data=True,
)
