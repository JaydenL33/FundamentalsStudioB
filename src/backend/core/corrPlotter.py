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


def corr_plot(df, ax, labels=True):
	"""Attaches the plot to the given axis."""
	sns.heatmap(df.corr(method ='kendall') , annot=True, ax=ax, xticklabels=labels)