# Python CORE
import os
import pickle

# DATA MANIP: PANDAS AND NUMPY
import pandas as pd
import numpy as np

# SEABORN
import seaborn as sns

# MATPLOTLIB
import matplotlib.gridspec as gridspec
import matplotlib.pyplot as plt
# SKLEARN
from sklearn.preprocessing import (MinMaxScaler, StandardScaler)
from sklearn.impute import SimpleImputer


def plot(feature: pd.Series, ax, colour: str, label:str):
	"""
	Author: Albert Ferguson
	Fit and plot a univariate or bivariate kernel density estimate.
	See: https://seaborn.pydata.org/generated/seaborn.kdeplot.html
	Takes the df series to plot with type: pd.Series and the axis to attach to.

	Note: colour is a string value, e.g. 'r', 'b', 'g'.
	Note: cuts the data to range of data by default.
	"""

	# call the plt plot type function on each axis
	sns.distplot(feature, kde_kws={"cut":0, "shade":True, "bw":0.2, "color":colour}, ax=ax)
	# set some labels
	ax.set_ylabel('Fitted Probability Density')
	ax.set_xlabel(label)
	
	return