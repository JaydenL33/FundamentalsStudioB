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

	df6 = df_list[6]
	
	df6_reidx = df6.reindex(columns=['COUNTRY', 'Numeric'])

	df6_reidx.index
	df6_reidx_grp = df6_reidx.groupby('COUNTRY').Numeric.mean()
	#df6_reidx_grp.first(offset)
	
	df6_reidx_grp.plot(kind='bar',x='COUNTRY',y='Numeric',color='red')
	plt.show()


main()