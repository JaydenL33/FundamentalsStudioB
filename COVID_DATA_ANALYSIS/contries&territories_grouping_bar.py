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
	df.head(10000)
	cT_cases(df)
	cT_deaths(df)
	geoId_cases(df)



def cT_cases(df):
	df.groupby('countriesAndTerritories')['cases'].plot(kind='bar')
	plt.show()
	
def cT_deaths(df):
	df.groupby('countriesAndTerritories')['deaths'].plot(kind='bar')
	plt.show()
	

def geoId_cases(df):
	df.groupby('geoId')['cases'].plot(kind='bar')
	plt.show()
	
if __name__ == '__main__': main()
