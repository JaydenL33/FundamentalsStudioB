# core user lib
from .core import environConfig, aggregations
from .core.grapher import corrPlotter
from .core.grapher import plot as kdePlotter

# Python core
import os
import pickle

# third party libs
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.gridspec as gridspec
import matplotlib.pyplot as plt
from sklearn.preprocessing import (MinMaxScaler, StandardScaler)
from sklearn.impute import SimpleImputer

# number charts we will plot
charts_int = 5

# df list to store our RAW
df_list = []

# defaults in case env var fails
# debug var, disables saving graphs and displays to monitor directly
# file name for Raw Data
DEBUG = False
baseDir = os.path.join(os.path.join(os.pardir, os.pardir), "data")

# global for the figure sizing
FIGSIZE = (20, 10)

################################################################################
# Utilities
################################################################################

def _runStartup():
	"""
	Author: Albert Ferguson
	Explicit startup function. Runs any necessary preloads for data and Globals updates.
	"""
	env = environConfig.safe_environ()

	global df_list
	global DEBUG
	global baseDir

	# update with the env config
	DEBUG = DEBUG   = env.bool("DEBUG", False)
	baseDir = env("BASE_DATA_DIR")

	# call the read binary to read-in the data frames RAW
	try:
		with open(os.path.join(baseDir, "processing_dump.txt"), "rb") as f:
			df_list = pickle.load(f)

	except FileNotFoundError:
		return False

	return True

################################################################################
# Plots and scaling
################################################################################

# TODO: add scaling
def scaler():
	pass

def makeAllThePlots():
	"""Author: Albert Ferguson
Helper function, implements our various plots onto a grid.
Call the other functions in this file to make the CorrMatrix.
Note: naming convention is camel case with explicit variable typing.
	e.g. myVar_int
	e.g. myData_df
	e.g. mySeries_list or mySeries_Series
	"""

	# explicit note for Python to call the global def
	global charts_int
	global df_list

	############################################################################
	# 1. 
	# Setup the grids for holding our plots, attach them to the same figure
	############################################################################

	fig = plt.figure(figsize=FIGSIZE)

	# the outer grid object, this holds two inner grids that we assign plots to
	# inner is for use with plotting, outer is purely spacing
	outer_grid = gridspec.GridSpec(2, 1, wspace=0.2, hspace=0.2)
	
	innerTop_grid = gridspec.GridSpecFromSubplotSpec(
		1, charts_int, 
		subplot_spec=outer_grid[0],
		wspace=0.1, hspace=0.1
		)
	
	innerBottom_grid = gridspec.GridSpecFromSubplotSpec(
		1, charts_int, 
		subplot_spec=outer_grid[1],
		wspace=0.1, hspace=0.1
		)

	############################################################################
	# 2. 
	# Call the plot for distPlots and add them to a subplot.
	# d+Dynamically create this for our raw non-covid data.
	############################################################################

	i = 0
	for df in df_list:
		
		# check to align on top or bottom of grid
		if i < 5:
			ax = plt.Subplot(fig, innerTop_grid[i])
		elif i > 4 and i < 10:
			ax = plt.Subplot(fig, innerBottom_grid[i-5])
		else:
			break

		# grab the label for x axis from the frame
		label_str = df.schema[0]

		# this is fucky check but it works, it'll break if it misses twice tho
		# an we'll get a gap in the figure
		try:
			kdePlotter.plot(df_list[i]["Numeric"], ax, 'g', label_str)
			fig.add_subplot(ax)
			i += 1

		except KeyError:
			try:
				kdePlotter.plot(df_list[i+1]["Numeric"], ax, 'g', label_str)
				fig.add_subplot(ax)
				i += 1
			except KeyError:
				pass

	plt.suptitle("Overview Graphs: distPlots for WHO indicators")
	
	if not DEBUG:
		plt.savefig(os.path.join(os.path.join(os.path.join(baseDir, "plots_pngs"), "distplots WHO Indicators RAW SCALED.png")))

	############################################################################
	# 3. 
	# Repeat above, but manually for the COVID data specifically.
	############################################################################

	# call a new figure for a new series of plots
	fig = plt.figure(figsize=FIGSIZE)

	# number of covid charts to make
	covidCharts_int = 2
	# the outer grid object, this holds one inner grid that we assign plots to
	# inner grid is for use with plotting
	outer_grid = gridspec.GridSpec(1, 1, wspace=0.2, hspace=0.2)
	
	inner_grid = gridspec.GridSpecFromSubplotSpec(
		1, covidCharts_int, 
		subplot_spec=outer_grid[0],
		wspace=0.1, hspace=0.1
		)

	# now create the subplots for each chart, ie make n new axis
	cases_ax  = plt.Subplot(fig, inner_grid[0])
	deaths_ax = plt.Subplot(fig, inner_grid[1])
	
	# call the plt plot type function on each axis
	sns.kdeplot(df_list[-1]["cases"], color='r', legend=True, ax=cases_ax)

	sns.kdeplot(df_list[-1]["deaths"], legend=True, ax=deaths_ax)

	# set some labels
	cases_ax.set_ylabel('Fitted Probability Density')
	deaths_ax.set_ylabel('Fitted Probability Density')
	cases_ax.set_xlabel("Cases")
	deaths_ax.set_xlabel("Deaths")

	#seaborn equiv. of set_xticks matplotlib
	#obviously, there are no negative deaths or cases. We may normalise later though
	cases_ax.set(xlim=(0,750))
	deaths_ax.set(xlim=(0,250))

	fig.add_subplot(cases_ax)
	fig.add_subplot(deaths_ax)

	plt.suptitle("Overview Graphs: KDE plots for Sars-Cov2")
	
	if not DEBUG:
		plt.savefig(os.path.join(os.path.join(os.path.join(baseDir, "plots_pngs"), "distplots Sars-Cov2 RAW SCALED.png")))

	############################################################################
	# 4. 
	# Setup and call a new figure for Covariance matricies.
	# These are aggregated comparisons across time and country.
	############################################################################

	# call a new figure for a new series of plots, default the frame to off
	fig = plt.figure(frameon=False, figsize=FIGSIZE)

	# number of cov matricies charts to make
	covMatsCharts_int = 2
	# the outer grid object, this holds one inner grid that we assign plots to
	# inner grid is for use with plotting
	# Note: this outer grid has an extra space for the c_bar generated by the corr_plots
	outer_grid = gridspec.GridSpec(covMatsCharts_int, 3, wspace=0.2, hspace=0.1)

	# now create the subplots for each chart, ie make n new axis
	covMatTime_ax    = plt.Subplot(fig, outer_grid[0, :])
	covMatCountry_ax = plt.Subplot(fig, outer_grid[1, :])

	# get current axis from plt instance retrieves the main axis, set them invisible for aesthetic
	plt.gca().axis('off')

	# create copies to avoid over-write issues
	covMatTime_df_list    = df_list.copy()
	covMatCountry_df_list = df_list.copy()
	
	# aggregate the data country wise
	for i in range(len(covMatCountry_df_list)): covMatCountry_df_list[i] = aggregations.groupbyCountry(covMatCountry_df_list[i])

	# aggregate the data monthly
	covMatTime_df_list[-1] = aggregations.groupbyMonthlyCovid(covMatTime_df_list[-1])

	# imputate and aggregate for time WHO Indicator data
	for i in range(len(covMatTime_df_list) - 1): covMatTime_df_list[i] = aggregations.imputateMonthlyOther(covMatTime_df_list[i])

	# call the plotter for time and country aggs and add axis to fig
	# bool value removes x axis labels on the top plot and keeps them on the bottom
	# call the spliced dataframes as the frames to plot corrs on
	corrPlotter.corr_plot(aggregations.splicer(covMatCountry_df_list), covMatTime_ax, labels=False)
	corrPlotter.corr_plot(aggregations.splicer(covMatTime_df_list), covMatCountry_ax)

	fig.add_subplot(covMatTime_ax)
	fig.add_subplot(covMatCountry_ax)

	plt.suptitle("Overview Graphs: Time and Country CovMats for Sars-Cov2")
	
	if not DEBUG:
		plt.savefig(os.path.join(os.path.join(os.path.join(baseDir, "plots_pngs"), "CovMats Sars-Cov2 RAW.png")))
	
	############################################################################
	# 5. 
	# Setup and call a new figure for boxplots.
	# Note: this creates a boxplot for every graph generated in 2.
	############################################################################

	# call a new figure for a new series of plots
	fig = plt.figure(figsize=FIGSIZE)

	# the outer grid object, this holds two inner grids that we assign plots to
	# inner is for use with plotting, outer is purely spacing
	outer_grid = gridspec.GridSpec(2, 1, wspace=0.2, hspace=0.2)
	
	innerTop_grid = gridspec.GridSpecFromSubplotSpec(
		1, charts_int, 
		subplot_spec=outer_grid[0],
		wspace=0.1, hspace=0.1
		)
	
	innerBottom_grid = gridspec.GridSpecFromSubplotSpec(
		1, charts_int, 
		subplot_spec=outer_grid[1],
		wspace=0.1, hspace=0.1
		)

	# create a boxplot for an arbitrary data frame, use an outlier marker and add a legend for it
	# Albert: added legend for outlier symbol
	# see: https://stackoverflow.com/questions/55648729/python-how-to-print-the-box-whiskers-and-outlier-values-in-box-and-whisker-plot
	green_diamond = dict(markerfacecolor='g', marker='D')

	# now create the subplots for each chart, ie make n new axis
	i = 0
	for df in df_list:
		
		# check to align on top or bottom of grid
		if i < 5:
			ax = plt.Subplot(fig, innerTop_grid[i])
		elif i > 4 and i < 10:
			ax = plt.Subplot(fig, innerBottom_grid[i-5])
		else:
			break

		# grab the label for x axis from the frame
		label_str = df.schema[0]

		# this is fucky check but it works, it'll break if it misses twice tho
		# an we'll pipget a gap in the figure
		try:
			plotVals_dict = ax.boxplot(
				df_list[i]["Numeric"],
				labels=[label_str],
				flierprops=green_diamond
				)

			# add the legend for outliers
			ax.legend(plotVals_dict['fliers'], ['outliers'])
			ax.set_ylabel(label_str)
			fig.add_subplot(ax)
			i += 1

		except KeyError:
			try:
				plotVals_dict = ax.boxplot(
					df_list[i + 1]["Numeric"],
					labels=[label_str],
					flierprops=green_diamond
					)

				# add the legend for outliers
				ax.legend(plotVals_dict['fliers'], ['outliers'])
				ax.set_ylabel(label_str)
				fig.add_subplot(ax)
				i += 1

			except KeyError:
				pass

	plt.suptitle("Overview Graphs: Boxplots for WHO Indicators")
	
	if not DEBUG:
		plt.savefig(os.path.join(os.path.join(os.path.join(baseDir, "plots_pngs"), "Boxplots WHO RAW.png")))

	if DEBUG:
		plt.show()

################################################################################
# Main
################################################################################

def main():
	if not _runStartup():
		return False

	makeAllThePlots()
