# -*- coding: utf-8 -*-
"""
Created on Sat Feb 29 07:57:03 2020

@author: LukaszMalucha
"""


import pandas as pd
import numpy as np


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


def breadcrumb_parent(string):
    """Get parent paragraph from topic breadcrumb"""
    breadcrumb_list = string.split('> ')
    return breadcrumb_list[-2]

def breadcrumb_depth(string):
    """Get depth level for document topics - parag. > subparag. > subsub..."""
    breadcrumb_list = string.split('> ')
    return int(len(breadcrumb_list))


def get_form_id(string):
    """Get from id from title"""
    if "(Form " in string:
        new_string = string.split("(Form ")[-1]
        new_string = new_string.replace("))", "]")
        new_string = new_string.replace(")", "")
        new_string = new_string.replace("]", ")")
        return new_string
    return "Not Specified"

dataset = pd.read_csv("documents_unique_id.csv", encoding='utf-8-sig')




products_unique = list(dataset['product_name'].unique())



"""
PRODUCTS DATASET
"""

       
dataset_products = dataset[['product_name', 'product_brand', 'product_category', 
                   'product_code', 'product_series', 'business', 'product_identifier']]    


dataset_products = dataset_products.drop_duplicates()


## UNIQUE PRODUCT CHECK
#products_unique = list(dataset['product_name'].unique())
#dataset_products['duplicate'] = dataset_products.duplicated(subset=['product_name','product_brand', 'product_part_number'])


dataset_products = dataset_products.replace(np.nan, "Not Specified", regex=True)



dataset_products.to_csv("dataset_products.csv",  encoding='utf-8-sig', index=False)



"""
DOCUMENTS DATASET - DOCUMENT IS WHEN TOPIC TITLE == DOCUMENT TITLE. OTHERS ARE JUST TOPICS
"""

dataset_documents = dataset[['topic_title','document_title', 'document_number', 'document_part_number', 'document_version', 
                   'document_revision', 'document_type', 'document_created_at',
                   'document_last_edition', 'document_last_publication', 
                   'document_revised_modified', 'document_link', 'maps_link', 
                   'product_identifier']]





erratic = dataset_documents[dataset_documents['document_number'] == "Not Specified"]
erratic_2 = erratic[erratic['document_part_number'] == "Not Specified"]



"""
DOCUMENT UNIQUE IDENTIFIER
"""

# Doc Number + docum

dataset_documents = dataset_documents[dataset_documents['topic_title'] == dataset_documents['document_title']]
dataset_documents = dataset_documents.drop_duplicates()


erratic = dataset_documents[dataset_documents['document_number'] == "Not Specified"]
erratic_2 = erratic[erratic['document_part_number'] == "Not Specified"]

dataset_documents = dataset_documents.drop(['document_title'], axis=1)

dataset_documents = dataset_documents.drop_duplicates()









dataset_documents.to_csv("dataset_documents.csv",  encoding='utf-8-sig', index=False)







"""
TOPICS DATASET
"""

dataset_topics = dataset[['topic_title','document_title','document_number', 'document_last_edition', 'document_link', 'breadcrumb']]

dataset_topics = dataset_topics[dataset_topics['topic_title'] != dataset_topics['document_title']]


# Check
erratic = dataset_topics[dataset_topics['breadcrumb'] == "nan"]


dataset_topics['topic_depth'] = dataset_topics['breadcrumb'].apply(lambda x: breadcrumb_depth(x))
dataset_topics['topic_parent'] = dataset_topics['breadcrumb'].apply(lambda x: breadcrumb_parent(x))   


dataset_topics = dataset_topics.drop(['document_title'], axis=1)
dataset_topics = dataset_topics.drop(['breadcrumb'], axis=1)

dataset_topics = dataset_topics.drop_duplicates()

dataset_topics.to_csv("dataset_topics.csv",  encoding='utf-8-sig', index=False)

































hattrix = dataset[dataset['document_title'] == "EntraPass hattrix Administration Guide"]



"""
FRONTEND INFO
"""

dataset = pd.read_csv("documents_unique_id.csv", encoding='utf-8-sig')


dataset.product_name.str.len().max()  # 140 chars
dataset.product_brand.str.len().max()
dataset.product_series.str.len().max()
dataset.product_category.str.len().max()
dataset.product_code.str.len().max()
dataset.product_part_number.str.len().max()
dataset.business.str.len().max()


len("Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt utlabore et dolore magna aliqua. Ut enim ad minim veniam loro")



len("Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt utlaboreto")

len("Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt utlabore et dolore magna aliqua. Ut enim ad minim veniam loro All TM and VSD Model OptiSpeed Compressor Drives Gate Driver Test Mode, Drives and Starters")









