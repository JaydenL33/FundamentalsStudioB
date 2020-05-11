import matplotlib.pyplot as plt
import pandas as pd
import pickle
import numpy as np
import seaborn as sn
import os

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

with open(os.path.join(os.pardir, "processing_dump.txt"), "rb") as f:

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
		columns.remove("FINPROTECTION_CATA_TOT_10_POP")
		columns.remove("FINPROTECTION_CATA_TOT_25_POP")
		columns.remove("BP_06")
		columns.remove("GHED_CHEGDP_SHA2011")
		columns.remove("GHED_CHE_pc_PPP_SHA2011")
		columns.remove("IHRSPAR_CAPACITY03")
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

with open(os.path.join(os.pardir, "processing_dump.txt"), "rb") as f:
		df_list = pickle.load(f)

def plot(df):
	df.plot(x='dateRep', y='Months', kind='line', 
	        figsize=(10, 8), legend=False, style='yo-')
	plt.axhline(y='Numeric', color='green', linestyle='--', label='Capacity of healthcare system')
	plt.title("Capacity of a given healthcare system against number of COVID19 cases", y=1.01, fontsize=20)
	plt.ylabel("cases", labelpad=15)
	plt.xlabel("Months of COVID19 cases", labelpad=15)
	plt.legend();	
	plt.show() 


df = df_list[11]
df = groupbyCountry(df)
df = groupbyMonthlyCovid(df)

	
working_df = splicer()
working_df.dropna()
plot(working_df)