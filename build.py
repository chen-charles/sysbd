__author__ = 'Charles'

try:

	import os
	import sysbd
	import envir
	import traceback
	import inspect



	print("PROJECTPATH:", envir.PROJECTPATH, end="\n\n")

	# add dependencies as user-defined macros, then solve them during compile time


	# bdr = builder.Builder(mod)
	# bdr.build(envir.solve_dependencies)

	# for name, fullname, root in sysbd.macro.walk(envir.PROJECTPATH, "pybuild"):
	#     print("pybuild found:", fullname, os.path.dirname(fullname))
	#     with open(fullname) as f: exec(f.read(), {"envir": envir, "sysbd": sysbd, "fpath": os.path.dirname(fullname)})

	for name, fullname, root in sysbd.macro.walk(envir.PROJECTPATH, "ini"):
		if name == "module.ini":
			print("module found:", fullname, os.path.dirname(fullname))

			filenames = os.listdir(os.path.dirname(fullname))
			found = None
			for filename in filenames:
				if os.path.isfile(filename) and filename.endswith('.pybuild'):
					found = os.path.dirname(fullname)+os.sep+filename

			if found is not None:
				print("not using default pybuild")
				with open(found) as f: exec(f.read(), {"envir": envir, "sysbd": sysbd, "fpath": os.path.dirname(fullname)})
			else:
				print("using default pybuild")
				if "DEFAULTPYBUILD" not in globals() or "DEFAULTPYBUILD" not in locals():
					with open(os.path.dirname(inspect.getfile(inspect.currentframe()))+os.sep+"pybuild.default") as f: exec(f.read(), {"envir": envir, "sysbd": sysbd, "fpath": os.path.dirname(fullname)})
				else:
					exec(DEFAULTPYBUILD, {"envir": envir, "sysbd": sysbd, "fpath": os.path.dirname(fullname)})
	# you can always redefine the build behaviour
	for i in envir.MODULEMAP.values():
		bdr = sysbd.builder.Builder(i, envir.solve_dependencies)
		bdr.build()
	sysbd.builder.MODULEBUILT.clear()

except Exception as err:
	input("\n\nFailed.  \n%s"%traceback.format_exc())
	exit(1)

input("\n\nSucceeded.  \n")


