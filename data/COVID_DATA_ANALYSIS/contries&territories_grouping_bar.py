
import matplotlib as plt
import matplotlib.pyplot as plt
import matplotlib.ticker as mtick
import pandas as pd
import pickle
import os

fn = os.path.join(os.pardir, "processing_dump.txt")



def cT_cases(df):
	df.groupby('countriesAndTerritories')['cases'].plot(kind='bar')
	plt.show()
	
def cT_deaths(df):
	df.groupby('countriesAndTerritories')['deaths'].plot(kind='bar')
	plt.show()
	

def geoId_cases(df):
	df.groupby('geoId')['cases'].plot(kind='bar')
	plt.show()
	

