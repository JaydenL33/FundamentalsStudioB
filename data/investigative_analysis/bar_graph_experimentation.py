fn = "D:\Fund_studio_B\development\Raw_data\processing_dump.txt"
import matplotlib as plt
import matplotlib.pyplot as plt
import matplotlib.ticker as mtick
import pandas as pds
import pandas as pd
import pickle

with open(fn, "rb") as f:
	df_list = pickle.load(f)
	df = df_list[11]

df.head()
df.describe()
bar_graph(df)
stacked_bar(df)

def bar_graph(df):
df.groupby('geoId')['cases'].plot(kind = 'bar')
plt.show()

def stacked_bar(df):
bins = [1,3,5,7,9,11]
mths_bins = pd.cut(df['month'], bins)
df.groupby(['month','cases']).size().unstack().plot(kind='bar',stacked=True)

plt.show()
