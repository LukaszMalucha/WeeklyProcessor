# -*- coding: utf-8 -*-
"""
Created on Sat Feb 29 07:57:03 2020

@author: LukaszMalucha
"""






import pandas as pd


def unique_elements(string):
    """Get unique elements after merging strings"""
    new_list = string.split(', ')
    new_list = list(set(new_list))
    new_list = ', '.join(sorted(new_list))
    return new_list


def sort_list(string):
    """sort/unique string"""
    new_list = string.split(', ')
    new_list = list(set(new_list))
    new_list = ', '.join(sorted(new_list))         
    return new_list


def first_letters(string):
    """First and last letter of a word to create some unique id"""
    first = string[0]
    last = string[-1]
    return first + last


dataset = pd.read_csv("documents_unique_id.csv", encoding='utf-8-sig')


products_unique = list(dataset['product_name'].unique())





"""
PRODUCTS DATASET
"""

       
dataset_products = dataset[['product_name', 'product_brand', 'product_category', 
                   'product_code', 'product_series', 'product_part_number', 
                   'business', 'product_identifier']]    


dataset_products = dataset_products.drop_duplicates()

products_unique = list(dataset['product_name'].unique())

dataset_products.to_csv("dataset_products.csv",  encoding='utf-8-sig', index=False)



"""
DOCUMENTS DATASET - DOCUMENT IS WHEN TOPIC TITLE == DOCUMENT TITLE. OTHERS ARE JUST TOPICS
"""

dataset_documents = dataset[['topic_title','document_title', 'document_number', 'document_version', 
                   'document_revision', 'document_type', 'document_created_at',
                   'document_last_edition', 'document_last_publication', 
                   'document_revised_modified', 'document_link', 'maps_link', 
                   'product_identifier']]


dataset_documents = dataset_documents[dataset_documents['topic_title'] == dataset_documents['document_title']]
dataset_documents['document_category'] = "document"

dataset_documents = dataset_documents.drop(['document_title'], axis=1)

dataset_documents = dataset_documents.drop_duplicates()


dataset_documents = dataset_documents.drop_duplicates()




"""
TOPICS DATASET
"""

dataset_topics = dataset[['topic_title','document_title', 'document_number', 'document_version', 
                   'document_revision', 'document_type', 'document_created_at',
                   'document_last_edition', 'document_last_publication', 
                   'document_revised_modified', 'document_link', 'maps_link', 
                   'product_identifier']]

dataset_topics = dataset_topics[dataset_topics['topic_title'] != dataset_topics['document_title']]
dataset_topics['document_category'] = "topic"
dataset_topics = dataset_topics.drop(['document_title'], axis=1)

dataset_topics = dataset_topics.drop_duplicates()


dataset_docs = pd.concat([dataset_documents, dataset_topics])




dataset_docs.to_csv("dataset_documents.csv",  encoding='utf-8-sig', index=False)





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
 




