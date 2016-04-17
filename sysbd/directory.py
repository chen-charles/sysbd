__author__ = 'Charles'

import os

from . import macro
#import macro

class Directory(object):
	def __init__(self, name, parentDir, isModule=False):
		self.parent = parentDir
		self.children = set()
		self.parent.add(self)
		self.name = name
		self.isModule = bool(isModule)


	def getPath(self):
		return self.parent.getPath() + os.sep + self.name

	def add(self, directory):
		self.children.add(directory)

class DirectoryRoot(Directory):
	def __init__(self, name, fullpath, isModule=False):
		super(DirectoryRoot, self).__init__(name, self, isModule)
		self.fullpath = fullpath
		self.children.clear()

	def getPath(self):
		return self.fullpath

def buildTree(ppath):
	dirDict = dict()
	dirDict[ppath] = DirectoryRoot("", ppath)

	for dirpath, dirs, files in os.walk(ppath):
		if dirpath == ppath: continue
		dirDict[dirpath] = Directory(dirpath.split(os.sep)[-1], dirDict[os.sep.join(dirpath.split(os.sep)[:-1])])

	return dirDict[ppath]

def buildModuleTree(ppath, modulefname="module.ini"):
	dirDict = dict()
	dirDict[ppath] = DirectoryRoot("", ppath)

	for dirpath, dirs, files in os.walk(ppath):
		if dirpath == ppath:
			if modulefname in files: dirDict[dirpath].isModule = True
			continue

		dirDict[dirpath] = Directory(dirpath.split(os.sep)[-1], dirDict[os.sep.join(dirpath.split(os.sep)[:-1])])
		if modulefname in files: dirDict[dirpath].isModule = True

	return dirDict

def dwalk(ppath, modulefname="module.ini"):
	mTree = buildModuleTree(ppath, modulefname)
	for dirpath, dirs, files in os.walk(ppath):
		t = dirs
		for i in t:
			p = os.path.join(dirpath, i)
			if mTree[p].isModule: dirs.remove(i)
		yield dirpath, dirs, files

def dwalkext(path, ext, modulefname="module.ini"):
	for root, dirs, files in dwalk(path, modulefname):
		for name in files:
			if name.split(".")[-1].lower() == ext.lower():
				yield name, os.path.join(root, name), root
