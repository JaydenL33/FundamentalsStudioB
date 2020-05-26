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

def main():
	with open(os.path.join(os.pardir, "processing_dump.txt"), "rb") as f:
		df_list = pickle.load(f)
	df = df_list

def sel(df6):
	newdf6 = df6.loc[:,['COUNTRY', 'Numeric']]
	print(newdf6)

def sel2(df11):
	newdf11 = df11.loc[:,['countriesAndTerritories', 'cases']]
	print(newdf11)


	
with open(os.path.join(os.pardir, "processing_dump.txt"), "rb") as f:
		df_list = pickle.load(f)
		df = df_list

df6 = df_list[6]
df11 = df_list[11]

sel(df6)
sel2(df11)

#def merge(df_list):
	# merged = pd.merge(df_list[9],df_list[11],left_on='Numeric',right_on='cases', how='left')
	# print(merged)


