# Python CORE
import os
import pickle

# DATA MANIP: PANDAS AND NUMPY
import pandas as pd
import numpy as np

# MATPLOTLIB
import matplotlib.gridspec as gridspec
import matplotlib.pyplot as plt

# core user lib
from .core import aggregations, grapher, environConfig

DEBUG = False                                                      # verbose debug prints
baseDir = "data" # file name for Raw Data (defaults to my local machine as ../../data)

def _runStartup():
	"""
	:author Albert Ferguson
	Explicit startup function. Runs any necessary preloads for data and Globals updates.
	Retrieves raw data and assigns Globals to env vars, runs default ones gracefully otherwise.
	"""

	# local dev, comment this out
	env = environConfig.safe_environ()

	global DEBUG
	global baseDir

	# update with the env config
	DEBUG   = env.bool("DEBUG", False)
	baseDir = env("BASE_DATA_DIR")

	return True

def flatteningCurves():
    """
    Author : Albert Ferguson
    Brief  : Prototype the "flattening" the curve graphs.
    """

    with open(os.path.join(baseDir, "data", "processing_dump.txt", "rb")) as f:
        df_list = pickle.load(f)
    df = df_list[-1]
    countries = df.countriesAndTerritories.unique()
    for country in countries:
        fig, ax = plt.subplots(1,1)
        # SELECT WHERE COUNTRY IS "Afghanistan"
        # sort by increasing date (oldest to latest)
        _df = df[df.countriesAndTerritories.isin([country])]
        _df = aggregations.groupTimeCovid(_df)

        if (not grapher.plotCulmValues(_df, _df.shape[0], ax, str(country))):
            print("Error")
            return False
        plt.savefig(os.path.join(baseDir, "res", "graph protos", country+".png"))
    return

def curveWithConstant():
    """
    Author : Albert Ferguson
    Brief  : Prototype graphing a constant against a hisogram/barplot of the data.
    """
    
    with open(os.path.join(baseDir, "data", "processing_dump.txt", "rb")) as f: df_list = pickle.load(f)
    covid = df_list[-1]
    hcap  = df_list[6]

    countries_list = covid.countryterritoryCode.unique()
    for country in countries_list:
        fig, ax = plt.subplots(1,1)

        covid_frame = covid[covid.countryterritoryCode.isin([country])]
        hcap_series = hcap[hcap.COUNTRY.isin([country])].Numeric

        try:
            # note: series returns the original df index, no reindex occurs.
            # Use keys accesor to correctly index
            hcap_num  = hcap_series[hcap_series.keys()[0]]
        except IndexError:
            hcap_num = 0
        # compares country to constant, independent axis shows number of cases
        
        if not grapher.barPlotComp(covid_frame.dateRep, covid_frame.cases, ax, hcap_num, str(country)):
            print("Error")
            return False
        plt.savefig(os.path.join(baseDir, "res", "graph protos", "prototype country_with_health_cap", country+".png"))
    return

def deltaTimeLine():
    """
    Author : Albert Ferguson
    Brief  : Prototype the delta case, deaths and fatality ratio graphs.
    """
    
    with open(os.path.join(baseDir, "data", "processing_dump.txt", "rb")) as f: df_list = pickle.load(f)
    df = df_list[-1]
    df.drop(columns=['day', 'month', 'year', 'year_binary_encoding'], inplace=True)
    countries_list = df.countriesAndTerritories.unique()
    df_time = aggregations.groupbyTimeFreq(df)

    for country in countries_list:
        fig, ax = plt.subplots(1,1)
        
        _df = df_time[df_time.countriesAndTerritories.isin([country])]
        if not grapher.plotTimlineDelta(_df, _df.cases, ax, "COVID 19 Cases Delta against Time"):
            print("Error")
            return False
        plt.savefig("res/graph protos/prototype deltaTimeline/"+country+"_cases.png"); plt.close(fig)

    for country in countries_list:
        fig, ax = plt.subplots(1,1)

        _df = df_time[df_time.countriesAndTerritories.isin([country])]
        if not grapher.plotTimlineDelta(_df, _df.deaths, ax, "COVID 19 Deaths Delta against Time"):
            print("Error")
            return False
        plt.savefig("res/graph protos/prototype deltaTimeline/"+country+"_deaths.png"); plt.close(fig)

    for country in countries_list:
        fig, ax = plt.subplots(1,1)

        _df = df_time[df_time.countriesAndTerritories.isin([country])]
        fatalityRatio = (_df.cases / _df.deaths)
        if not grapher.plotTimlineDelta(_df, fatalityRatio, ax, "COVID 19 Fatality Ratio Delta against Time"):
            print("Error")
            return False
        plt.savefig(os.path.join(baseDir, "res", "graph protos", "prototype deltaTimeline", country+"_fatalityRatio.png")); plt.close(fig)
    return

_runStartup()

