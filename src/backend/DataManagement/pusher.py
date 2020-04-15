__doc__="""Takes dataframes completed by overviewer and pushes them to the central
data schema. Guarantees correct typing and secure connection.
"""

# core
from core import environConfig, graphing, images

# third party libs
import pymysql
import pandas as pd
from pandas.io import to_sql
from sqlalchemy.types import Integer, Text, String, DateTime, Numeric, Float, Boolean

# python core
import pickle
import os

#################################################################################
# Globals
RAW_DATA_FIELDS = [
]

ATTRIBUTES = {
}

DEBUG = False

RAW_DF_LIST = []
RAWGLOBAL_DF_LIST = []

baseDir = "WHO"

#################################################################################

def dbConnect():
	# pull sensitive settings from local.env for database login
	env = environConfig.safe_environ()
	URI_str = env("DB_URI")
	engine = create_engine(URI_str)

	return True

def pushFrame(df, con, name):
	"""Write records stored in a DataFrame to a SQL database.

	Databases supported by SQLAlchemy are supported.
	Tables can be newly created, appended to, or overwritten.

	see: pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.to_sql.html
	"""

	_con = connex
	_flavour = "mysql"
	_name = name
	_overwrite_setting = 'replace'
	_schema = "innodb"
	_index = False
	_chunksize = 100
	_method = "multi"

	_dtype = _convertDtypes(df) # dictionary returned

	try:
		df.to_sql(_con, schema=_schema, if_exists=_overwrite_setting, 
				  index=_index, chunksize=_chunksize, dtype=_dtype,
				  method=_method)

		return True
		
	except ValueError as e:
		print(e)
		return False


	def _convertDtypes(df):

		def _switcher(arg):
			switcher = {
				"int64": Integer,
				"float64": Float,
				"object": String,
				"datetime": DateTime,
				"bool": Boolean,
			}

		cols_list = df.columnns.tolist()
		types_list = df.dtypes.tolist()

		for i in range(len(types_list)):
			types_list[i] = _switcher(types_list[i]):

		return dict(zip(cols_list, types_list))