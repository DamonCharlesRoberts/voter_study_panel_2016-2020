# Title: Cleaning Script for Voter Study 2016-2020 Panel Data Set

# Notes:
    #* Description: Script for cleaning 2016-2020 Voter Study
    #* Updated: 2021-12-15
    #* Updated by: dcr

# Setup
    #* Load libraries
import os
import numpy as np
import pandas as pd
import plotly.graph_objects as go
    #* WD
os.chdir('/Users/damonroberts/Dropbox/datasets/voter_study_2016-2020_panel') # Mac path
    #* Load dataset
vsdata = pd.read_stata('data/voter_panel.dta', convert_categoricals=False)
        #** Create version for cleaning
vsclean = vsdata
# Checking out the raw data
    #* Get shape of dataset
vsdata.info # 12517 x 1797
    #* Get summary stats of numerical factors
vsdata.describe()
    #* Get info about the number of missing values in each column
vsdata.isnull().sum() # large attrition in 2020 panel
    #* Coding PID - 7 item
        #** Coded as: pid7_2020Nov - 1 Strong Dem : 7 Strong Rep, 8 Not Sure
        #** Recoded to: pid_2020 - -3 Strong Dem : 3 Strong Rep, NaN Not Sure
vsclean['pid_2020'] = vsdata['pid7_2020Nov'] - 4
vsclean['pid_2020'] = vsclean['pid_2020'].replace(4, np.NaN)
    #* Coding PID - 3 item
        #** Coded as: pid7_2020Nov - 1 Strong Dem : 7 Strong Rep, 8 Not Sure
        #** Recoded to: pid_2020 - -1 Dem : 1 Rep, NaN Not Sure
vsclean['pid3_2020'] = vsdata['pid7_2020Nov'] - 4
vsclean['pid3_2020'] = vsclean['pid_2020'].replace(4, np.NaN).replace(-3, -1).replace(-2, -1).replace(-1, -1).replace(0,0).replace(1,1).replace(2,1).replace(3,1)
vsclean['pid3_2020'] = vsclean['pid3_2020'].astype(int, errors = 'ignore')
    #* Ideology of Biden
        #** Coded as: ideo5_biden_2020Nov - 1 Very Liberal : 5 Very Conservative, 6 Not Sure
        #** Recoded to: ideo5_biden_2020Nov - 1 Very Liberal : 5 Very Conservative, NaN Not Sure
vsclean['ideo5_biden_2020Nov'] =  vsdata['ideo5_biden_2020Nov'].replace(6, np.NaN)
    #* Ideology of Democrats
        #** Coded as: ideo5_dems_2020Nov - 1 Very Liberal : 5 Very Conservative, 6 Not Sure
        #** Recoded to: ideo5_dems_2020Nov - 1 Very Liberal : 5 Very Conservative, NaN Not Sure
vsclean['ideo5_dems_2020Nov'] =  vsdata['ideo5_dems_2020Nov'].replace(6, np.NaN)
    #* Ideology of Trump
        #** Coded as: ideo5_trump_2020Nov - 1 Very Liberal : 5 Very Conservative, 6 Not Sure
        #** Recoded to: ideo5_trump_2020Nov - 1 Very Liberal : 5 Very Conservative, NaN Not Sure
vsclean['ideo5_trump_2020Nov'] =  vsdata['ideo5_trump_2020Nov'].replace(6, np.NaN)
    #* Ideology of GOP
        #** Coded as: ideo5_GOP_2020Nov - 1 Very Liberal : 5 Very Conservative, 6 Not Sure
        #** Recoded to: ideo5_GOP_2020Nov - 1 Very Liberal : 5 Very Conservative, NaN Not Sure
vsclean['ideo5_gop_2020Nov'] =  vsdata['ideo5_gop_2020Nov'].replace(6, np.NaN).replace(8, np.NaN)

# Looking at some interesting relationships
    #* Partisan break down of perceptions of Biden, Trump, GOP, and Dem Ideology
vsideo = vsclean[['pid3_2020', 'ideo5_biden_2020Nov', 'ideo5_dems_2020Nov', 'ideo5_trump_2020Nov', 'ideo5_gop_2020Nov']].dropna() # Subset dataset

fig = px.parallel_categories(vsideo, dimensions=['ideo5_biden_2020Nov', 'ideo5_dems_2020Nov', 'ideo5_trump_2020Nov', 'ideo5_gop_2020Nov'],color="pid3_2020", color_continuous_scale=px.colors.sequential.Bluered,labels={'ideo5_biden_2020Nov':'Biden', 'ideo5_dems_2020Nov':'Democrats', 'ideo5_trump_2020Nov':'Trump', 'ideo5_gop_2020Nov': 'GOP'})

fig.show()