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
import matplotlib.dates as mdates

# SKLEARN
from sklearn.preprocessing import (MinMaxScaler, StandardScaler)
from sklearn.impute import SimpleImputer


def plotCorrKendall(data: pd.DataFrame, ax, labels=True) -> bool:
    """
        Author : Albert Ferguson
        Brief  : Attaches the correlation matrix to the given axis as a heatmap.
        Details: 
            Utilises the kendall method and applies cell annotations.

        Param  : data, a dataframe to calculate correlation coeff's on.
        Param  : ax, a premade axis to attach the graph to.
        Param  : label, an optional boolean to attach labels to the cells.
    """
    sns.heatmap(data.corr(method ='kendall') , annot=True, ax=ax, xticklabels=labels)

    return True

def plot(feature: pd.Series, ax, colour: str, label:str) -> bool:
    """
        Author : Albert Ferguson
        Brief  : Fit and plot a univariate or bivariate kernel density estimate.
        Details: 
            Takes the df series to plot with type: pd.Series and the axis to attach to.
            See: https://seaborn.pydata.org/generated/seaborn.kdeplot.html
        Note   : colour is a string value, e.g. 'r', 'b', 'g'.
        Note   : cuts the data to range of data by default.
    """

    # call the plt plot type function on each axis, then set axis labels
    sns.distplot(feature, kde_kws={"cut":0, "shade":True, "bw":0.2, "color":colour}, ax=ax)
    ax.set_ylabel('Fitted Probability Density'); ax.set_xlabel(label)
    
    return True

def barPlotComp(x, y, ax, constantComp, labels) -> bool:
    """
        Author : Albert Ferguson
        Brief  : Uses constant comp to compare to a constant value on y-axis.
        Details: 
            Takes the df series to plot with type: pd.Series and the axis to attach to.
            See: https://seaborn.pydata.org/generated/seaborn.kdeplot.html

        Param  : x, categorical/indexable data to place on bar chart x-axis.
        Param  : y, numerical data to place on bar chart y-axis.
        Param  : ax, a premade axis to attach the graph to.
        Param  : labels, a label for the graph x-axis names.
        Param  : constantComp, a constant numeric value for capacity comparisons to the y-axis data.

        Note  : generates a bar plot using countries and territories.
        Note  : https://matplotlib.org/3.2.1/api/_as_gen/matplotlib.pyplot.axhline.html for docs.
        Note  : Previous method called -- style for line plot, this happens to align with the barplot
                default widths and looks confusing.
        Note  : Note the len conversion for y in ax.plot, matching dimensions.
    """

    ax.bar(x, y, color='red', label=labels)
    ax.plot(x, [constantComp]*len(x), label="Medical constant")
    plt.xticks(rotation=30)
    ax.legend(loc="right")
    return True

def plotCulmValues(data: pd.DataFrame, bins: int, ax, label) -> bool:
    """
        Author : Albert Ferguson
        Brief  : Plot the culminative cases/deaths/etc. against to time.	
        Param  : data, a dataframe with the data to index by time.
        Param  : bins, int value for the number of bins to apply.
        Param  : ax, a premade axis to attach the graph to.
        Param  : label, a label for the graph title.

        Note  : Note the len conversion for y in ax.plot, matching dimensions.
    """

    def plotHist(x: np.ndarray, bins: int, label:str, ax) -> list:
        """
        Brief   : Generate a step'ed histogram plot for n bins.
        Returns : list, [n, bins, patches]
        """
        try:
            # n, bins, patches = ax.hist(x, bins=bins, density=True, histtype="step",
            # 			   		      cumulative=True, label=label)
            n, bins, patches = ax.hist(x, bins=bins, density=True, histtype="step",
                                         cumulative=True, label=label, align="mid")
            return_vals = [n, bins, patches]
        except ValueError:
            return False
        return return_vals

    def plotCurveApprox(sd: int, mean: int, bins: int, label:str, ax) -> bool:
        """
        Brief   : Flattened curve approx. to calculate the bell curve of our pandemic
        Returns : True if successful, False if not.
        """
        try:
            y = (( 1 / (np.sqrt(2 * np.pi) * sd)) *
                np.exp( -0.5 * ( 1 / sd * (bins - mean))**2))
            # convert to cumulative sum then calc average at all points (last val in cumulative is total)
            y = y.cumsum()
            y /= y[-1]
            ax.plot(bins, y, 'k--', linewidth=1.5, label=label)

        except ValueError:
            return False
        return True

    if data is None or ax is None:
        return False
    
    try:
        # stat's calculations
        cases_sd    = data.cases.std(); cases_mean  = data.cases.mean()
        deaths_sd   = data.deaths.std(); deaths_mean = data.deaths.mean()
    except AttributeError:
        return False
    
    # graph labels
    casesLbl_str   = "Emperical - Confirmed Cases Cumulative Frequency"
    deathsLbl_str  = "Emperical - Confirmed Deaths Cumulative Frequency"
    curveCases_str = "Projected Cases Curve (Current Environment)"
    curveDeaths_str= "Projected Deaths Curve (Current Environment)"
    
    # generate the axis plots
    res_list = plotHist(data.cases, bins, casesLbl_str, ax)
    plotCurveApprox(cases_sd, cases_mean, res_list[1], curveCases_str, ax)
    res_list = plotHist(data.deaths, bins, deathsLbl_str, ax)
    plotCurveApprox(deaths_sd, deaths_mean, res_list[1], curveDeaths_str, ax)

    # graph fine tuning for quicker viewing of axis and legend
    # xticks logic sets a tick for every month, as data is in time order this places the hist in time order
    plt.xticks(ticks = np.arange(0, ax.get_xlim()[1], ax.get_xlim()[1]/bins), labels=data.dateRep)
    ax.legend(loc="right")
    plt.title(label)
    plt.xticks(rotation=30)

    return True

def plotTimlineDelta(data: pd.DataFrame, y_vals: pd.Series, ax, title: str) -> bool:
    """
        Author : Albert Ferguson
        Brief  : Plot the change in cases and deaths per country as a timeline.
        Param  : data, a dataframe with the data to index by time.
        Param  : y_vals, the y values to calculate diff on. e.g. cases, deaths.
        Param  : ax, a premade axis to attach the graph to.
        Param  : title, the graph title.

        Note  :  Assumes time and country group have already been called.
    """

    try:
        dates_axis = data.dateRep
        cases_axis = y_vals.diff()
        dayMonth_vals = [str(t.day) + '-' + str(t.month) for t in dates_axis]
    except AttributeError:
        return False

    markerline, stemline, baseline = ax.stem(dates_axis, cases_axis, linefmt="C3-",
                                        basefmt="k-", use_line_collection=True)

    plt.setp(markerline, mec="k", mfc="w", zorder=3) # recolour markers and remove line through them
    markerline.set_ydata(np.zeros(len(data.dateRep)))

    # annotate lines
    vert = np.array(['top', 'bottom'])[(cases_axis > 0).astype(int)]
    for d, l, r, va in zip(dates_axis, cases_axis, dayMonth_vals, vert):
        text = ax.annotate(r, xy=(d, l), xytext=(-3, np.sign(l)*3),
                textcoords="offset points", va=va, ha="right")
        text.set_rotation(-90)
    
    # formatting, add title, rotate date labels and remove y axis and spines
    ax.set(title="COVID19" + title)
    plt.setp(ax.get_xticklabels(), rotation=30)

    ax.get_yaxis().set_visible(False)
    for spine in ["left", "top", "right"]: ax.spines[spine].set_visible(False)

    return True
