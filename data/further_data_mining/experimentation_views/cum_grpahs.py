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



with open(os.path.join(os.pardir, "processing_dump.txt"), "rb") as f:
		df_list = pickle.load(f)


fig = plt.figure()
ax = plt.axes()

#def deaths(df):
df = df_list[11]
df = groupbyCountry(df)

df = groupbyMonthlyCovid(df)

print(df.columns)
print(df.head())
print(df.countriesAndTerritories)
print(df.cases)
input()

#df['Deaths_cum'] = df.groupby('month')['deaths'].head(1)
# df['Deaths_cum'].cumsum().ffill()

# df.plot(x='month', y='Deaths_cum', kind='line', 
#      	figsize=(10, 8), legend=False, style='yo-', label="Cumulative frequency graph deaths")
# plt.legend();
# plt.show()

#def cases(df):
# df = df_list[11]
# df['cases_cum'] = df.groupby('cases')['dateRep'].head(1)
# df['cases_cum'].cumsum()
# df['cumcase_perc'] = 100*df['cases']/df['cases_cum'].sum()

####
# Index is now the date time values!!!
###
ax.plot(df.index, df['cases'], 'bo-')
ax.plot(df.index, df['deaths'], 'ro-')

#plt.axhline(y=count_students_at_class_start, color='green', linestyle='--', label='count students at initial start')
#plt.title("Running Total of Students Who Graduated in $X$ Years\nFrom Same Start Class", y=1.01, fontsize=20)
# plt.ylabel("running total of students graduated", labelpad=15)
# plt.xlabel("years after starting college", labelpad=15)
# fig.legend();
plt.show()

# #def deaths(df):
# df = df_list[11]
# df['cases_death_cum'] = df.groupby('deaths')['cases'].head(1)
# df['cases_death_cum'].cumsum()
# df.plot(x='deaths', y='cases_death_cum', kind='line', 
#      	figsize=(10, 8), legend=False, style='yo-', label="Cumulative frequency graph cases_deaths")
# plt.legend();
# plt.show()
# # mu = 200
# sigma = 25
# n_bins = 50
# x = df[['Deaths_cum']]( size=100)





