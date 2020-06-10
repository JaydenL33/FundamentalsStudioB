fn = "D:\Fund_studio_B\development\Raw_data\processing_dump.txt"
import matplotlib as plt
import matplotlib.pyplot as plt
import pandas as pds
import pandas as pd
import pickle

with open(fn, "rb") as f:
	df_list = pickle.load(f)
	df = df_list[11]

df.head(10000)
df.describe()
df[['cases']].plot(kind='hist',bins=[0,12500,25000,37500,50000 ],rwidth=0.8)
plt.show()