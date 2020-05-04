fn = "D:\Fund_studio_B\development\Raw_data\processing_dump.txt"
import matplotlib as plt
import matplotlib.pyplot as plt
import matplotlib.ticker as mtick
import pandas as pds
import pandas as pd
import pickle

def main():
	with open(fn, "rb") as f:
		df_list = pickle.load(f)
		df = df_list[11]

	df.head()
	df.describe()
	month_cases(df)
	month_deaths(df)
	geoId_cases(df)

def month_cases(df):
	df.groupby(['month','cases']).size().unstack().plot(kind='bar',stacked=True)
	plt.show()

def month_deaths(df):
	df.groupby(['month','deaths']).size().unstack().plot(kind='bar',stacked=True)
	plt.show()

def geoId_cases(df):
	df.groupby(['geoId','cases']).size().unstack().plot(kind='bar',stacked=True)
	plt.show()






if __name__ == '__main__': main()