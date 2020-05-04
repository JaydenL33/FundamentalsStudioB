fn = "D:\Fund_studio_B\development\Raw_data\processing_dump.txt"
import matplotlib as plt
import matplotlib.pyplot as plt
import pandas as pds
import pandas as pd
import pandas
import pickle
import numpy as np
import seaborn as sn


def main():
	with open(fn, "rb") as f:
		df_list = pickle.load(f)
		df = df_list[11]

	df.head(10000)
	df.describe()
	corr_plot(df)

def corr_plot(df):
	df.corr(method ='kendall') 
	corrMatrix = df.drop(columns=["dateRep","geoId", "countryterritoryCode"], axis=1).corr()
	sn.heatmap(corrMatrix, annot=True)
	df.head(10000)
	plt.show()


if __name__ == '__main__': main()
