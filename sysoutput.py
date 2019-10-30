import sys
import pip
import os
import pkg_resources
import json
import yaml
import subprocess
import site

ver = sys.version[0:5]
venvname = str(os.environ.get('VIRTUALENV')).split("/")[-1]
exdir = sys.executable
pipdir = "".join(pip.__path__)
pythonpath = str(os.environ.get('PYTHONPATH'))

packages = []

for i in pkg_resources.working_set:
    packages.append(
        "Name: " + i.project_name + ",'Version: " + i.version)

location = "".join(site.getsitepackages())

verdata = subprocess.Popen(['pyenv', 'versions'], stdout=subprocess.PIPE)
versions = verdata.stdout.read()
versions = versions.decode('utf-8').replace(" ", "").split("\n")[:-1]

file = {"Version": ver, "Virtual environment": venvname,
        "Executable location": sys.executable,
        "Pip Location": pipdir,
        "Python path": pythonpath, "Packages": packages,
        "Site-packages location": location,
        "Python versions and environments": versions}

with open("packages.json", 'w') as outfile:
    json.dump(file, outfile, indent=3)

with open("packages.yml", 'w') as outfile:
    yaml.dump(file, outfile, indent=3)
