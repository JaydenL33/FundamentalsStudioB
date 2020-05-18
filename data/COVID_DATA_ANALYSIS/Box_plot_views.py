fn = "D:\Fund_studio_B\development\Raw_data\processing_dump.txt"
import matplotlib as plt
import matplotlib.pyplot as plt
import pandas as pds
import pandas as pd
import pickle

def main():
	with open(fn, "rb") as f:
		df_list = pickle.load(f)
		df = df_list[11]

	df.head(10000)
	df.describe()
	cases_day(df)
	deaths_day(df)
	cases_months(df)
	geoid_cases(df)


def cases_day(df):
	df.boxplot(by ='day', column =['cases'], figsize=[20,10], grid = False) 
	plt.show()

def deaths_day(df):
	df.boxplot(by ='day', column =['deaths'], figsize=[20,10], grid = False) 
	plt.show()

def cases_months(df):
	df.boxplot(by ='month', column =['cases'], figsize=[20,10], grid = False) 
	plt.show()

def geoid_cases(df):
	df.boxplot(by ='geoId', column =['cases'], figsize=[20,10], grid = False) 
	plt.show()



if __name__ == '__main__': main()
