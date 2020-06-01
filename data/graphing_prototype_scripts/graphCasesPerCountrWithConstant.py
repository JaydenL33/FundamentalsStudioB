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

def barPlotComp(x, y, ax, constantComp, labels):
	"""Note: generates a bar plot using countries and territories.
	Uses constant comp to compare to a constant value on y-axis."""

	# note the len conversion for y in ax.plot, matching dimensions
	ax.bar(x, y, color='red', label=labels) # plot the y data
	ax.plot(x, [constantComp]*len(x), label="Medical constant") # plot a constant across the chart
	# this is just generating a green bar of value 1000. 
	# https://matplotlib.org/3.2.1/api/_as_gen/matplotlib.pyplot.axhline.html
	# effect if used on top of df.plot as kind="bar" is a bar of h=1000 at every point...
	# plt.axhline(y= 1000, color='green', linestyle='--', label='(to be medical cap) test')
	ax.legend(["Some constant", "Cases per Country"])
	
with open("processing_dump.txt", "rb") as f:
		df_list = pickle.load(f)

fig = plt.figure()
ax = plt.axes()

# perform a grouping, avoids 10 instances of each country (time measurment replication)
df = groupbyCountry(df_list[-1])
someVal = 10000

# this essentialy compares every country to a constant value, with the independent axis showing number of cases
barPlotComp(df.countriesAndTerritories, df.cases, ax, someVal, df.countriesAndTerritories)
plt.xticks(rotation=90)
plt.show()