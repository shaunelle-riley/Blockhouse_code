# -*- coding: utf-8 -*-
"""
Created on Thu May  1 11:16:35 2025

@author: SW-SQRiley
"""

import pandas as pd 
from Best_level_ofi import best_level_ofi
from Multi_level_ofi import multi_level_ofi
from Integrated_ofi import integrated_ofi

df = pd.read_csv("C:/Users/sqril/Downloads/first_25000_rows.csv")

df.head()

best_level_ofi(df)

multi_level_ofi(df, 10)

integrated_ofi(df, 10)





