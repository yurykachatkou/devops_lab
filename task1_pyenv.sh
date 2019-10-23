#!/bin/bash

#installing Python2.7 and Python3.7
pyenv install 2.7.8
pyenv install 3.7.5

#creating virtual enviroments
pyenv virtualenv 2.7.8 MyPyEnv2.7
pyenv virtualenv 3.7.5 MyPyEnv3.7

pyenv activate MyPyEnv3.7

pyenv versions

