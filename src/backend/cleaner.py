__doc__ = """Cleaner runs the prechecks and initial import of any data sources \
we pull. This includes NaN, duplicate, missing data, erroneous strings checks as \
well as label encoding for binary and categorical data."""

# core user lib
from .core import environConfig

# Python core
import math
import time
import pickle
import os

# third party libs
import pandas as pd
import numpy as np
from sklearn import preprocessing as pre
from sklearn.impute import SimpleImputer

################################################################################
# Globals
# Some defaults in case env var fails.
################################################################################

ATTRIBUTES = {}
RAW_DF_LIST = []
RAWGLOBAL_DF_LIST = []
DEBUG = False                                                      # verbose debug prints
baseDir = "data" # file name for Raw Data (defaults to my local machine as ../../data)

################################################################################
# Utilities
################################################################################

def _runStartup():
	"""
	:author Albert Ferguson
	Explicit startup function. Runs any necessary preloads for data and Globals updates.
	Retrieves raw data and assigns Globals to env vars, runs default ones gracefully otherwise.
	"""

	# local dev, comment this out
	env = environConfig.safe_environ()

	global RAW_DF_LIST
	global DEBUG
	global baseDir
	global RAWGLOBAL_DF_LIST
	global ATTRIBUTES

	# update with the env config
	DEBUG   = env.bool("DEBUG", False)
	baseDir = env("BASE_DATA_DIR")

	# retrieve the WHO Indicator Data and create a HDF (human data format) checklist
	try:
		# data/WHO_INDICATORS.txt
		who_fn = os.path.join(baseDir, "data", "WHO", "WHO_INDICATORS.txt")
		with open(who_fn, "rb") as whoIndicators:
			ATTRIBUTES = pickle.load(whoIndicators)

		for attributeID in ATTRIBUTES.values():
			# data/WHO/*.csv
			fn = os.path.join(os.path.join(baseDir, "WHO"), attributeID+".csv")
			RAW_DF_LIST.append(pd.read_csv(fn, index_col=0, parse_dates=True))

		# data/ECDC/COVID-19-geographic-disbtribution-worldwide.xlsx
		ecdc_path = os.path.join(os.path.join(baseDir, "ECDC"), "COVID-19-geographic-disbtribution-worldwide.xlsx")
		RAW_DF_LIST.append(pd.read_excel(ecdc_path))
	
	except FileNotFoundError:
		return False

	# TODO: add 1point3acres stuff here once granted access

	# TODO: add Economic data stuff here once data sourced

	return True

################################################################################
# Cleaners (NaNs, dups, imputators...)
################################################################################

def dropConstantColumns(df):
	# 1. Determine number of unique values in a column, mask for 1
	dataUnique_boolarr = df.nunique().isin([1])


	if True not in dataUnique_boolarr:
		return False

	# 2. Drop every column we masked as True
	dropColumns = df.loc[:, dataUnique_boolarr].columns
	df.drop(dropColumns, inplace=True, axis=1)

	return True

def dropHighNaNCols(df):
	# 1. Get the total sum of NaN values (sum of fields and sum of sums)
	NaNCount = df.isna().sum().sum()

	if NaNCount is 0:
		return True

	# from prev analysis, Low and High dimensions are often full NaN
	# often Numeric is too (when the data is binary in a diff dimension)
	try:
		# 2. start by dropping 100% NaN column.
		df.dropna(how="all", inplace=True, axis=1)
		# 3. Then drop any columns missing at least floor(45% of data).
		alpha = math.floor(0.45*len(df))
		df.dropna(thresh=alpha, inplace=True, axis=1)
		return True

	except AttributeError:
		print("dropHighNaNCols: AttributeError")
		return False

	# how did you get here?
	return False

def imputateNaNs(df):
	# A. pre, return immediately if no NaNs in df.
	if df.isna().sum().sum() is 0:
		return True

	# B. pre, run a constant imputate for any object dtype cols with "No data".
	constantImpNoData= SimpleImputer(missing_values="No data", strategy="constant",
								fill_value=0)
	# B2. pre, run another check and imputate for any object dtype cols with "Don't Know".
	constantImpDontKnow = SimpleImputer(missing_values="Don't know", strategy="constant",
								fill_value="No")

	# B3. pre, run another check and imputate for any object dtype cols with "Other"
	constantImpOther = SimpleImputer(missing_values="Other", strategy="constant",
								fill_value=0)

	# C. run constant imputator where missing values present.
	columns_list = df.columns

	for col in columns_list:
		"""
		Creates warning:
		FutureWarning: elementwise comparison failed; returning scalar instead,
		but in the future will perform elementwise comparison
		"""

		if (df.loc[:,col] == "Other").any():
			df[col] = constantImpOther.fit_transform(df[[col]])
			try:
				df[col] = df[[col]].astype("int64")
			except ValueError:
				pass
		if (df.loc[:,col] == "Don't know").any():
			df[col] = constantImpDontKnow.fit_transform(df[[col]])
			try:
				df[col] = df[col].astype("object")
			except ValueError:
				pass
		if (df.loc[:,col] == "No data").any():
			df[col] = constantImpNoData.fit_transform(df[[col]])
			try:
				df[col] = df[col].astype("float64")
			except ValueError:
				pass
		
	if DEBUG == True:
		print("imputateNaNs: Constant adjustments completed")

	# 1. Select the cols with NaN data, where dtype is integer/
	integerNANCols_df = df.select_dtypes(include=np.number)

	# 2. setup a simple imputator for replacing values with their series mean/
	nanImp = SimpleImputer(missing_values=np.nan, strategy="mean")
	
	# 3. Use integerNANCols_df for column-wise transforms/
	for col in integerNANCols_df:
		nanValCheck_boolarr = df.loc[:, col].isna()
		if nanValCheck_boolarr.sum() > 0:
			df[col] = nanImp.fit_transform(df[[col]])
	
	if DEBUG == True:
		print("imputateNaNs: imputation completed")
		print("imputateNaNs:\n{}".format(df.head()))
		print("imputateNaNs:\n{}".format(df.dtypes))
		print("\t###\n")

	return True

def splitGlobalStats(df):
	# 1. Check if GLOBALS val in REGION dimension
	try:
		globalCheck_boolarr = df.REGION == "GLOBAL"

		if globalCheck_boolarr.sum() > 0:
			# 2. retrieve indexes of GLOBAL stats
			globals_df = df[globalCheck_boolarr]
			
			if DEBUG == True:
				print("splitGlobalStats: dropped and added global dat\n")
				print("\t###\n")

			idxs = df.loc[globalCheck_boolarr].index
			df.drop(idxs, inplace=True)
			return globals_df
		else:
			# REGION dimension exists but no GLOBALS in it
			return False

	except AttributeError:
		# no REGION dimension, skip
		print("AttributeError")
		return False

	# how did you get here?
	return False

def dropIndex(df):
	try:
		df.drop("Unnamed: 0", axis=1, inplace=True)
		return True
	except KeyError:
		# no default index to drop
		return False

	# how did you get here?
	return False

def binaryPreProcessor(df):
	# 1. Determine number of unique values in a column, mask for 2
	binaryCols_boolarr = df.nunique() == 2
	binaryCols_list = df.columns[binaryCols_boolarr]
	
	if DEBUG == True:
		print("binaryPreProcessor:\n{}\n".format(df.nunique()))
		print("binaryPreProcessor: binary columns to adjust\n{}\n\n".format(binaryCols_boolarr))

	if binaryCols_boolarr is False:
		return False

	# 2. Encode the column to [0,1]
	# encode on the discrete range [0, 1, ..., n - 1, n]
	ordinalEncoder = pre.OrdinalEncoder()
	binaryDimensions_df = df[binaryCols_list]
	
	for col in binaryCols_list:
		try:
			# df[col] = ordinalEncoder.fit_transform(df[[col]]).astype('bool')
			# Append the encoded rather than over writing
			new_col = col + '_binary_encoding'
			df[new_col] = ordinalEncoder.fit_transform(df[[col]]).astype('bool')

			if DEBUG == True:
				print("binaryPreProcessor:\n{}\n".format(df[[col]]))
				print("\t###\n")

		except AttributeError:
			print("binaryPreProcessor: AttributeError")
			pass

	return True

def encodeCategoricals(df):
	# 1. Determine discrete values that are categorical.
	categoricalCols_df = df.select_dtypes(include=["object"])

	if categoricalCols_df.empty:
		return False

	# 2. Create a label encoder for each dimension of categoricals.
	# encode on the discrete range [0, 1, ..., n - 1, n]
	# NOTE: this may be incorrect depending on latter fitting algorithms
	#		as they may assume continuous when these are arbitrarily ordered!
	ordinalEncoder = pre.OrdinalEncoder()

	if DEBUG == True:
		print("encodeCategoricals: categorical columns\n{}".format(categoricalCols_df.head()))

	for col in categoricalCols_df.columns:
		if col == "schema":
			continue

		try:
			if DEBUG == True:
				print("encodeCategoricals: attempting\n{}".format(col))
			# df[[col]] = ordinalEncoder.fit_transform(df[[col]])
			# Append the encoded rather than over writing
			new_col = col + '_encoding'
			df[new_col] = ordinalEncoder.fit_transform(df[[col]])

		except AttributeError:
			print("encodeCategoricals: AttributeError")
			pass
		except TypeError:
			print("encodeCategoricals: TypeError")
			pass

	return True

def numericaliseDisplayValueDimension(displayValueColumn):
	try:
		# CASE: float or int value with spaces and formatting
		return displayValueColumn.str[0:5].astype("float64")
	except ValueError:
		# CASE: string binary value, doesnt require adjustments
		return displayValueColumn
	except AttributeError:
		# CASE: imputateNaNs inserted a zero, this is now int64 type.
		return displayValueColumn
	except TypeError:
		# CASE: an int was passed instead of str, skip the subscript
		return displayValueColumn

# implements all of the above
def runPreChecks():
	# TODO: return as bool for eval checks
	
	global RAW_DF_LIST
	global RAWGLOBAL_DF_LIST
	
	i = 1
	for raw_df in RAW_DF_LIST:
		if DEBUG  == True:
			print(DEBUG)
			print("\n\n#################################################################################")
			print("CURRENT FRAME:", i)
			#print("Source Name:\t", list(ATTRIBUTES.values())[i])
			print("runPreChecks:\n{}".format(raw_df.head(),"\n"))

		#####
		# 1. Drop any immediately irrelevant columns here.
		#    Then drop any duplicate rows, constant columns, 
		#    index if it exists, global data and any high Nan content.
		#	 Apply database normalisation rules: if a col depends on
		#	 calc's from another, drop it.
		#####

		drops_list = [
		"Comments", "PUBLISHSTATE","Display Value",
		"High", "Low", "DATASOURCE", "DHSMICSGEOREGION",
		"REGION", "geoId",
		]

		# if from GHO, drop the "GHO" column
		if "GHO" in raw_df.columns:
			raw_df.rename(columns={"GHO":"schema"}, inplace=True)
		else:
			# add a name identifier for indexing in our db later
			raw_df["schema"] = "COVID19"

		for col in drops_list:
			try:
				if col in raw_df.columns:
					raw_df.drop(columns=col, inplace=True, axis=1)
				else:
					pass
			except KeyError:
				pass

		dropIndex(raw_df)
		dropConstantColumns(raw_df)
		raw_df.drop_duplicates(ignore_index=True, inplace=True)

		globalDataRes = splitGlobalStats(raw_df)
		if type(globalDataRes) is pd.DataFrame:
			# add the global data to its own list
			if DEBUG == True:
				print("runPreChecks: GLOBAL DF DESCRIBE:\n{}\n".format(globalDataRes.head()))
			
			RAWGLOBAL_DF_LIST.append(globalDataRes)
		
		dropHighNaNCols(raw_df)

		####
		# 2. Apply imputations to remove remaining NaN values
		####
		imputateNaNs(raw_df)
		# drop any remaining rows with NaN data (usually WHO regions)
		raw_df.dropna(inplace=True)

		####
		# 3. Adjust encoding for binaries
		####
		binaryPreProcessor(raw_df)

		####
		# 4. Complete the string manipulation to change Display Value to
		#    correct type and remove erroneous string content.
		####
		if "Display Value" in raw_df.columns and raw_df["Display Value"].dtype == np.object:
			if DEBUG == True:
				print("\nrunPreChecks: Adjusting Display Value type.\n")
			raw_df["Display Value"] = numericaliseDisplayValueDimension(raw_df["Display Value"])
			
			try:
				raw_df["Display Value"] = raw_df["Display Value"].astype("float64")
			except ValueError as e:
				if DEBUG == True:
					print("\n###\nrunPreChecks:", e, "\n###\n")

		####
		# 5. Adjust labelling on categoricals, imputating values
		####
		encodeCategoricals(raw_df)

		# debug prints and counter update
		if DEBUG == True:
			print(raw_df.head())
			input()

		i += 1

def output():
	global ATTRIBUTES
	global RAWGLOBAL_DF_LIST
	global RAW_DF_LIST

	try:
		with open(os.path.join(baseDir, "Table Checklist.txt"), 'w+') as hdf_checklist:
			hdf_checklist.write("WHO Indicator Data\n\n")

			for key in ATTRIBUTES:
				hdf_checklist.write(ATTRIBUTES[key] + ":\t\t" + key)
				hdf_checklist.write("\n")

			hdf_checklist.write("\nECDC Sars-Cov2 Data (AKA COVID19)\n\n")
			hdf_checklist.write("COVID19:\t\tCOVID-19-geographic-disbtribution-worldwide")

		with open(os.path.join(baseDir,"processing_dump.txt"), "wb") as fn:
			pickle.dump(RAW_DF_LIST, fn)

		with open(os.path.join(baseDir, "globaldata_processing_dump.txt"), "wb") as fn:
			pickle.dump(RAWGLOBAL_DF_LIST, fn)
	
	except FileExistsError:
		return False

	except AttributeError:
		return False

	return True

################################################################################
# Main
################################################################################

def main():
	if not _runStartup():
		print("THERE WAS AN UNCAUGHT STARTUP ERROR")

	runPreChecks() # run prechecks

	if DEBUG:
		print("\t###\n")
		print("\tWRITING TO BINARY DUMP...")
		print("\t###\n")

		for df in RAW_DF_LIST:
			print(df.head())

	output() # write output to file dumps


if __name__ == "__main__":
	main()

