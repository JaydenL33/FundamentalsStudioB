fn = "D:\Fund_studio_B\development\Raw_data\processing_dump.txt"
import matplotlib as plt
import matplotlib.pyplot as plt
import pandas as pds
import pandas as pd
import pickle

with open(fn, "rb") as f:
	df_list = pickle.load(f)
	df = df_list[11]

df.head(9868)
df.describe()
df.plot(kind = "scatter", x = "day", y = "deaths", color = 'green', marker='o', linestyle= 'dashed')
plt.show()
plt.savefig()