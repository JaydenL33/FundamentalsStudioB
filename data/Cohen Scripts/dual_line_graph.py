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
	df.head(1000)
	df.describe()
	cases_deaths(df)
	geoId(df)


def cases_deaths(df):
	df.assign(dummy = 1).groupby(
	  ['dummy','cases']
	).size().groupby(level=0).apply(
	    lambda x: 100 * x / x.sum()
	).to_frame().unstack().plot(kind='bar',stacked=True,legend=False)

	# or it'll show up as 'dummy' 
	plt.xlabel('cases')

	# disable ticks in the x axis
	plt.xticks([])

	# fix the legend or it'll include the dummy variable
	current_handles, _ = plt.gca().get_legend_handles_labels()
	reversed_handles = reversed(current_handles)
	correct_labels = reversed(df['cases'].unique())
	ax = plt.gca()
	df.plot(kind='line',x='month',y='deaths',ax=ax)
	df.plot(kind='line',x='month',y='cases', color='red', ax=ax)
	plt.show()


def geoId(df):
	
	ax = plt.gca()
	df.plot(kind='line',x='day',y='cases',ax=ax)
	df.plot(kind='line',x='day',y='deaths', color='red', ax=ax)
	plt.show()
	

if __name__ == '__main__': main()
