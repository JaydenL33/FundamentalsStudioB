fn = "D:\Fund_studio_B\development\Raw_data\processing_dump.txt"
import matplotlib as plt
import matplotlib.pyplot as plt
import pandas as pds
import pandas as pd
import pickle
import numpy as np

def main():
	with open(fn, "rb") as f:
		df_list = pickle.load(f)
		df = df_list[11]
	df.head(10000)
	df.loc[['cases','deaths']]
	cases_deaths(df)


def cases_deaths(df):
	
	corr = df.corr() 
	corr.style.background_gradient(cmap='coolwarm')
	plt.show()

if __name__ == '__main__': main()

