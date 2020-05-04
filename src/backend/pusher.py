__doc__="""Takes dataframes completed by overviewer and pushes them to the central
data schema. Guarantees correct typing and secure connection.
"""

# core
from core import environConfig

# third party libs
import pandas as pd
import sqlalchemy
from sqlalchemy.types import Integer, Text, String, DateTime, Numeric, Float, Boolean

# python core
import pickle
import os

#################################################################################
# Globals
env = environConfig.safe_environ()

DEBUG = env.bool("DEBUG")
RAW_DF_LIST = []
RAWGLOBAL_DF_LIST = []
baseDir = env.str("BASE_DATA_DIR")

#################################################################################

def dbConnect():
	# pull sensitive settings from local.env for database login
	env = environConfig.safe_environ()
	URI_str = env("DB_URI")
	engine = sqlalchemy.create_engine(URI_str)
	print(engine)

	return engine

def pushFrame(df, connex, name, schema):
	"""Write records stored in a DataFrame to a SQL database.

	Databases supported by SQLAlchemy are supported.
	Tables can be newly created, appended to, or overwritten.

	see: pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.to_sql.html
	"""

	def _convertDtypes(df):

		def _switcher(arg):
			switcher = {
				"int64": Integer,
				"float64": Float,
				"object": String(32),
				"datetime": DateTime,
				"bool": Boolean,
			}

		cols_list = df.columns.tolist()
		types_list = df.dtypes.tolist()

		for i in range(len(types_list)):
			types_list[i] = _switcher(types_list[i])

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
		#df.to_sql(name, con=_con, schema=_schema, if_exists=_overwrite_setting,
                #          index=_index, chunksize=_chunksize, dtype=_dtype,
                #          method=_method)
		df.to_sql(name, con=_con, dtype=_dtype)
		connex.execute("SELECT * FROM {}".format(name)).fetchall
		print()

	except ValueError as e:
		print(e)
		return False

		return True


# public interface
def push(df, name, opt):
        """Note, schema is the db to write to within our MySQL storage."""
        return pushFrame(df, dbConnect(), name, opt)

# test
with open(os.path.join(baseDir, "processing_dump.txt"), "rb") as procData:
        RAWDF_LIST = pickle.load(procData)
with open(os.path.join(baseDir, "globaldata_processing_dump.txt"), "rb") as globData:
        RAWGLOBAL_DF_LIST = pickle.load(globData)

for df in RAW_DF_LIST:
        push(df, df["schema"].iloc[0], "rawdata")

for df in RAWGLOBAL_DF_LIST:
        push(df, df["schema"].iloc[0],  "rawdata")
