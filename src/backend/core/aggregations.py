# Python CORE
import os
import pickle

# DATA MANIP: PANDAS AND NUMPY
import pandas as pd
import numpy as np

# SEABORN
import seaborn as sns

# MATPLOTLIB
import matplotlib.gridspec as gridspec
import matplotlib.pyplot as plt
# SKLEARN
from sklearn.preprocessing import (MinMaxScaler, StandardScaler)
from sklearn.impute import SimpleImputer

def splicer(df_list):
	# get max index size of df in list
	max_idx = 0
	for df in df_list:
		if max_idx < df.shape[0]:
			max_idx = df.shape[0]

	# compute the new df's col names and index size
	index = df_list[0].index
	columns = [df["schema"][0] for df in df_list]
	columns = columns[:-1]
	columns.append("cases")
	columns.append("deaths") 

	new_df = pd.DataFrame(index=index, columns=columns)
	
	for df in df_list:
		if df.schema[0] not in columns:
			continue
		try:
			schema = df.schema[0]
			new_df[schema] = pd.Series(df["Numeric"], index=new_df.index)
		except KeyError:
			pass
	
	# attach the covid data
	new_df["cases"] = df_list[-1]["cases"]
	new_df["deaths"] = df_list[-1]["deaths"]
	# drop any NaNs
	new_df.dropna()

	return new_df

def groupTimeCovid(data: pd.DataFrame, time='M'):
	"""
	========================================
	**  DEPRECIATED USE groupbyTimeFreq   **
	========================================
	Author : Albert Ferguson
	Brief  : Reindex for time by retyping. 
	Details:
		Retype and apply a PeriodIndex, selecting the M (monthly) opt. as a default.
		Use the groupby function of a dataframe and the column we want to groupby, return a sum

	Param  : data, a dataframe with the data to index by time.
	Param  : time, options are 'Y', 'M' and 'D'. Defined by pd.PeriodIndex.
			See: https://pandas.pydata.org/pandas-docs/stable/user_guide/timeseries.html
			See: https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.PeriodIndex.html
			
	Note   : This is a destructive method.
	Returns: the dataframe grouped by time, False if an error occurs.
	"""
	try:
		data.dateRep = pd.to_datetime(data.dateRep)
		data = data.groupby(pd.PeriodIndex(data.dateRep, freq = time), axis = 0).sum()
	except AttributeError:
		return False

	data["schema"] = "COVID19" # re add the schema
	data = data.reset_index()  # reset the index for following functions.

	return data

def groupbyTimeFreq(data: pd.DataFrame, time='M'):
    """
    Author : Albert Ferguson
    Brief  : Reindex for time by retyping. 
    Details:
        Retype and apply a PeriodIndex, selecting the M (monthly) opt. as a default.
        Use the groupby function of a dataframe and the column we want to groupby, return a sum

    Param  : data, a dataframe with the data to index by time.
    Param  : time, options are 'Y', 'M' and 'D'. Defined by pd.PeriodIndex.
            See: https://pandas.pydata.org/pandas-docs/stable/user_guide/timeseries.html
            See: https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.PeriodIndex.html
            
    Note   : This is a destructive method.
    Returns: the dataframe grouped by time, False if an error occurs.
    """
    # info on sorting
    # https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.sort_values.html
    # https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.asfreq.html
    
    data.dateRep = pd.to_datetime(data.dateRep)
    data.sort_values(by=["dateRep"], ascending=True, inplace=True)
    dateSeries = list(data.dateRep)
    data.reset_index(inplace=True)
    data.dateRep = dateSeries
    data.drop(["index"], axis=1, inplace=True)
    data.dateRep = pd.to_datetime(data.dateRep)
    return data

def groupbyCountry(df, summative=False, country=None):
	"""
	Author : Albert Ferguson
	Brief  : Group the given dataframe according to country. 
	Details:
		Use the groupby function of a dataframe and the column we want to
		groupby, return a sum

	Param: df, input dataframe to group.
	Param: summative, optional kwarg to return a single row per country with
		   sum of values per column. Drops any columns that can't be summed.
	Param: country, if set and summative False, filter for the selected country.

	Note   :
		This differs from df to df as schema may change and the field
		for countries is labelled differently.

	TODO: figure out non destructive method
	"""

	
	if summative and country is None:			
		_df = df.copy() # work with a copy, destructive method
		schema_str = _df.schema[0] # save the schema for re adding later.
		try:
			_df = _df.groupby(df.countriesAndTerritories, axis = 0).sum()
		except AttributeError:
			try:
				_df = _df.groupby(df.COUNTRY, axis = 0).sum()
			except AttributeError:
				pass
		_df = _df.reset_index()     # allow normal indexing for other functions.
		_df["schema"] = schema_str # re-add the schema constant.
		return _df
	
	elif country is not None:
		_df = df.copy()
		try:
			_df = _df[df.countriesAndTerritories.isin(list(country))]
		except AttributeError:
			try:
				_df = _df[df.COUNTRY.isin(list(country))]
			except AttributeError:
				return False
		return _df
	else:
		return False

def imputateMonthlyOther(df):
	try:
		# convert to PeriodIndexing
		schema = df.schema[0]

		# aggregate for monthly data
		df.set_index(pd.to_datetime(df.YEAR, format="%Y"),inplace=True)
		df = df.drop("YEAR",axis=1)

		# apply a resample, leaving 0's where we need to imputate
		df = pd.DataFrame(df["Numeric"].resample('M').sum())
		df["schema"] = schema

		constantImpNoData = SimpleImputer(missing_values=0, strategy="constant",
								fill_value=df["Numeric"].mean())

		df["Numeric"] = constantImpNoData.fit_transform(df[["Numeric"]])
	except KeyError:
		return df[:5]
	return df[:5].reset_index()
