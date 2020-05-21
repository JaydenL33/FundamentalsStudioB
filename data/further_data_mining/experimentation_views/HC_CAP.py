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
		df = df.groupby(df.countriesterritoriesCode, axis = 0).sum()
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

# idea, get a constant per country, pair it with the country and show cases/deaths
# filter the data by country indexing (use countryterritoryCode as it's the common dimension we want to match).
covidDataTotal = groupbyCountry(df_list[-1]) # returns a total for every country.
covidData      = df_list[-1]                 # a series of country is contained in this frame.
healthCapConst = groupbyCountry(df_list[6])  # returns a list of constants.

# create a plot of cases/deaths per country vs equiv numeric val in healthCap
# i.e. index both by country (done) then match the indexes (countriesAndTerritories and COUNTRY)
# note the len conversion for values in ax.plot, matching dimensions
def barPlotComp(category, values, ax, constantComp, country):
	"""Note: generates a bar plot using countries and territories.
	Uses constant comp to compare to a constant value on y-axis."""

	ax.bar(category, values, color="red", label=("Cases per date in: " + country)) # plot the values
	ax.plot(category, [constantComp]*len(category), label="Doctors Per 100K Pop.", color="green") # plot a constant across the chart
	ax.legend()

# filter a df for one country with isin (pd.Series) and boolean indexing.
countries_list = covidData.countryterritoryCode.unique()
fig = plt.figure(); 
for i in range(len(countries_list)):
	ax = plt.axes()
	
	covidCountry = covidData[covidData.countryterritoryCode.isin([countries_list[i]])]
	drs100_series = healthCapConst[healthCapConst.COUNTRY.isin([countries_list[i]])].Numeric
	country_series = covidCountry.countriesAndTerritories
	# note: series returns the original df index, no reindex occurs. Use keys accesor to correctly index
	country_str = country_series[country_series.keys()[0]]
	
	try:
		drs100_num  = drs100_series[drs100_series.keys()[0]]
	except IndexError:
		drs100_num = 0
	
	barPlotComp(covidCountry.dateRep, covidCountry.cases, ax, drs100_num, country_str)
	plt.xticks(rotation=30);
	plt.savefig(str(i)+".png")