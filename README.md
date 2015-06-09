sysbd building system
======

overview
-----------
*sysbd* --- a python 3.x building system  
some efforts are required to make it compatible with python 2.x  
if any problem is encountered during using *sysbd*, feel free to contact me  

directory
-----------
  * ./sysbd  
	python 3 main module directory  
  * ./build.py  
	project loop-through build script, ONE AND ONLY ONE for each project  
  * ./envir.py  
	project loop-through environment, this is passed to every pybuild script for editing and passing global information, ONE AND ONLY ONE for each project  
  * ./module.ini  
	module specific configuration, most attention is needed for this config  
  * ./module.pybuild.update  
	module specific pybuild script, mostly stable, no changes is needed unless you want to perform some specific tasks around the system  
	this file shall be used to call distribute_pybuild.py  
	**module's subdirectorie(s) MUST NOT contain another module**  


  * ./sysbd.md  
    this file  
  * ./distribute_pybuild.py  
    simple utility to loop through PROJECTPATH for distributing pybuild scripts based on configuration files (CHECK THE SCRIPT BEFORE YOU USE)  
	
	
how-to
-----------
  * For every single module of the project, create a configuration file that looks like ./module.ini  
  * Copy ./sysbd ./build.py ./envir.py ./module.pybuild.update ./distribute_pybuild.py into your project path  
  * Run PROJECTPATH/distribute_pybuild.py, input the configuration name and pybuild name(which shall be module.pybuild.update)  
  * Run PROJECTPATH/build.py  


	
