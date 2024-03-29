
# -*- coding=utf-8 -*-
# Name: teddy oweh
# Email: teddy@teddyoweh.com
# Message: Feel Free To Contact Me on Enquires or Question, il Reply :)mport pathlib

from setuptools import setup, find_packages
import pathlib
 
HERE = pathlib.Path(__file__).parent

 
README = (HERE / "README.md").read_text()
 
setup(
    name="BeardbAPI",
    version="0.0.6",
    description="Microservice to deploy Beardb Secured Databases Remotely.",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/teddyoweh/beardb-api",
    author="Teddy Oweh",
    author_email="teddyoweh@gmail.com",
    packages=find_packages(),
 
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.11",
    ],
  
    include_package_data=True,
    install_requires=['cryptography','requests','flask_cors','flask','werkzeug','gunicorn'],
  
)