__author__ = 'Charles'

import os
from . import module

MODULEBUILT = set()

class Builder(object):
    def __init__(self, mod, solve_dependencies):
        if issubclass(mod.__class__, module.Module):
            mod.solve_dependencies(solve_dependencies)
            self.solve_dependencies = solve_dependencies
            self.pending = mod.dependencies
            self.mod = mod
        else: raise TypeError("the given object's class is not derived from Module, given: %s, with content: "%str(mod.__class__) + str(mod))

    link = set()

    def build(self):
        if self.mod in MODULEBUILT: return
        while self.pending:
            i = self.pending.pop()
            try:
                bdr = Builder(i, self.solve_dependencies)
                bdr.build()
            except Exception as err:
                self.pending.add(i)
                raise err
            self.link.add(i.path+os.sep+i.target)

        self.mod.build(self.link)
        MODULEBUILT.add(self.mod)

