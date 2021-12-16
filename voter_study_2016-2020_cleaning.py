# Title: Cleaning Script for Voter Study 2016-2020 Panel Data Set

# Notes:
    #* Description: Script for cleaning 2016-2020 Voter Study
    #* Updated: 2021-12-15
    #* Updated by: dcr

# Setup
    #* Load libraries
import os
import pandas as pd
    #* WD
os.chdir('/Users/damonroberts/Dropbox/datasets/voter_study_2016-2020_panel') # Mac path
    #* Load dataset
vsdata = pd.read_stata('voter_panel.dta', convert_categoricals=False)

# Checking out the raw data
    #* Get shape of dataset
vsdata.info # 12517 x 1797
    #* Get summary stats of numerical factors
vsdata.describe()
    #* Get info about the number of missing values in each column
vsdata.isnull().sum() # large attrition in 2020 panel