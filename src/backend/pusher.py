__doc__="""Takes dataframes completed by overviewer and pushes them to the central
data schema. Guarantees correct typing and secure connection.
"""

# core user lib
from core import environConfig


# Python core
import os
import pickle

# third party libs
import pandas as pd
import sqlalchemy
from sqlalchemy.types import Integer, Text, String, DateTime, Numeric, Float, Boolean
import numpy as np

################################################################################
# Globals
# Some defaults in case env var fails.
################################################################################

RAW_DF_LIST = []
RAWGLOBAL_DF_LIST = []
baseDir =  os.path.join(os.path.join(os.pardir, os.pardir), "data") # file name for Raw Data (defaults to my local machine as ../../data)
DEBUG = False                                                      # verbose debug prints
URI_str = ''

################################################################################
# Utilities
################################################################################

def _runStartup():
	"""
	Author: Albert Ferguson
	Explicit startup function. Runs any necessary preloads for data and Globals updates.
	"""
	# env = environConfig.safe_environ()

	global DEBUG
	global RAW_DF_LIST
	global RAWGLOBAL_DF_LIST
	global baseDir

	# update with the env config
	# DEBUG = env("DEBUG")
	# baseDir = env("BASE_DATA_DIR")

	try:
		# call the read binary to read-in the data frames RAW
		with open(os.path.join(baseDir, "processing_dump.txt"), "rb") as f:
			RAW_DF_LIST = pickle.load(f)

		# call the read binary to read-in the global data frames RAW
		with open(os.path.join(baseDir, "globaldata_processing_dump.txt"), "rb") as f:
			RAWGLOBAL_DF_LIST = pickle.load(f)

	except FileNotFoundError:
		return False
	
	except AttributeError:
		return False

	return True

def dbConnect():
	"""
	Author: Albert Ferguson
	Create a new connection to the desired db engine. This setting is
	controlled via the environ settings according to 12 Factor methods.
	
	Returns: engine, the db engine
	"""

	global URI_str
	URI_str = env("DB_URI")
	
	engine = sqlalchemy.create_engine(URI_str)

	return engine

################################################################################
# Database interactors
################################################################################

def pushFrame(df, connex, name, schema):
	"""Write records stored in a DataFrame to a SQL database.

	Databases supported by SQLAlchemy are supported.
	Tables can be newly created, appended to, or overwritten.

	see: pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.to_sql.html
	"""

	def _convertDtypes(df):
		switcher = {
			np.dtype("int64"): Integer,
			np.dtype("float64"): Float,
			np.dtype("object"): String(32),
			np.dtype("datetime64"): DateTime,
			np.dtype("bool"): Boolean,
		}

		cols_list = df.columns.tolist()
		types_list = df.dtypes.tolist()

		# use our type dict switcher to switch on the type and swap them for verbose ones
		for i in range(len(types_list)): types_list[i] = switcher[types_list[i]]
		# dict cast the zip of verbose type lists
		return dict(zip(cols_list, types_list))

	_con = connex
	_name = name
	_overwrite_setting = 'replace'
	_schema = schema
	_index = True
	_chunksize = 100
	_method = "multi"

	_dtype = _convertDtypes(df) # dictionary returned

	try:
		df.to_sql(name, con=_con, schema=_schema, if_exists=_overwrite_setting,
                          index=_index, chunksize=_chunksize, dtype=_dtype,
                          method=_method)
		#df.to_sql(name, con=_con, dtype=_dtype)
		print(connex.execute("SELECT * FROM {}.{}".format(schema, name)).fetchall()[:10])
		
		return True # only valid exit point

	except ValueError:
		return False

	return False

def push(df, name, opt):
	"""Note, schema is the db to write to within our MySQL storage."""
	return pushFrame(df, dbConnect(), name, opt)

def pushAll():
	try:
		for df in RAW_DF_LIST:
			print(df["schema"].iloc[0])
			if not push(df, df["schema"].iloc[0], "rawdata"):
				return False

		for df in RAWGLOBAL_DF_LIST:
			print(df["schema"].iloc[0])
			if not push(df, df["schema"].iloc[0]+"_GLOBAL",  "rawdata"):
				return False

	except AttributeError:
		return False

	return True

################################################################################
# Main
################################################################################

if not _runStartup():
	print("UNCAUGHT STARTUP ERROR.")

if DEBUG:
	print("\n\nDF INFO\n{}\t{}\n".format(len(RAW_DF_LIST), len(RAWGLOBAL_DF_LIST)))

pushAll() # atm just push all, this script isn't called otherwise
