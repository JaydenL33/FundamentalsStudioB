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
	deaths_hist(df)
	cases_hist(df)
	date_hist(df)

def deaths_hist(df):
	df[['deaths']].plot(kind='hist',bins=[400,800,1200,1600,2000],rwidth=0.8)
	plt.show()

def cases_hist(df):
	df[['cases']].plot(kind ='hist',bins=[6000,12000,18000,24000,30000,36000],rwidth=0.8)
	plt.show()

def date_hist(df):
	df['dateRep'] = pd.to_datetime(df['dateRep'], infer_datetime_format=True)
	plt.clf()
	df['dateRep'].map(lambda d: d.day).plot(kind='hist')
	plt.show()


if __name__ == '__main__': main()