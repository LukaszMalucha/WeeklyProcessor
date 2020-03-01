# -*- coding: utf-8 -*-
"""
Created on Wed Feb 19 11:54:04 2020

@author: jmalucl
"""

import pandas as pd


#dataset = pd.read_csv("documents_processed.csv", encoding='utf-8-sig')
#
#
#columns = list(dataset.columns)

"""
DROP COLUMNS AS LISTED IN EMAIL
"""


def column_remover(dataset):
    
    dataset = dataset.drop(['meta_clusterId', 'meta_editorialType', 'meta_dita:ditavalPath', 'meta_khubVersion', 'meta_openMode', 'meta_maps_link', 'meta_category_bas', 'meta_category_ductedsystems', 'meta_category_visonic',], axis=1)

    return dataset
    