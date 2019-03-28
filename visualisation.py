#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 28 19:31:04 2019

@author: sohel
"""

import seaborn as sb
import matplotlib.pyplot as plt
import pandas as pd

class Vis(object):
     def __init__(self):
         pass
         
     def seabornVis(self,dataset):
         sb.pairplot(dataset,hue='target',vars=['sex','cp','trestbps','chol','fbs','restecg','thalach','exang','oldpeak','slope','ca','thal'])
         plt.show()
         
     def histogramVis(self,dataset):    
         dataset.hist(figsize=(10,10))
         plt.show()
         
     def __del__(self):
         pass
     
         
         
