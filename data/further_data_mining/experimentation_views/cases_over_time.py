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


# def sel(df11):
# 	newdf11 = df11.loc[:,['countriesAndTerritories', 'cases']]
# 	print(newdf11)
# # def sel_att(newdf11):
# # 	df3.groupby(['X']).get_group('A')

def groupbyCountry(newdf11):
	"""
	Author: Albert Ferguson
	Use the groupby function of a dataframe and the column we want to groupby, return a sum
	Note: this differs from df to df as schema may change and the field for countries is labelled
		differently.
	"""

	# aggregate for countriesAndTerritories data

	# save the schema for re adding later..TODO: figure out non destructive method
	#schema_str = newdf11.schema[0]

	#try:
	newdf11 = newdf11.groupby(newdf11.countriesAndTerritories, axis = 0).get_group('Afghanistan')
	newdf11 = newdf11.reset_index()

	# except AttributeError:
	# 	try:
	# 		df = df.groupby(df.COUNTRY, axis = 0).sum()
	# 		df = df.reset_index()

	# 	except AttributeError:
	# 		pass

	# re add the schema
	# newdf11.schema = schema_str
	return newdf11

def lp(newdf11):
	newdf11.plot(kind='line',x='countriesAndTerritories',y='cases',color='red')
	plt.show()



with open(os.path.join(os.pardir, "processing_dump.txt"), "rb") as f:
		df_list = pickle.load(f)
		df = df_list

df11 = df_list[11]
newdf11 = df11.loc[:,['countriesAndTerritories', 'cases']]
#sel(df11)
newdf11 = groupbyCountry(newdf11)
lp(newdf11)