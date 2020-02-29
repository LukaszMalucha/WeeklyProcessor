# -*- coding: utf-8 -*-
"""
Created on Sat Feb 29 07:57:03 2020

@author: LukaszMalucha
"""


import pandas as pd

dataset = pd.read_csv("documents_cleaned_products.csv", encoding='utf-8-sig')


products_unique = list(dataset['product_name'].unique())


products_split = []
for element in products_unique:
    split = element.split(',')
    for e in split:
        e = e.strip()
        products_split.append(e)
        
        
        
products_coma = []
for element in products_unique:
    if "," in element:
        products_coma.append(element) 
 

"""
PRODUCTS DATASET
"""
       
dataset_products = dataset[['product_name', 'product_brand', 'product_category', 
                   'product_code', 'product_series', 'product_part_number', 
                   'business']]   


dataset_products = dataset_products.drop_duplicates()
dataset_products.to_csv("dataset_products.csv",  encoding='utf-8-sig', index=False)



"""
DOCUMENTS DATASET
"""

dataset_document = dataset[['document_title', 'document_number', 'document_version', 
                   'document_revision', 'document_type', 'document_created_at', 
                   'document_last_edition', 'document_last_publication', 'maps_link',
                   'document_revised_modified', 'document_link', 'product_name']]

dataset_document = dataset_document.drop_duplicates()
dataset_document.to_csv("dataset_document.csv",  encoding='utf-8-sig', index=False)



"""
TOPICS DATASET
"""

dataset_topic = dataset[['topic_title','document_title']]
dataset_topic = dataset_topic.drop_duplicates()
dataset_topic.to_csv("dataset_topic.csv",  encoding='utf-8-sig', index=False)










