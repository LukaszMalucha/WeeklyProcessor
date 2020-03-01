# -*- coding: utf-8 -*-
"""
Created on Sun Mar  1 18:14:40 2020

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


def unique_product_id(filename):    
    
    """
    CLEAR PRODUCT CATEGORIES
    if product name and brand are the same then take all categories together and create one long list separated by comma
    """
    
    
    dataset = pd.read_csv(filename, encoding='utf-8-sig')
    
    dataset = dataset.drop_duplicates()
    
    
    ## GROUP BY THE SAME NAME + BRAND AND CREATE LONG CATEGORY LIST 
    dataset_cat = dataset.groupby(['product_name','product_brand'], as_index=False).agg(', '.join)
    dataset_cat['product_category_long'] = dataset_cat['product_category'].apply(lambda x: unique_elements(x)) 
    
    dataset_cat = dataset_cat[['product_name','product_brand','product_category_long']]
    
    
    dataset = dataset.merge(dataset_cat, how = "left", on = ['product_name','product_brand'])
    
    
    dataset['product_category'] = dataset['product_category_long']
    dataset = dataset.drop(['product_category_long'], axis=1)
    
    dataset = dataset.drop_duplicates()
    
    
    """
    CLEAN PRODUCT SERIES
    """
    
    ## GROUP BY THE SAME NAME + BRAND AND CREATE LONG CATEGORY LIST 
    dataset_series = dataset.groupby(['product_name','product_brand', 'product_category'], as_index=False).agg(', '.join)
    dataset_series['product_series_long'] = dataset_series['product_series'].apply(lambda x: unique_elements(x)) 
    
    dataset_series = dataset_series[['product_name','product_brand','product_category', 'product_series_long']]
    
    
    dataset = dataset.merge(dataset_series, how = "left", on = ['product_name','product_brand','product_category'])
    
    
    dataset['product_series'] = dataset['product_series_long']
    dataset = dataset.drop(['product_series_long'], axis=1)
    
    dataset = dataset.drop_duplicates()
    
    
    
    """
    SORT PRODUCT CODES
    """
    
    dataset['product_code'] = dataset['product_code'].apply(lambda x: sort_list(x))
    
    ## GROUP BY THE SAME NAME + BRAND AND CREATE LONG CATEGORY LIST 
    dataset_codes = dataset.groupby(['product_name','product_brand', 'product_category'], as_index=False).agg(', '.join)
    dataset_codes['product_code_long'] = dataset_codes['product_code'].apply(lambda x: unique_elements(x))
    
    dataset_codes = dataset_codes[['product_name','product_brand','product_category', 'product_code_long']]
    
    dataset = dataset.merge(dataset_codes, how = "left", on = ['product_name','product_brand','product_category'])
    
    dataset['product_code'] = dataset['product_code_long']
    dataset = dataset.drop(['product_code_long'], axis=1)
    
    dataset = dataset.drop_duplicates()
    
    
    
    """
    CREATING UNIQUE IDENTIFIER FOR ALL PRODUCTS
    first part of name + created_id + first three letters of brand ...
    """
    
    
    dataset['product_name_first'] = dataset['product_name'].str.split(',').str[0]
    dataset['product_name_id'] = dataset['product_name'].apply(lambda x: first_letters(str(x)))
    dataset['product_brand_id'] = dataset['product_brand'].str[:3]
    dataset['product_category_id'] = dataset['product_category'].apply(lambda x: first_letters(str(x)))
    dataset['product_code_id'] = dataset['product_code'].apply(lambda x: first_letters(str(x)))
    dataset['product_code_last'] = dataset['product_code'].str.split(',').str[-1]
    dataset['product_series_id'] = dataset['product_series'].apply(lambda x: first_letters(str(x)))
    dataset['product_part_number_id'] = dataset['product_part_number'].apply(lambda x: first_letters(str(x)))
    dataset['product_business_id'] = dataset['business'].apply(lambda x: first_letters(str(x)))
    
    
    dataset['product_identifier'] = dataset['product_name_first'] + "-" + dataset['product_brand_id'] +  "-" + dataset['product_code_last']  + "-" + dataset['product_series_id'] + "-" + dataset['product_part_number'] + dataset['product_business_id']            
    
    dataset['product_identifier'] = dataset['product_identifier'].str.replace('Not Specified', 'na')
    dataset['product_identifier'] = dataset['product_identifier'].str.replace(' ', '_')
    
    dataset = dataset.drop(['product_name_first'], axis=1)
    dataset = dataset.drop(['product_name_id'], axis=1)
    dataset = dataset.drop(['product_brand_id'], axis=1)
    dataset = dataset.drop(['product_category_id'], axis=1)
    dataset = dataset.drop(['product_code_id'], axis=1)
    dataset = dataset.drop(['product_code_last'], axis=1)
    dataset = dataset.drop(['product_series_id'], axis=1)
    dataset = dataset.drop(['product_part_number_id'], axis=1)
    dataset = dataset.drop(['product_business_id'], axis=1)
    
    dataset.to_csv('documents_unique_id.csv',  encoding='utf-8-sig', index=False)
    
    
    return dataset




data = unique_product_id('documents_cleaned_products.csv')
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    

    