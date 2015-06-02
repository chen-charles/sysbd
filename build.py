__author__ = 'Charles'

try:
    
    import os
    import sysbd
    import envir

    print("PROJECTPATH:", envir.PROJECTPATH)

    # add dependencies as user-defined macros, then solve them during compile time


    # bdr = builder.Builder(mod)
    # bdr.build(envir.solve_dependencies)

    for name, fullname, root in sysbd.macro.walk(envir.PROJECTPATH, "pybuild"):
        print("pybuild found:", fullname)
        with open(fullname) as f: exec(f.read(), {"envir": envir, "sysbd": sysbd, "fpath": os.path.dirname(fullname)})

    # you can always redefine the build behaviour
    for i in envir.MODULEMAP.values():
        bdr = sysbd.builder.Builder(i, envir.solve_dependencies)
        bdr.build()
    sysbd.builder.MODULEBUILT.clear()

except Exception as err:
    input("\n\nFailed.  \n%s\t%s\n"%(str(err), str(type(err))))
    exit(1)

input("\n\nSucceeded.  \n")
    

