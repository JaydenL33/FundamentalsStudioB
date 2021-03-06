import os
import sys
from environs import Env

def safe_environ():
	"""Check for the environment settings and config file. Attempt to gracefully
	import the local.env file and deal with a FileNotFoundError or other
	configuration error.

	Returns
	----------
	env, Env builtin object
		the environemtn class object is returned on successful detection of the
		local.env file
	default_warn, str
		this is returned if the file cannot be found. Prints a message to stderr
	"""

	default_warn = "[ENVIRON SETTINGS] Environment settings not found"
	try:
		# grab local environ settings and attempt to read settings file
		env = Env()
		parent = os.path.abspath(os.pardir)
		target = ".env"
		env_file = os.path.abspath(os.path.join(parent, target))
		print(env_file)
		env.read_env(env_file, recurse=False)
		return env
	except FileNotFoundError:
		return sys.exit(default_warn)
