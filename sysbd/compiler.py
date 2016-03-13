__author__ = 'Charles'


class Compiler(object):
	def __init__(self, *args):
		if len(args) == 2:
			self.cmd = args[0]
			self.flags = args[1]
		self.mkcompstr = lambda compilerMacro, compilerFlagsMacro: "$(%s) $(%s) $< -o $@"%(compilerMacro, compilerFlagsMacro)
	cmd = ""
	flags = ""
	def mkfstr(self, compilerMacro, compilerFlagsMacro): return """\n%s\t=\t%s\n%s\t=\t%s\n"""%(compilerMacro, self.cmd, compilerFlagsMacro, self.flags)

class Linker(Compiler):
	pass
