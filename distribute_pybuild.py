__author__ = 'Charles'

import os
import sysbd
import envir

print(envir.PROJECTPATH)
ini_fname = input("-> ini file name: ")
with open(input("-> pybuild file name: ")) as f:
    new_ver = f.read()

for root, dirs, files in os.walk(envir.PROJECTPATH):
    for name in files:
        if name == ini_fname:
            print("ini found: ", str(os.path.join(root, name)))
            with open(os.path.dirname(str(os.path.join(root, name)))+os.sep+"module.pybuild", "w") as f:
                f.write(new_ver)


input("-> Distributed.  ")
