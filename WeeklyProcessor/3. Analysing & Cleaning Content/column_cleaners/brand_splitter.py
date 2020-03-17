# -*- coding: utf-8 -*-
"""
Created on Tue Feb 18 17:42:50 2020

@author: jmalucl
"""

import pandas as pd



def brand_splitter(dataset):
    """
    brand
    IDEALLY THERE SHOULD BE ONE ROW FOR EACH COMPANY. THEY SHOULD NOT BE LISTED IN A ONE FIELD
    """
    
    dataset['brand'].fillna("Not Specified")
    dataset['brand'] = dataset['brand'].apply(lambda x: x.split(',')) 
    


    # SPLIT LISTED COMPANIES INTO SEPARATE ROWS
    brand_column = dataset.apply(lambda x: pd.Series(x['brand']), axis=1).stack().reset_index(level=1, drop=True)
    brand_column.name = 'brand'
    dataset = dataset.drop('brand', axis=1).join(brand_column)
    dataset['brand'] = pd.Series(dataset['brand'], dtype=object)
    
    # REMOVE (OTHER CHOICES AVAILABLE)
    dataset['brand'] = dataset['brand'].str.replace("other choices available", "")
    dataset['brand'] = dataset['brand'].str.replace("(", "")
    dataset['brand'] = dataset['brand'].str.replace(")", "")
    dataset['brand'] = dataset['brand'].str.replace("TYCO", "Tyco")
    
    # REMOVE WHITESPACES
    dataset['brand'] = dataset['brand'].str.strip()
    
    return dataset





















    


