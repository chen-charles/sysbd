__author__ = 'Charles'

import os
import sysbd
import envir

with open(input("-> new file name: ")) as f:
    new_ver = f.read()

for name, fullname, root in sysbd.macro.walk(envir.PROJECTPATH, "pybuild"):
    print("pybuild found:", fullname)
    with open(fullname, "w") as f: f.write(new_ver)
        
input()
