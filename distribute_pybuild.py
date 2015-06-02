__author__ = 'Charles'

import os
import sysbd
import envir

ini_fname = input("-> ini file name: ")
with open(input("-> pybuild file name: ")) as f:
    new_ver = f.read()

for name, fullname, root in os.walk(envir.PROJECTPATH):
    if name == ini_fname:
        print("ini found: ", fullname)
        with open(os.path.dirname(fullname)+os.sep+"module.pybuild", "w") as f: f.write(new_ver)
        
input()
