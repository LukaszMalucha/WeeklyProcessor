# -*- coding: utf-8 -*-
"""
Created on Wed Feb 19 17:40:18 2020

@author: jmalucl
"""

import pandas as pd
import numpy as np




"""
HAVE A LOOK ON UNIQUE DOC NUMBER
"""


def document_number_cleaner(dataset):
    

    
    
    dataset['document_number'] = dataset['Document Number']
    dataset = dataset.drop(['Document Number'], axis=1)
    
    # REMOVE (OTHER CHOICES AVAILABLE)
    dataset['document_number'] = dataset['document_number'].str.replace("other choices available", "")
    dataset['document_number'] = dataset['document_number'].str.replace("\(", "")
    dataset['document_number'] = dataset['document_number'].str.replace("\)", "")
    
    
    return dataset
    
    