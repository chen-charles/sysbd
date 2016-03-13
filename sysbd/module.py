__author__ = 'Charles'

import os
import copy

from . import macro


class Module(object):
    def __init__(self, name, target): self.name = name; self.target = target

    def override(self, subcobj=None):
        if issubclass(subcobj.__class__, self):
            subcobj.compilers = copy.deepcopy(self.compilers)
            subcobj.dependencies = copy.deepcopy(self.dependencies)

    # Details
    name = ""
    target = ""
    path = ""

    # Needed
    compilers = dict()

    dependencies = set()    #module objects
    def solve_dependencies(self, func): self.dependencies = set(map(func, self.dependencies))

    def build(self, link):
        self.make(set(link))

    def make(self, link):
        pass

    def collect(self, ext, parse_inc_sep=os.sep, parse_inc_stat="#include"):
        all_name = list()
        inc_data = dict()
        for name, fullname, root in macro.walk(self.path, ext):
            inc = ["%s "%fullname]
            all_name.append(fullname+".o")  #[:-1-len(ext)]
            for i in self.parse_include(root, name, os.sep): inc.append(i)
            inc_data[fullname] = (" ".join(inc))

        return all_name, inc_data


    macrosdefined = set()
    def parse_include(self, path, name, sep=os.sep, include_stat="#include"):
        skipping = False
        with open(path+sep+name, "r") as f:
            for i in f.readlines():
                if skipping:
                    if "#endif" in i:
                        skipping = False
                    continue

                if "#define" in i:
                    self.macrosdefined.add(i.split()[1])
                    continue

                if "#ifndef" in i:
                    if i.split()[1] in self.macrosdefined:
                        skipping = True
                        continue

                if "#ifdef" in i:
                    if i.split()[1] not in self.macrosdefined:
                        skipping = True
                        continue

                if "#undef" in i:
                    if i.split()[1] in self.macrosdefined:
                        self.macrosdefined.remove(i.split()[1])

                if include_stat in i:
                    if '<' in i or '>' in i:
                        continue
                    elif '\'' in i:
                        t = '\''
                    elif '\"' in i:
                        t = '\"'
                    else:continue
                    i = i[i.index(t)+1:]
                    i = i[:i.index(t)]

                    li = i.split(sep)
                    p = path.split(sep)
                    for j in li:
                        if j == "..":
                            p.pop()
                        elif j == ".":
                            pass
                        else:
                            p.append(j)
                    yield sep.join(p)
                    for j in self.parse_include(sep.join(p[:-1]), p[-1], sep, include_stat): yield j

