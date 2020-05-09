import matplotlib.pyplot as plt
import pandas as pd
import pickle
import numpy as np
import seaborn as sn
import os

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

with open(os.path.join(os.pardir, "processing_dump.txt"), "rb") as f:
		df_list = pickle.load(f)

def merge(df_list):
	merged = pd.merge(df_list[9],df_list[11],left_on='Numeric',right_on='cases', how='left')
	print(merged)
