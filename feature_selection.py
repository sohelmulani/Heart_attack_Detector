#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 28 18:57:41 2019

@author: sohel
"""

from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import chi2
import numpy as np

class FeatureSelection(object):
    def __init__(self):
        pass
    
    def selectBest(self,x,y,n):
        self.x=x
        self.y=y
        self.skb=SelectKBest(score_func=chi2,k=n)
        self.selected=self.skb.fit(self.x,self.y)
        return self.selected
    
    def printScore(self):
        np.set_printoptions(precision=2)
        print(self.skb.scores_)
        
    def selectFinalFetures(self):
        finalX=self.selected.transform(self.x)
        return(finalX)
        
    def __del__(self):
        pass
    
        