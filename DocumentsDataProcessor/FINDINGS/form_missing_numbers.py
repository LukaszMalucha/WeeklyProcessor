# -*- coding: utf-8 -*-
"""
Created on Fri Mar  6 12:57:01 2020

@author: jmalucl
"""

import pandas as pd
import numpy as np


def get_form_id(string):
    """Get from id from title"""
    if "(Form " in string:
        new_string = string.split("(Form ")[-1]
        new_string = new_string.replace("))", "]")
        new_string = new_string.replace(")", "")
        new_string = new_string.replace("]", ")")
        return new_string
    return string



dataset = pd.read_csv("documents_unique_id.csv", encoding='utf-8-sig')



dataset_documents = dataset[['topic_title','document_title', 'document_number', 'document_part_number', 'document_version', 
                   'document_revision', 'document_type', 'document_created_at',
                   'document_last_edition', 'document_last_publication', 
                   'document_revised_modified', 'document_link', 'maps_link', 
                   'product_identifier']]






dataset_documents = dataset_documents[dataset_documents['document_title'].str.contains("\(Form ")]

dataset_documents['form_number'] = dataset_documents['document_title'].apply(lambda x: get_form_id(x))

dataset_documents['document_number'] = np.where(dataset_documents['document_number'] == "Not Specified", dataset_documents['form_number'], dataset_documents['document_number'])


dataset_forms = dataset_documents[['document_title', 'document_link', 'document_number']]
dataset_forms['document_link'] = "https://johnsoncontrols.fluidtopics.net" + dataset_forms['document_link']


dataset_forms.to_csv('dataset_forms_missing_document_number.csv',  encoding='utf-8-sig', index=False)

