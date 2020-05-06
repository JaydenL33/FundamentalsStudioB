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

def groupbyMonthlyCovid(df):
	"""
	Author: Albert Ferguson
	Reindex for time by retyping and applying a PeriodIndex selecting the M (mnonthly) opt.
	Use the groupby function of a dataframe and the column we want to groupby, return a sum
	"""

	# convert to PeriodIndexing
	df.dateRep = pd.to_datetime(df.dateRep)
	# aggregate for monthly data
	df = df.groupby(pd.PeriodIndex(df.dateRep, freq = "M"), axis = 0).sum()
	# re add the schema
	df["schema"] = "COVID19"
	return df.reset_index()

def groupbyCountry(df):
	"""
	Author: Albert Ferguson
	Use the groupby function of a dataframe and the column we want to groupby, return a sum
	Note: this differs from df to df as schema may change and the field for countries is labelled
		differently.
	"""

	# aggregate for countriesAndTerritories data

	# save the schema for re adding later..TODO: figure out non destructive method
	schema_str = df.schema[0]

	try:
		df = df.groupby(df.countriesAndTerritories, axis = 0).sum()
		df = df.reset_index()

	except AttributeError:
		try:
			df = df.groupby(df.COUNTRY, axis = 0).sum()
			df = df.reset_index()

		except AttributeError:
			pass

	# re add the schema
	df["schema"] = schema_str
	return df

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
