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
	reindex(df_list)
	groupby(df9_reidx)
	plot(df9_reidx_grp)

def reindex(df_list):
	df9_reidx = df_list[9].reindex(columns=['COUNTRY', 'Numeric'])
def groupby(df9_reidx):
	df9_reidx_grp = df9_reidx.groupby('COUNTRY')
	df9_reidx_grp.first()

def plot(df9_reidx_grp):
	df.plot(kind='bar',x='COUNTRY',y='Numeric',color='red')
	plt.show()

if __name__ == '__main__':
	main()