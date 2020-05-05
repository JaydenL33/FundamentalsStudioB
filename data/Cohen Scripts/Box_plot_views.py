import matplotlib.pyplot as plt
import pandas as pd
import pickle

import os
import seaborn as sns

fn = os.path.join(os.pardir, "processing_dump.txt")

with open(fn, "rb") as f:
	df_list = pickle.load(f)
	df = df_list[11]

plt.boxplot(df['cases']) 
plt.show()
# ax1.boxplot(df['deaths']) 