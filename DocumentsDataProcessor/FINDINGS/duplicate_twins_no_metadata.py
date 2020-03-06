# -*- coding: utf-8 -*-
"""
Created on Fri Mar  6 11:35:58 2020

@author: jmalucl
"""

import pandas as pd

dataset = pd.read_csv("documents_unique_id.csv", encoding='utf-8-sig')



dataset_documents = dataset[['topic_title','document_title', 'document_number', 'document_part_number', 'document_version', 
                   'document_revision', 'document_type', 'document_created_at',
                   'document_last_edition', 'document_last_publication', 
                   'document_revised_modified', 'document_link', 'maps_link', 
                   'product_identifier']]




# Doc Number + docum

dataset_documents = dataset_documents[dataset_documents['topic_title'] == dataset_documents['document_title']]
dataset_documents = dataset_documents.drop_duplicates()
dataset_documents = dataset_documents[~dataset_documents['document_title'].str.contains('miramo')]
dataset_documents = dataset_documents[~dataset_documents['document_title'].str.contains('.fm')]
dataset_documents = dataset_documents[~dataset_documents['document_title'].str.contains('.pdf')]
dataset_documents = dataset_documents[~dataset_documents['document_title'].str.contains('yki')]
dataset_documents = dataset_documents[~dataset_documents['document_title'].str.contains('untitled')]

erratic = dataset_documents[dataset_documents['document_number'] == "Not Specified"]
erratic_2 = erratic[erratic['document_part_number'] == "Not Specified"]


dataset_documents = dataset_documents.drop(['topic_title'], axis=1)


duplicates = dataset_documents[dataset_documents.duplicated(['document_title'], keep=False)]

duplicates2 = duplicates[duplicates['document_number'] == "Not Specified"]
duplicates3 = duplicates2[duplicates2['document_part_number'] == "Not Specified"]









duplicates = duplicates3[['document_title', 'document_link']]
duplicates['document_link'] = "https://johnsoncontrols.fluidtopics.net" + duplicates['document_link']
duplicates.to_csv('duplicate_titles.csv',  encoding='utf-8-sig', index=False)
#
#dataset_documents = dataset_documents.drop_duplicates()














