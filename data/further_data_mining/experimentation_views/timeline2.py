import matplotlib.pyplot as plt
import pandas as pd
import pickle
import numpy as np
import seaborn as sn

# Python CORE
import os
import pickle
from datetime import datetime

# DATA MANIP: PANDAS AND NUMPY
import pandas as pd
import numpy as np

# SEABORN
import seaborn as sns

# MATPLOTLIB
import matplotlib.gridspec as gridspec
import matplotlib.pyplot as plt
import matplotlib.dates as mdates


def dateconv(df11):
	df11.dateRep = df11.dateRep.dt.strftime('%Y-%m-%d')
	df11.dateRep = [datetime.strptime(d, "%Y-%m-%d") for d in df11.dateRep]


def setupTL(df11):
	levels = np.tile([-5, 5, -3, 3, -1, 1],
	                int(np.ceil(len(df11.dateRep))))[:len(df11.dateRep)]
	fig, ax = plt.subplots(figsize=(8.8, 4), constrained_layout=True)
	ax.set(title="COVID19 dates")

	markerline, stemline, baseline = ax.stem(df11.dateRep, levels,
                                         linefmt="C3-", basefmt="k-",
                                         use_line_collection=True)
	plt.setp(markerline, mec="k", mfc="w", zorder=3)

	markerline.set_ydata(np.zeros(len(df11.dateRep)))

# annotate lines
	vert = np.array(['top', 'bottom'])[(levels > 0).astype(int)]
	for d, l, r, va in zip(df11.dateRep, levels, df11.cases, vert):
	    ax.annotate(r, xy=(d, l), xytext=(-3, np.sign(l)*3),
	                textcoords="offset points", va=va, ha="right")

	# format xaxis with 4 month intervals
	ax.get_xaxis().set_major_locator(mdates.MonthLocator(interval=4))
	ax.get_xaxis().set_major_formatter(mdates.DateFormatter("%b %Y"))
	plt.setp(ax.get_xticklabels(), rotation=30, ha="right")

	# remove y axis and spines
	ax.get_yaxis().set_visible(False)
	for spine in ["left", "top", "right"]:
	    ax.spines[spine].set_visible(False)

	ax.margins(y=0.1)
	plt.show()

with open(os.path.join(os.pardir, "processing_dump.txt"), "rb") as f:
		df_list = pickle.load(f)
		df = df_list

df11 = df_list[11]

dateconv(df11)
setupTL(df11)