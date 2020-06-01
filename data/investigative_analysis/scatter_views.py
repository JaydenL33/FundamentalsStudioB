fn = "D:\Fund_studio_B\development\Raw_data\processing_dump.txt"
import matplotlib as plt
import matplotlib.pyplot as plt
import pandas as pds
import pandas as pd
import pickle
import os

def main():
	with open(fn, "rb") as f:
		df_list = pickle.load(f)
		df = df_list[11]

	df.head(10000)
	df.describe()
	deaths_cases(df)
	day_cases(df)
	day_deaths(df)


def deaths_cases(df):
	df.plot(kind='scatter',x='deaths',y='cases',color='red')
	plt.show()

def day_cases(df):
	
	df.plot(kind='scatter',x='day',y='cases',color='red')
	plt.show()

def day_deaths(df):
	df.plot(kind='scatter',x='day',y='deaths',color='blue')
	plt.show()

if __name__ == '__main__': main()