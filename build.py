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
    bdr = sysbd.builder.Builder(list(envir.MODULEMAP.values())[0], envir.solve_dependencies)
    bdr.build()

except Exception as err:
    input("\n\nFailed.  \n%s\t%s\n"%(str(err), str(type(err))))
    exit(1)

input("\n\nSucceeded.  \n")
    

