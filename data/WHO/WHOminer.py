from selenium.webdriver import Chrome
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.common import exceptions

import pandas as pd
import numpy as np
import os
import requests
import pickle


ATTRIBUTES = {
'Average of 13 International Health Regulations core capacity scores':None,
'Composite coverage index (%)':None,
'Population with household expenditures on health greater than 10% of total household expenditure or income':None,
'Population with household expenditures on health greater than 25% of total household expenditure or income':None,
'Children aged < 5 years with pneumonia symptoms taken to a health facility (%)':None,
'Existence of a register of patients who had rheumatic fever and rheumatic heart disease':None,
'Mean systolic blood pressure (age-standardized estimate)':None,
'Medical doctors (number)':None,
'Cancer, age-standardized death rates (15+), per 100,000 population':None,
'Current health expenditure (CHE) as percentage of gross domestic product (GDP) (%)':None,
'Current health expenditure (CHE) per capita in PPP int$':None,
'Zoonotic Events and the Human-animal Interface':None,
}

GHO_API = "https://ghoapi.azureedge.net/api/"
ATHENA_API = "https://apps.who.int/gho/athena/api/GHO/"
DEBUG = False

def GETindicatorCodes():
	r = requests.get(GHO_API+'Indicator')

	indicators = list(str(r.content).split('}'))
	del indicators[0]
	length = len(indicators)
	for i in range(length):
		indicators[i] = indicators[i][2:]
		indicators[i] = indicators[i][:-16]

	if DEBUG:
		print("Found {} indicators...".format(length))
	return indicators

def GETindicatorData(indicator, apiPath):
	apiPath += indicator
	apiPath += '.csv'
	# r = requests.get(apiPath)
	df = pd.read_csv(apiPath)
	if DEBUG:
		print("\nAcquired: {} with shape {}...\n".format(indicator, df.shape))
		print(df.describe())
	return df

def dataScraper():
	indicators = GETindicatorCodes()
	listIndicatorCodes(indicators)
	for attribute in ATTRIBUTES:
		df = GETindicatorData(ATTRIBUTES[attribute], ATHENA_API)
		df.to_csv(ATTRIBUTES[attribute]+".csv")

	with open("WHO_INDICATORS.txt", "wb") as output:
		# for key, val in ATTRIBUTES.items():
		# 	out = str("{} : {}\n".format(key, val))
		# 	output.write(out)
		pickle.dump(ATTRIBUTES, output)


def listIndicatorCodes(indicators):
	keys = list(ATTRIBUTES.keys())
	for i in range(len(indicators)):
		for key in keys:
			if key in indicators[i]:
				# code between 3rd and 4th " characters
				# 3rd " is at idx = 16
				idx = indicators[i][17:].find('"')
				ATTRIBUTES[key] = indicators[i][17:(idx+17)]
				keys.remove(key) # dont search for the key we just found


dataScraper()
