# -*- coding: utf-8 -*-
"""
Created on Sat Feb 29 07:57:03 2020

@author: LukaszMalucha
"""






import pandas as pd
import itertools


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

def unique_elements(string):
    new_list = string.split(', ')
    new_list = list(set(new_list))
    new_list = ', '.join(sorted(new_list))
    return new_list


def sort_list(string):
    new_list = string.split(', ')
    new_list = list(set(new_list))
    new_list = ', '.join(sorted(new_list))         
    return new_list

dataset = pd.read_csv("documents_cleaned_products.csv", encoding='utf-8-sig')


products_unique = list(dataset['product_name'].unique())




"""
FIXING NON-EXISTING DATES IN DATASET
"""
dataset = dataset.replace(['2020-1-29'], ['2020-01-29'])



created_at_unique = list(dataset['document_created_at'].unique())
last_edition_unique = list(dataset['document_last_edition'].unique())
last_publication_unique = list(dataset['document_last_publication'].unique())
revised_modified_unique = list(dataset['document_revised_modified'].unique())

invalid_created_at = is_valid_date(created_at_unique)
invalid_last_edition_unique = is_valid_date(last_edition_unique)
invalid_last_publication_unique = is_valid_date(last_publication_unique)
invalid_revised_modified_unique = is_valid_date(revised_modified_unique)


invalid_dates =  list(set(itertools.chain(invalid_created_at, invalid_last_edition_unique, invalid_last_publication_unique, invalid_revised_modified_unique)))




# Non-existing February 29th
dataset = dataset.replace(['2019-04-31', '2016-11-31', '2019-09-31', '2015-02-31', '2017-04-31', '2015-11-31', '2015-09-31', '2017-02-29', '2018-09-31', '2017-06-31', '2018-04-31', '2015-04-31', '2018-11-31', '2017-09-31', '2015-02-29', '2019-02-29', '2019-06-31', '2018-02-29', '2016-02-30', '2016-06-31', '2016-09-31', '2018-06-31', '2019-18-03'], 
                          ['2019-04-30', '2016-11-30', '2019-09-30', '2015-02-28', '2017-04-30', '2015-11-30', '2015-09-30', '2017-02-28', '2018-09-30', '2017-06-30', '2018-04-30', '2015-04-30', '2018-11-30', '2017-09-30', '2015-02-28', '2019-02-28', '2019-06-30', '2018-02-28', '2016-02-28', '2016-06-30', '2016-09-30', '2018-06-30', '2019-03-18'])



"""
CLEAR PRODUCT CATEGORIES
if product name and brand are the same then take all categories together and create one long list separated by comma
"""


dataset_products = dataset[['product_name', 'product_brand', 'product_category', 
                   'product_code', 'product_series', 'product_part_number', 
                   'business']]    

#ioSmart = dataset[dataset['product_name'] == 'ioSmart']

dataset_products = dataset_products.drop_duplicates()


## GROUP BY THE SAME NAME + BRAND AND CREATE LONG CATEGORY LIST 
dataset_cat = dataset_products.groupby(['product_name','product_brand'], as_index=False).agg(', '.join)
dataset_cat['product_category_long'] = dataset_cat['product_category'].apply(lambda x: unique_elements(x)) 

dataset_cat = dataset_cat[['product_name','product_brand','product_category_long']]


dataset_products = dataset_products.merge(dataset_cat, how = "left", on = ['product_name','product_brand'])


dataset_products['product_category'] = dataset_products['product_category_long']
dataset_products = dataset_products.drop(['product_category_long'], axis=1)

dataset_products = dataset_products.drop_duplicates()


"""
CLEAN PRODUCT SERIES
"""

## GROUP BY THE SAME NAME + BRAND AND CREATE LONG CATEGORY LIST 
dataset_series = dataset_products.groupby(['product_name','product_brand', 'product_category'], as_index=False).agg(', '.join)
dataset_series['product_series_long'] = dataset_series['product_series'].apply(lambda x: unique_elements(x)) 

dataset_series = dataset_series[['product_name','product_brand','product_category', 'product_series_long']]


dataset_products = dataset_products.merge(dataset_series, how = "left", on = ['product_name','product_brand','product_category'])


dataset_products['product_series'] = dataset_products['product_series_long']
dataset_products = dataset_products.drop(['product_series_long'], axis=1)

dataset_products = dataset_products.drop_duplicates()



"""
SORT PRODUCT CODES
"""

dataset_products['product_code'] = dataset_products['product_code'].apply(lambda x: sort_list(x))

## GROUP BY THE SAME NAME + BRAND AND CREATE LONG CATEGORY LIST 
dataset_codes = dataset_products.groupby(['product_name','product_brand', 'product_category'], as_index=False).agg(', '.join)
dataset_codes['product_code_long'] = dataset_codes['product_code'].apply(lambda x: unique_elements(x))

dataset_codes = dataset_codes[['product_name','product_brand','product_category', 'product_code_long']]

dataset_products = dataset_products.merge(dataset_codes, how = "left", on = ['product_name','product_brand','product_category'])

dataset_products['product_code'] = dataset_products['product_code_long']
dataset_products = dataset_products.drop(['product_code_long'], axis=1)

dataset_products = dataset_products.drop_duplicates()



"""
CREATING UNIQUE IDENTIFIER FOR ALL PRODUCTS
merge last element of each column to a code
"""
def first_letters(string):
    str_length = str(len(string))
    first = string[0]
    last = string[-1]
    return first + last
    
    
#    lst = str(string).split(',')
#    firsts = []
#    for element in lst:
#        element = element.strip()
#        firsts.append(element[0])
#    first_string = "".join(firsts)
#    return first_string  



asd = first_letters("CREATING, UNIQUE, IDENTIFIER, FOR, ALL, PRODUCTS")
        

#dataset_products['product_category_id'] = dataset_products['product_category'].str.split(', ').str[-1]
#dataset_products['product_code_id'] = dataset_products['product_code'].str.split(', ').str[-1]
#dataset_products['product_series_id'] = dataset_products['product_series'].str.split(', ').str[-1]
#dataset_products['product_part_number_id'] = dataset_products['product_part_number'].str.split(', ').str[-1]
#dataset_products['product_business_id'] = dataset_products['business'].str.split(', ').str[-1]

dataset_products['product_name_first'] = dataset_products['product_name'].str.split(',').str[0]
dataset_products['product_name_id'] = dataset_products['product_name'].apply(lambda x: first_letters(str(x)))
dataset_products['product_brand_id'] = dataset_products['product_brand'].str[:3]
dataset_products['product_category_id'] = dataset_products['product_category'].apply(lambda x: first_letters(str(x)))
dataset_products['product_code_id'] = dataset_products['product_code'].apply(lambda x: first_letters(str(x)))
dataset_products['product_code_last'] = dataset_products['product_code'].str.split(',').str[-1]
dataset_products['product_series_id'] = dataset_products['product_series'].apply(lambda x: first_letters(str(x)))
dataset_products['product_part_number_id'] = dataset_products['product_part_number'].apply(lambda x: first_letters(str(x)))
dataset_products['product_business_id'] = dataset_products['business'].apply(lambda x: first_letters(str(x)))


dataset_products['product_identifier'] = dataset_products['product_name_first'] + "-" + dataset_products['product_brand_id'] +  "-" + dataset_products['product_code_last']  + "-" + dataset_products['product_series_id'] + "-" + dataset_products['product_part_number'] + dataset_products['product_business_id']            

dataset_products['product_identifier'] = dataset_products['product_identifier'].str.replace('Not Specified', 'na')


identifier_unique = list(dataset_products['product_identifier'].unique())


dataset_products = dataset_products[['product_name', 'product_brand', 'product_category', 
                   'product_code', 'product_series', 'product_part_number', 
                   'business', 'product_identifier']]    

dataset_products['xxx'] = dataset_products.duplicated(['product_identifier'])
dataset_products = dataset_products.drop_duplicates()

erratic = dataset_products[dataset_products['xxx'] == True]
bulb = dataset[dataset['product_name'] == 'A19 Remote Bulb Control']

"""
PRODUCTS DATASET
"""
       



dataset_products = dataset_products.drop_duplicates()

products_unique = list(dataset['product_name'].unique())

dataset_products.to_csv("dataset_products.csv",  encoding='utf-8-sig', index=False)



"""
DOCUMENTS DATASET
"""

dataset_documents = dataset[['document_title', 'document_number', 'document_version', 
                   'document_revision', 'document_type', 'document_created_at', 
                   'document_last_edition', 'document_last_publication', 
                   'document_revised_modified', 'document_link', 'maps_link', 
                   'product_name']]

#dataset_documents = dataset_documents.iloc[:100, :]

dataset_documents = dataset_documents.drop_duplicates()
dataset_documents.to_csv("dataset_documents.csv",  encoding='utf-8-sig', index=False)



"""
TOPICS DATASET
"""

dataset_topics = dataset[['topic_title','document_title', 'document_number', 'document_last_edition']]
dataset_topics = dataset_topics[dataset_topics['topic_title'] != dataset_topics['document_title']]


dataset_topics = dataset_topics.drop_duplicates()
dataset_topics.to_csv("dataset_topics.csv",  encoding='utf-8-sig', index=False)





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
 




