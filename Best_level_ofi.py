# -*- coding: utf-8 -*-
"""
Created on Fri May  2 14:51:47 2025

@author: sqril
"""
import numpy as np

''' Calculating the best-level OFI'''
def best_level_ofi(df):
    
    #Assigning columns for simplicity
    bid_px = df['bid_px_00']
    ask_px = df['ask_px_00']
    bid_sz = df['bid_sz_00']
    ask_sz = df['ask_sz_00']
    
    #Computing OFI for bid 
    of_bid_sz = (np.where(bid_px > bid_px.shift(1),bid_sz, 
                           np.where(bid_px == bid_px.shift(1), bid_sz - bid_sz.shift(1),
                                    -bid_sz)))
    
    #Computing OFI for ask 
    of_ask_sz = (np.where(ask_px > ask_px.shift(1), -ask_sz, 
                           np.where(ask_px == ask_px.shift(1), ask_sz - ask_sz.shift(1),
                                    ask_sz)))
    
    #Calculating best-level OFI
    ofi = of_bid_sz - of_ask_sz
    
    #Explicitly setting first row value as NAN
    ofi[0] = np.nan
    
    #Creating column in dataframe with best-level OFI
    df['best_level_ofi'] = ofi
    
    #Returning df with best-level OFI column
    return df    