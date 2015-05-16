__author__ = 'Charles'

import os
import subprocess

def path(): return os.getcwd()

def walk(path, ext):
    for root, dirs, files in os.walk(path):
        for name in files:
            if name.split(".")[-1].lower() == ext.lower():
                yield name, os.path.join(root, name), root

def launch(command):
    subproc = subprocess.Popen(command, stderr=subprocess.STDOUT)
    return subproc.wait()
