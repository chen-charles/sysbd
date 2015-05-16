__author__ = 'Charles'

from sysbd import macro

PROJECTPATH = macro.path()

# First Scan, Analyse Module Names
MODULEMAP = dict()

# define how to solve dependencies
solve_dependencies = lambda x: MODULEMAP[x]

# if DEBUG, RUN = print
DEBUG = True
