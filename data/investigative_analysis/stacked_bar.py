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
	stacked_cases(df)
	stacked_deaths(df)

	



def stacked_cases(df):
	
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

	plt.legend(reversed_handles,correct_labels)

	plt.gca().yaxis.set_major_formatter(mtick.PercentFormatter())
	plt.show()


def stacked_deaths(df):
	
	df.assign(dummy = 1).groupby(
	  ['dummy','deaths']
	).size().groupby(level=0).apply(
	    lambda x: 100 * x / x.sum()
	).to_frame().unstack().plot(kind='bar',stacked=True,legend=False)

	# or it'll show up as 'dummy' 
	plt.xlabel('deaths')

	# disable ticks in the x axis
	plt.xticks([])

	# fix the legend or it'll include the dummy variable
	current_handles, _ = plt.gca().get_legend_handles_labels()
	reversed_handles = reversed(current_handles)
	correct_labels = reversed(df['deaths'].unique())

	plt.legend(reversed_handles,correct_labels)

	plt.gca().yaxis.set_major_formatter(mtick.PercentFormatter())
	plt.show()

if __name__ == '__main__': main()