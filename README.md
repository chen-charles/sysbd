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
  * ./module.pybuild  
	module specific pybuild script, mostly stable, no changes is needed unless you want to perform some specific tasks around the system  
	**subdirectorie(s) MUST NOT contain another module**  
  * ./module.ini  
	module specific configuration, most attention is needed for this config  


  * ./sysbd.md  
    this file
  * ./update_pybuild.py  
    simple utility to loop through PROJECTPATH for updating pybuild scripts (CHECK THE SCRIPT BEFORE YOU USE)  
  * ./sample.zip  
	sample project  
	
	
