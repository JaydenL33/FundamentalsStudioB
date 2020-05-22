import matplotlib.pyplot as plt
import pandas as pd
import pickle
import numpy as np
import seaborn as sn
import os

from sklearn.preprocessing import (MinMaxScaler, StandardScaler)
from sklearn.impute import SimpleImputer

fn = os.path.join(os.pardir, "processing_dump.txt")

def splicer():
	# get max index size of df in list
	max_idx = 0
	for df in df_list:
		if max_idx < df.shape[0]:
			max_idx = df.shape[0]

	# compute the new df's col names and index size
	index = df_list[0].index
	columns = [df.schema[0] for df in df_list]
	columns = columns[:-1]
	columns.remove("SA_0000001807")
	columns.remove("NCD_CCS_rheumreg")
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
	cov_df = df_list[-1]
	new_df["cases"] = cov_df["cases"]
	new_df["deaths"] = cov_df["deaths"]
	return new_df

def groupbyMonthlyCovid(df):
	# convert to PeriodIndexing
	df.dateRep = pd.to_datetime(df.dateRep)
	# aggregate for monthly data
	df = df.groupby(pd.PeriodIndex(df.dateRep, freq = "M"), axis = 0).sum()
	# re add the schema
	df["schema"] = "COVID19"
	print(df.shape)
	return df.reset_index()

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

def corr_plot(df):
	df.corr(method ='kendall') 
	corrMatrix = df.head(1000).corr()
	sn.heatmap(corrMatrix, annot=True)
	plt.savefig("corrMatrix.png")

with open(fn, "rb") as f:
	df_list = pickle.load(f)

df_list[-1] = groupbyMonthlyCovid(df_list[-1])

for i in range(len(df_list) - 1):
	df_list[i] = imputateMonthlyOther(df_list[i])


working_df = splicer()
working_df.dropna()
corr_plot(working_df)