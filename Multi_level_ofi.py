# -*- coding: utf-8 -*-
"""
Created on Fri May  2 14:52:33 2025

@author: sqril
"""
import pandas as pd 
import numpy as np

'''Calculating Multi-Level OFI'''
def multi_level_ofi(df, level):
    
    #Creating lists that will hold all levels
    ofi_levels = []
    depth_levels = []
    
    #Assigning columns
    for i in range(level):
        bid_px = df[f'bid_px_{i:02d}']
        ask_px = df[f'ask_px_{i:02d}']
        bid_sz = df[f'bid_sz_{i:02d}']
        ask_sz = df[f'ask_sz_{i:02d}']
        
        #Computing OFI for bid 
        of_bid_sz = (np.where(bid_px > bid_px.shift(1),bid_sz, 
                               np.where(bid_px == bid_px.shift(1), bid_sz - bid_sz.shift(1),
                                        -bid_sz)))
        
        #Computing OFI for ask 
        of_ask_sz = (np.where(ask_px > ask_px.shift(1), -ask_sz, 
                               np.where(ask_px == ask_px.shift(1), ask_sz - ask_sz.shift(1),
                                        ask_sz)))
        
        #Computing OFI and appending to list
        unweighted_ofi = of_bid_sz - of_ask_sz
        ofi_levels.append(pd.Series(unweighted_ofi, index=df.index, name=f'ofi_level_{i}'))
        
        #Computing Average depth and appending to list
        avg_depth = (bid_sz + ask_sz) / 2
        depth_levels.append(avg_depth)
        
    #Combining OFIs and depth levels into a dataframe
    ofi_stack = pd.concat(ofi_levels, axis=1)
    depth_stack = pd.concat(depth_levels, axis=1)
    
    #Computing Average Depth Across all levels
    avg_depth_all_levels = depth_stack.mean(axis=1).replace(0,np.nan)
    
    #Calculating weighted OFI
    weighted_ofi = ofi_stack.div(avg_depth_all_levels, axis=0) 
    
    #Setting first row as NaN
    weighted_ofi.iloc[0, :] = np.nan

    #Creating vector
    df['mult_level_ofi'] = weighted_ofi.astype(str).agg(','.join, axis=1)
        
    return df