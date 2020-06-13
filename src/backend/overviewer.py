__doc__="""Overviewer runs the prechecks and initial import of any data sources
we pull. This includes NaN, duplicate, missing data, erroneous strings checks as
well as label encoding for binary and categorical data.
"""

# core
from .core import environConfig

# third party libs
import pandas as pd
import numpy as np
from sklearn import preprocessing as pre
from sklearn.impute import SimpleImputer

# python core
import math
import time
import pickle
import os

#################################################################################
# Globals
env = environConfig.safe_environ()

ATTRIBUTES = {
}

RAW_DF_LIST = []
RAWGLOBAL_DF_LIST = []

DEBUG   = env.bool("DEBUG", False)

baseDir = env("BASE_DATA_DIR")

#################################################################################



#################################################################################
# Load up the raw data

# retrieve the WHO Indicator Data and create a HDF (human data format) checklist
with open(os.path.join(baseDir, "data", "WHO", "WHO_INDICATORS.txt"), "rb") as whoIndicators:
	ATTRIBUTES = pickle.load(whoIndicators)

for attributeID in ATTRIBUTES.values():
	fn = os.path.join(baseDir, 'data', 'WHO', attributeID+".csv")
	RAW_DF_LIST.append(pd.read_csv(fn, index_col=0, parse_dates=True))

ecdc_path = os.path.join(baseDir, "data", "ECDC", "COVID-19-geographic-disbtribution-worldwide.xlsx")
RAW_DF_LIST.append(pd.read_excel(ecdc_path))

# TODO: add 1point3acres stuff here once granted access

# TODO: add Economic data stuff here once data sourced

#################################################################################

#################################################################################
# Sanity, NaN, Null, zero dev checks

def dropConstantColumns(df):
	 """
    Author : Albert Ferguson
    Brief  : Dropping columns with unique data within a given dataframe
    Details:
        

    Param  : df, a dataframe containing all the relevant columns that contain
			unique values that are to be dropped. 
            
            
    Note   : This method helps filter values for effective data mining. 
    Returns: the dataframe with filtered unique values
    """
	# 1. Determine number of unique values in a column, mask for 1
	dataUnique_boolarr = df.nunique().isin([1])


	if True not in dataUnique_boolarr:
		return False

	# 2. Drop every column we masked as True
	dropColumns = df.loc[:, dataUnique_boolarr].columns
	df.drop(dropColumns, inplace=True, axis=1)

	return True

def dropHighNaNCols(df):
		 """
    Author : Albert Ferguson
    Brief  : Dropping the NaN values from the dataframe, and determines
			the total number of NaN values present. 
    Details:
        
	Param  : df, a dataframe containing all the relevant columns that relevant
			data passed through the function to be processed
            
            
    Note   : This method helps filter NaN values for effective data mining 
    Returns: true and false for the high number NaN columns that are dropped.
    """
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
		         """
    Author : Albert Ferguson
    Brief  : Imputes NaN data in columns that contain NaN data 
        
    Param  : df, a dataframe containing all the relevant columns that relevant
            data passed through the function to be processed.
            
            
    Note   : This method imputes columns that contain NaN data or data of 
		similar types
    Returns: true and false for helping the imputate process to determine 
		which NaN values in columns are to be imputed. 
				"""
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

#################################################################################

#################################################################################
# Runner code

def runPreChecks():
	# TODO: return as bool for eval checks
	
	global RAW_DF_LIST
	global RAWGLOBAL_DF_LIST
	
	i = 1
	for raw_df in RAW_DF_LIST:
		if DEBUG == True:
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
		"REGION", "geoId", "countryterritoryCode",
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

# run prechecks
runPreChecks()

if DEBUG == True:
	print("\t###\n")
	print("\tWRITING TO BINARY DUMP...")
	print("\t###\n")

# assert we actually completed the data prechecks correctly
k = os.system("cls")

for df in RAW_DF_LIST:
	print(df.head())

# write output to file dumps
with open(os.path.join(baseDir, "Table Checklist.txt"), 'w+') as hdf_checklist:
	hdf_checklist.write("WHO Indicator Data\n\n")

	for key in ATTRIBUTES:
		hdf_checklist.write(ATTRIBUTES[key] + ":\t\t" + key)
		hdf_checklist.write("\n")

	hdf_checklist.write("\nECDC Sars-Cov2 Data (AKA COVID19)\n\n")
	hdf_checklist.write("COVID19:\t\tCOVID-19-geographic-disbtribution-worldwide")


with open("processing_dump.txt", "wb") as fn:
	pickle.dump(RAW_DF_LIST, fn)
with open("globaldata_processing_dump.txt", "wb") as fn:
	pickle.dump(RAWGLOBAL_DF_LIST, fn)

#################################################################################
