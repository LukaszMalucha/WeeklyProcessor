# -*- coding: utf-8 -*-
"""
Created on Tue Feb 18 17:42:50 2020

@author: jmalucl
"""


import numpy as np
import dateutil.parser
import itertools

def unify_date_format(date):
    """Helper function that turns dates into correct format"""
    if type(date) == str:
        try:
            date = dateutil.parser.parse(date)   
        except:
            pass
    return date  


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



def date_cleaner(dataset):
    
    
    """
    Rename column according to convention
    """
    dataset['document_last_edition'] = dataset['meta_lastEdition']
    dataset = dataset.drop(['meta_lastEdition'], axis=1)
    
    
    """
    Get column to correct date format
    """
    dataset['document_last_edition'] = dataset['document_last_edition'].apply(lambda x: str(unify_date_format(x))[:10])  
    
        
    """
    meta_lastPublication renaming
    """
    dataset['document_last_publication'] = dataset['meta_lastPublication']
    dataset = dataset.drop(['meta_lastPublication'], axis=1)

    # DROP HOURS/M/S
    dataset['document_last_publication'] = dataset['document_last_publication'].apply(lambda x: str(unify_date_format(x))[:10])  
    
    
    # META CREATED DATE
    dataset['meta_created_date'] = dataset['meta_created_date'].str.replace('_', '-')
    dataset['meta_created_date'] = dataset['meta_created_date'].apply(lambda x: str(unify_date_format(x))[:10])
    dataset['document_created_at'] = dataset['meta_created_date']
    dataset = dataset.drop(['meta_created_date'], axis=1)

    # META_REVISED_MODIFIED
    dataset['document_revised_modified'] = dataset['meta_revised_modified']
    dataset = dataset.drop(['meta_revised_modified'], axis=1) 
    
    
    date_column_list = ['document_created_at','document_last_edition', 'document_last_publication', 'document_revised_modified']
    
    """
    
    THE PLAN IS TO FIRST REPLACE EMPTY SPOTS IN META_CREATED_DATE WITH CREATED_AT
    THEN WE DROP CREATED_AT
    THEN WE REPLACE EMPTY SPOTS IN OTHER COLUMNS WITH document_created_at
    """ 
   
    dataset[date_column_list] = dataset[date_column_list].replace('Not Specified', np.nan)
    dataset[date_column_list] = dataset[date_column_list].replace('Not Specif', np.nan)
    dataset[date_column_list] = dataset[date_column_list].replace('nan', np.nan)   
    dataset['document_created_at'].fillna(dataset['created_at'], inplace=True)   
    dataset = dataset.drop(['created_at'], axis=1)
    
    dataset['document_last_edition'].fillna(dataset['document_created_at'], inplace=True)
    dataset['document_last_publication'].fillna(dataset['document_created_at'], inplace=True)
    dataset['document_revised_modified'].fillna(dataset['document_created_at'], inplace=True)
    
    

    
    """
    FIXING NON-EXISTING DATES IN DATASET
    """
    
    dataset = dataset.replace(['2020-1-29'], ['2020-01-29'])
    
    
    
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
    
    
    
    
    # Non-existing dates from the list
    dataset = dataset.replace(['2019-04-31', '2016-11-31', '2019-09-31', '2015-02-31', '2017-04-31', '2015-11-31', '2015-09-31', '2017-02-29', '2018-09-31', '2017-06-31', '2018-04-31', '2015-04-31', '2018-11-31', '2017-09-31', '2015-02-29', '2019-02-29', '2019-06-31', '2018-02-29', '2016-02-30', '2016-06-31', '2016-09-31', '2018-06-31', '2019-18-03', '2020-02-31', '9999-12-31'], 
                              ['2019-04-30', '2016-11-30', '2019-09-30', '2015-02-28', '2017-04-30', '2015-11-30', '2015-09-30', '2017-02-28', '2018-09-30', '2017-06-30', '2018-04-30', '2015-04-30', '2018-11-30', '2017-09-30', '2015-02-28', '2019-02-28', '2019-06-30', '2018-02-28', '2016-02-28', '2016-06-30', '2016-09-30', '2018-06-30', '2019-03-18', '2020-02-28', '1999-12-31'])


    
    


    return dataset
    
    
      


    



