fn = "D:\Fund_studio_B\development\Raw_data\processing_dump.txt"
import matplotlib as plt
import matplotlib.pyplot as plt
import pandas as pds
import pandas as pd
import pickle

with open(fn, "rb") as f:
	df_list = pickle.load(f)
	df = df_list[11]

df.head(1000)
df.describe()
df.groupby('deaths')['cases'].plot(kind='bar')
plt.show()
plt.savefig()