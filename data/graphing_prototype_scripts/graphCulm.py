__doc__="""Note, this now works. Requires integration and fixup."""

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

# SKLEARN
from sklearn import preprocessing

def groupbyMonthlyCovid(df):
	"""
	Author: Albert Ferguson
	Reindex for time by retyping and applying a PeriodIndex selecting the M (mnonthly) opt.
	Use the groupby function of a dataframe and the column we want to groupby, return a sum
	"""

	# convert to PeriodIndexing
	try:
		df.dateRep = pd.to_datetime(df.dateRep)
		df = df.groupby(pd.PeriodIndex(df.dateRep, freq = "M"), axis = 0).sum()

	except AttributeError:
		df.index = pd.to_datetime(df.index)
		df = df.groupby(pd.PeriodIndex(df.index, freq = "M"), axis = 0).sum()


		# DOESN'T WORK
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

with open("data/processing_dump.txt", "rb") as f:
		df_list = pickle.load(f)

fig = plt.figure()
ax = plt.axes()

# df = groupbyCountry(df_list[-1]); 
# df = groupbyMonthlyCovid(df_list[-1])
# df = df_list[-1]
# ax.plot(df.dateRep, df.cases, 'yo-')
# plt.show(); plt.legend()
# input()

# df['Deaths_culm'] = df.groupby('month')['deaths'].head(1)
# df['Deaths_culm'].cumsum().ffill()

# ax.plot(df['month'], df['Deaths_culm'], 'yo-', label="Cumulative Frequencty - Cases, Deaths")

df = groupbyCountry(df_list[-1])
sd_sp   = df.cases.std(); mean_sp = df.cases.mean() # stat values for graphing the bell curve.
bins_int = 100
cases = df[df["countriesAndTerritories"].isin(["Afghanistan"])].cases
# group by country, otherwise we get a clusterfuck of graphing.

# normalise the data
# norm_scaler = preprocessing.StandardScaler()
# norm_ndarray = norm_scaler.fit_transform(df[["cases"]])

# current curve, use the bins value for our curve approx. later.
n, bins, patches = ax.hist(cases, bins=bins_int, density=True, histtype="step",
						   cumulative=True, label="Emperical - confirmed cases")

# flattened curve approx. to calculate the bell curve of our pandemic
y = (( 1 / (np.sqrt(2 * np.pi) * sd_sp)) *
	 np.exp( -0.5 * ( 1 / sd_sp * (bins - mean_sp))**2))
y = y.cumsum(); y /= y[-1] # convert to cumulative sum then calc average at all points (last val in cumulative is total)

ax.plot(bins, y, 'k--', linewidth=1.5, label="Project Exp. Curve")

plt.xticks(rotation=30)
ax.legend(loc="right"); plt.show()




