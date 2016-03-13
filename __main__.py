import pkg_resources
DEFAULTPYBUILD = pkg_resources.resource_string(__name__, 'pybuild.default')
exec(pkg_resources.resource_string(__name__, 'build.py'), {"DEFAULTPYBUILD": DEFAULTPYBUILD})
