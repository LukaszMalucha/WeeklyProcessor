# -*- coding: utf-8 -*-
"""
Created on Sat Feb 29 07:57:03 2020

@author: LukaszMalucha
"""


import pandas as pd
import numpy as np
import itertools


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


#dataset = pd.read_csv("documents_unique_document_id.csv", encoding='utf-8-sig')
    
dataset = pd.read_csv("documents_fixed_topics.csv", encoding='utf-8-sig')

"""
TOPIC QUICKFIX - MISSING METADATA
"""




"""
PRODUCTS DATASET
"""


       
dataset_products = dataset[['product_name', 'brand', 'product_category', 
                   'product_code', 'product_series', 'business', 'product_identifier']]    


dataset_products = dataset_products.drop_duplicates()





dataset_products = dataset_products.replace(np.nan, "Not Specified", regex=True)
unique_products = list(dataset_products['product_identifier'].unique())


tryit = dataset_products[dataset_products['brand'] == "Not Specified"]



dataset_products.to_csv("dataset_products.csv",  encoding='utf-8-sig', index=False)



"""
DOCUMENTS DATASET - DOCUMENT IS WHEN TOPIC TITLE == DOCUMENT TITLE. OTHERS ARE JUST TOPICS
"""

dataset_documents = dataset[['topic_title','document_title', 'document_number', 'document_part_number', 'document_version', 
                   'document_revision', 'document_type', 'document_created_at',
                   'document_last_edition', 'document_last_publication', 
                   'document_revised_modified', 'brand', 'document_link', 'maps_link', 
                   'product_identifier', 'document_identifier']]





#erratic = dataset_documents[dataset_documents['document_number'] == "Not Specified"]
#erratic_2 = erratic[erratic['document_part_number'] == "Not Specified"]


dataset_documents = dataset_documents[dataset_documents['topic_title'] == dataset_documents['document_title']]
dataset_documents = dataset_documents.drop(['topic_title'], axis=1)

"""
There is 376 duplicates diffrentiating only by one day in "created_at" - keeping earliest only
"""
dataset_documents = dataset_documents.sort_values('document_created_at').drop_duplicates(subset="document_identifier", keep="first")


dataset_documents = dataset_documents.drop_duplicates()

#unique_documents = list(dataset_documents['document_identifier'].unique())
#dataset_documents['duplicate'] = dataset_documents.duplicated(subset=['document_identifier'])
#docs_duplicates = dataset_documents[dataset_documents['duplicate'] == True]

dataset_documents.to_csv("dataset_documents.csv",  encoding='utf-8-sig', index=False)





"""
TOPICS DATASET
"""

dataset_topics = dataset[['topic_title','document_title','document_last_edition', 'document_link', 'breadcrumb', 'document_identifier']]

dataset_topics = dataset_topics[dataset_topics['topic_title'] != dataset_topics['document_title']]


# Check
erratic = dataset_topics[dataset_topics['breadcrumb'] == "nan"]


dataset_topics['topic_depth'] = dataset_topics['breadcrumb'].apply(lambda x: breadcrumb_depth(x))
dataset_topics['topic_parent'] = dataset_topics['breadcrumb'].apply(lambda x: breadcrumb_parent(x))   


dataset_topics = dataset_topics.drop(['document_title'], axis=1)
dataset_topics = dataset_topics.drop(['breadcrumb'], axis=1)

dataset_topics = dataset_topics.drop_duplicates()

dataset_topics = dataset_topics[['topic_title','topic_parent', 'topic_depth','document_last_edition', 'document_link', 'document_identifier' ]]


dataset_topics.to_csv("dataset_topics.csv",  encoding='utf-8-sig', index=False)













"""
DATES QUICKCHECK
"""

def is_valid_date(lst):
    """Helper function that check if date is valid"""
    invalid_date = []
    for date in lst:
        try:
            year = int(date[:4])
            month = int(date[5:7])
            day = int(date[8:10])
        except:
            invalid_date.append(date)
            return invalid_date
        day_count_for_month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        if year%4==0 and (year%100 != 0 or year%400==0):
            day_count_for_month[2] = 29
        valid = (1 <= month <= 12 and 1 <= day <= day_count_for_month[month])
        if not valid:        
            invalid_date.append(date)
    return invalid_date 




created_at_unique = list(dataset['document_created_at'].unique())
last_edition_unique = list(dataset['document_last_edition'].unique())
last_publication_unique = list(dataset['document_last_publication'].unique())
revised_modified_unique = list(dataset['document_revised_modified'].unique())


# IF LIST NEED TO GET UPDATED
invalid_created_at = is_valid_date(created_at_unique)
invalid_last_edition_unique = is_valid_date(last_edition_unique)
invalid_last_publication_unique = is_valid_date(last_publication_unique)
invalid_revised_modified_unique = is_valid_date(revised_modified_unique)        
invalid_dates =  list(set(itertools.chain(invalid_created_at, invalid_last_edition_unique, invalid_last_publication_unique, invalid_revised_modified_unique)))



"""
PROD VS DOC QUICKCHECK
"""

unique_prods = list(dataset_products['product_identifier'].unique())
unique_docs = list(dataset_documents['product_identifier'].unique())
missing_id_list = np.setdiff1d(unique_docs, unique_prods, assume_unique=True).tolist()


"""
DOCS VS TOPICS QUICKCHECK
"""

unique_documents = list(dataset_documents['document_identifier'].unique())
unique_topics = list(dataset_topics['document_identifier'].unique())
missing_id_list = np.setdiff1d(unique_topics,unique_documents, assume_unique=True).tolist()







"""
FRONTEND INFO
"""

dataset = pd.read_csv("documents_unique_document_id.csv", encoding='utf-8-sig')


dataset.product_name.str.len().max()  # 140 chars
dataset.brand.str.len().max()
dataset.product_series.str.len().max()
dataset.product_category.str.len().max()
dataset.product_code.str.len().max()
dataset.product_part_number.str.len().max()
dataset.business.str.len().max()


len("Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt utlabore et dolore magna aliqua. Ut enim ad minim veniam loro")



len("Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt utlaboreto")

len("Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt utlabore et dolore magna aliqua. Ut enim ad minim veniam loro All TM and VSD Model OptiSpeed Compressor Drives Gate Driver Test Mode, Drives and Starters")


tryit = dataset[dataset['topic_title'] == "Input and Output terminals"]





