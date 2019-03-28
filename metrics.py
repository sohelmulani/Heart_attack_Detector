#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 28 19:43:59 2019

@author: sohel
"""

from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix
import numpy as np

class Metrics(object):
    def __init__(self):
        pass
    
    def accuracy(self,y_pred,y_test):
        print("{} %".format(accuracy_score(y_pred,y_test)*100))
        
    def confusionMatrix(self,y_pred,y_test):
        np.set_printoptions(precision=2)
        print(confusion_matrix(y_pred,y_test))
        
    def __del__(self):
        pass
    