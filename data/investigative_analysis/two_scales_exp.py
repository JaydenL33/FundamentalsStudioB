fn = "D:\Fund_studio_B\development\Raw_data\processing_dump.txt"
import matplotlib as plt
import matplotlib.pyplot as plt
import pandas as pds
import pandas as pd
import pickle

with open(fn, "rb") as f:
	df_list = pickle.load(f)
	df = df_list[11]

df.head()
df.describe()
fig, ax1 = plt.subplots()

color = 'tab:red'
df.plot(ax1.set_xlabel('month')
ax1.set_ylabel('cases', color=color)
ax1.plot(month, cases, color=color)
ax1.tick_params(axis='y', labelcolor=color)

ax2 = ax1.twinx()  # instantiate a second axes that shares the same x-axis

color = 'tab:blue'
ax2.set_ylabel('Country_code', color=color)  # we already handled the x-label with ax1
ax2.plot(month,countriesAndTerritories , color=color)
ax2.tick_params(axis='y', labelcolor=color)

fig.tight_layout()  # otherwise the right y-label is slightly clipped
plt.show()



