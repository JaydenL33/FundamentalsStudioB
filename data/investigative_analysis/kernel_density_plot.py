import matplotlib.pyplot as plt
import pandas as pd
import pickle
import numpy as np
import os
import seaborn as sns

fn = os.path.join(os.pardir, "processing_dump.txt")

with open(fn, "rb") as f:
	df_list = pickle.load(f)
	df = df_list[11]
_min = -100
_max = 100
fig = sns.kdeplot(df["cases"],  clip=(_min, _max), shade=True)
fig = sns.kdeplot(df["deaths"], clip=(_min, _max), shade=True)

plt.show()
