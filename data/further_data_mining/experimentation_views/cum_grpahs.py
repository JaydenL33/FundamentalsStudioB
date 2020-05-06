import matplotlib.pyplot as plt
import pandas as pd
import pickle
import numpy as np
import seaborn as sn
import os



with open(os.path.join(os.pardir, "processing_dump.txt"), "rb") as f:
		df_list = pickle.load(f)

#def deaths(df):
df = df_list[11]
df['Deaths_cum'] = df.groupby('month')['deaths'].head(1)
df['Deaths_cum'].cumsum().ffill()
df.plot(x='month', y='Deaths_cum', kind='line', 
     	figsize=(10, 8), legend=False, style='yo-', label="Cumulative frequency graph deaths")
plt.legend();
plt.show()

#def cases(df):
df = df_list[11]
df['cases_cum'] = df.groupby('cases')['dateRep'].head(1)
df['cases_cum'].cumsum()
# df['cumcase_perc'] = 100*df['cases']/df['cases_cum'].sum()
df.plot(x='cases_cum', y='cases', kind='line', 
        figsize=(10, 8), legend=False, style='yo-', label="Cumulative frequency graph cases")
#plt.axhline(y=count_students_at_class_start, color='green', linestyle='--', label='count students at initial start')
#plt.title("Running Total of Students Who Graduated in $X$ Years\nFrom Same Start Class", y=1.01, fontsize=20)
# plt.ylabel("running total of students graduated", labelpad=15)
# plt.xlabel("years after starting college", labelpad=15)
plt.legend();
plt.show()

#def deaths(df):
df = df_list[11]
df['cases_death_cum'] = df.groupby('deaths')['cases'].head(1)
df['cases_death_cum'].cumsum()
df.plot(x='deaths', y='cases_death_cum', kind='line', 
     	figsize=(10, 8), legend=False, style='yo-', label="Cumulative frequency graph cases_deaths")
plt.legend();
plt.show()
# mu = 200
# sigma = 25
# n_bins = 50
# x = df[['Deaths_cum']]( size=100)





