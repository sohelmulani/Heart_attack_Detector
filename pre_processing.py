#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 28 18:48:31 2019

@author: sohel
"""

from sklearn.preprocessing import MinMaxScaler
from sklearn.cross_validation import train_test_split

class Preprocessing(object):
    def __init__(self):
        pass
    
    def scalling(self,x):
        scaler=MinMaxScaler(feature_range=(0,1))
        scaledX=scaler.fit_transform(x)
        return scaledX
    
    def decomposition(self,x,y):
        x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=0)
        return x_train,x_test,y_train,y_test
    
    def __del__(self):
        pass