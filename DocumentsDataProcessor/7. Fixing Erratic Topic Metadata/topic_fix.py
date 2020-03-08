# -*- coding: utf-8 -*-
"""
Created on Sun Mar  8 14:27:23 2020

@author: LukaszMalucha
"""

import pandas as pd
import numpy as np


def fix_metadata(df):
    """
    FUNCTION THAT REAPPLIES CORRECT METADATA FROM DOCUMNET ROOT TO THE
    WHOLE FAMILY OF RELATED TOPICS
    """
    
    # LIST OF TUPLES WITH CRITICAL TOPIC TITLE + LINK
    df['tuple'] = list(list(zip(df.topic_title, df.document_link, df.breadcrumb)))    
    tuple_list = df['tuple'].tolist()    
    df = df.drop(['tuple'], axis=1)    
    
    # GET PARENT DOCUMENT, WHERE DOC TITLE == TOPIC TITLE
    parent = df[df['document_title'] == df['topic_title']]
    try:
        parent_list = parent.to_numpy().tolist()
    
        merged_list = []
        
        for element in tuple_list:
            merged_list.append([element, parent_list]) 
        
    
        new_data_list = []
    
        # RECREATE FIXED ROWS INTO LIST OF LISTS
        for element in merged_list:
            new_data_list.append([element[0][0], element[1][0][1], element[1][0][2], 
                         element[1][0][3], element[1][0][4],  element[1][0][5],
                         element[1][0][6], element[1][0][7],  element[1][0][8],
                         element[1][0][9], element[1][0][10],  element[1][0][11],
                         element[0][1], element[1][0][13], element[1][0][14],  
                         element[1][0][15], element[1][0][16],  element[1][0][17],
                         element[1][0][18], element[0][2],  element[1][0][20], element[1][0][21], 
                         element[1][0][22], "asd"
                         ])

    
    
        df = df.iloc[0:0]   
        new_df = df.append(pd.DataFrame(new_data_list, columns=df.columns))  
    
        return new_df
    
    except:        
        return df



def fix_topics(filename):

    dataset = pd.read_csv(filename, encoding='utf-8-sig')


    """
    MANUAL FIX
    """
    # exacq
    dataset['document_version'] = np.where(dataset['document_link'].str.contains("/reader/vCp6cjnJB7AdOe279US~Ow"), "19.3", dataset['document_version'])



    exacq_1904 = {'topic_title':'exacqVision Client User Manual', 
                  'document_title': 'exacqVision Client User Manual',
                  'document_number': 'ygd1549486126810',
                  'document_part_number': 'ygd1549486126810',
                  'document_version': '9.4',
                  'document_revision': 'Not Specified',
                  'document_type': 'User Guide',
                  'document_lang': 'Not Specified',
                  'document_created_at': '2018-06-15',
                  'document_last_edition': '2019-06-24',
                  'document_last_publication': '2019-06-24',
                  'document_revised_modified': '2018-06-15',
                  'document_link': '/reader/I9sxqp4DRaTFWlaRAPwqTQ/root',
                  'brand': 'Exacq',
                  'product_category': 'VMS Software',
                  'product_code': 'Not Specified',
                  'product_series': 'Not Specified',
                  'business': 'Not Specified',
                  'maps_link': 'https://johnsoncontrols.fluidtopics.net/api/khub/maps/I9sxqp4DRaTFWlaRAPwqTQ',
                  'breadcrumb': 'Not Specified',
                  'product_name': 'exacqVision Professional and Enterprise',                           
                  'product_identifier': 'eed9c6c25022273917e24a26159371e5438bec12',
                  'document_identifier': 'b9bd97eec39e8d9aaa550b13a3eee90303f5c481',
                  }
    
    
    dataset = dataset.append(exacq_1904, ignore_index=True)



    # Johnson Controls Enterprise Management: Hardware Installation Guide 2.2
    
    
    jc22 = {'topic_title':'Johnson Controls Enterprise Management: Hardware Installation Guide', 
              'document_title': 'Johnson Controls Enterprise Management: Hardware Installation Guide',
              'document_number': 'LIT-12012431',
              'document_part_number': 'LIT-12012431',
              'document_version': '2.2',
              'document_revision': 'Not Specified',
              'document_type': 'Installation Guide',
              'document_lang': 'Not Specified',
              'document_created_at': '2018-12-11',
              'document_last_edition': '2020-02-28',
              'document_last_publication': '2020-02-28',
              'document_revised_modified': '2020-02-28',
              'document_link': '/reader/EJncpncXUiFvyKgUNmpnyQ/root',
              'brand': 'Johnson Controls',
              'product_category': 'Connected Offerings, Digital Solutions, Software Application',
              'product_code': 'CPN-B1-10M-8, CPN-B1-11M-8, CPN-B1-12M-8, CPN-B1-13M-8, CPN-B1-14M-8, CPN-B1-15M-8, CPN-B1-16M-8, CPN-B1-17M-8, CPN-B1-18M-8, CPN-B1-19M-8, CPN-B1-1M-8, CPN-B1-20M-8, CPN-B1-21M-8, CPN-B1-22M-8, CPN-B1-23M-8, CPN-B1-24M-8, CPN-B1-25M-8, CPN-B1-26M-8, CPN-B1-27M-8, CPN-B1-28M-8, CPN-B1-29M-8, CPN-B1-2M-8, CPN-B1-30M-8, CPN-B1-31M-8, CPN-B1-32M-8, CPN-B1-33M-8, CPN-B1-34M-8, CPN-B1-35M-8, CPN-B1-36M-8, CPN-B1-3M-8, CPN-B1-4M-8, CPN-B1-5M-8, CPN-B1-6M-8, CPN-B1-7M-8, CPN-B1-8M-8, CPN-B1-9M-8, CPN-B1-N-1Y, CPN-B1-N-3Y, CPN-C1-10M-8, CPN-C1-11M-8, CPN-C1-12M-8, CPN-C1-13M-8, CPN-C1-14M-8, CPN-C1-15M-8, CPN-C1-16M-8, CPN-C1-17M-8, CPN-C1-18M-8, CPN-C1-19M-8, CPN-C1-1M-8, CPN-C1-20M-8, CPN-C1-21M-8, CPN-C1-22M-8, CPN-C1-23M-8, CPN-C1-24M-8, CPN-C1-25M-8, CPN-C1-26M-8, CPN-C1-27M-8, CPN-C1-28M-8, CPN-C1-29M-8, CPN-C1-2M-8, CPN-C1-30M-8, CPN-C1-31M-8, CPN-C1-32M-8, CPN-C1-33M-8, CPN-C1-34M-8, CPN-C1-35M-8, CPN-C1-36M-8, CPN-C1-3M-8, CPN-C1-4M-8, CPN-C1-5M-8, CPN-C1-6M-8, CPN-C1-7M-8, CPN-C1-8M-8, CPN-C1-9M-8, CPN-C1-N-1Y, CPN-C1-N-3Y, CPN-C2-10M-8, CPN-C2-11M-8, CPN-C2-12M-8, CPN-C2-13M-8, CPN-C2-14M-8, CPN-C2-15M-8, CPN-C2-16M-8, CPN-C2-17M-8, CPN-C2-18M-8, CPN-C2-19M-8, CPN-C2-1M-8, CPN-C2-20M-8, CPN-C2-21M-8, CPN-C2-22M-8, CPN-C2-23M-8, CPN-C2-24M-8, CPN-C2-25M-8, CPN-C2-26M-8, CPN-C2-27M-8, CPN-C2-28M-8, CPN-C2-29M-8, CPN-C2-2M-8, CPN-C2-30M-8, CPN-C2-31M-8, CPN-C2-32M-8, CPN-C2-33M-8, CPN-C2-34M-8, CPN-C2-35M-8, CPN-C2-36M-8, CPN-C2-3M-8, CPN-C2-4M-8, CPN-C2-5M-8, CPN-C2-6M-8, CPN-C2-7M-8, CPN-C2-8M-8, CPN-C2-9M-8, CPN-C2-N-1Y, CPN-C2-N-3Y, MS-ME-T100250-8, MS-ME-T100500-8, MS-ME-T10100-8, MS-ME-T101000-8, MS-ME-T1025-8, MS-ME-T10250-8, MS-ME-T1050-8, MS-ME-T10500-8, MS-ME-T250500-8, MS-ME-T25100-8, MS-ME-T251000-8, MS-ME-T25250-8, MS-ME-T2550-8, MS-ME-T25500-8, MS-ME-T50100-8, MS-ME-T501000-8, MS-ME-T50250-8, MS-ME-T50500-8, MS-MEM-BH-1Y, MS-MEM-BH-3Y, MS-MEM-BH-B, MS-MEM-BH-B3, MS-MEM-DH-1Y, MS-MEM-DH-3Y, MS-MEM-DH-B, MS-MEM-DH-B3, MS-MEM-E15H-1Y, MS-MEM-E15H-3Y, MS-MEM-E15H-B, MS-MEM-E15H-B3, MS-MEM-E30H-1Y, MS-MEM-E30H-3Y, MS-MEM-E30H-B, MS-MEM-E30H-B3, MS-MEM-EQP-1Y, MS-MEM-EQP-3Y, MS-MEM-HBD-8, MS-MEM-HBE15-8, MS-MEM-HBE30-8, MS-MEM-HBP-8, MS-MEM-HDE15-8, MS-MEM-HDE30-8, MS-MEM-HDP-8, MS-MEM-HE1530-8, MS-MEM-HPE15-8, MS-MEM-HPE30-8, MS-MEM-HWHDC-0, MS-MEM-KIO-1Y, MS-MEM-KIO-3Y, MS-MEM-PH-1Y, MS-MEM-PH-3Y, MS-MEM-PH-B, MS-MEM-PH-B3, MS-MEM-SP-1Y, MS-MEM-SP-3Y, MS-MEM-SP-M, MS-MEM-T10-1Y, MS-MEM-T10-3Y, MS-MEM-T100-1Y, MS-MEM-T100-3Y, MS-MEM-T1000-1Y, MS-MEM-T1000-3Y, MS-MEM-T25-1Y, MS-MEM-T25-3Y, MS-MEM-T250-1Y, MS-MEM-T250-3Y, MS-MEM-T50-1Y, MS-MEM-T50-3Y, MS-MEM-T500-1Y, MS-MEM-T500-3Y',
              'product_series': 'Not Specified',
              'business': 'Building Automation and Controls',
              'maps_link': 'https://johnsoncontrols.fluidtopics.net/api/khub/maps/EJncpncXUiFvyKgUNmpnyQ',
              'breadcrumb': 'Johnson Controls Enterprise Management: Hardware Installation Guide> Configuring data collectors> Configuring an EDMI meter',
              'product_name': 'Johnson Controls Enterprise Management',                           
              'product_identifier': '99481fc08ff8e7e99f643f816ae0ceed73bf5e63',
              'document_identifier': '20e825d45ea0efdb335e0f53944276d9bdd1523e',
                  }
    
    dataset = dataset.append(jc22, ignore_index=True)



    # THIS IS ERRATIC EMPTY ENTRY FOR "Johnson Controls Enterprise Management: Hardware Installation Guide"
    dataset = dataset[~dataset['document_link'].str.contains('/reader/DYKyptCmOh__np3CokBH0w')]
    dataset = dataset[~dataset['document_link'].str.contains('/reader/TcXd997usfEwTQVUI34H_w')]




    
    
    """
    DEFINE WHICH TOPICS HAVE ERRATIC METADATA
    """
    
    dataset_documents = dataset[['topic_title','document_title', 'document_number', 'product_name','document_part_number', 'document_version', 
                       'document_revision', 'document_type', 'document_created_at',
                       'document_last_edition', 'document_last_publication', 
                       'document_revised_modified', 'brand', 'document_link', 'maps_link', 
                       'product_identifier', 'document_identifier']]
    dataset_documents = dataset_documents[dataset_documents['topic_title'] == dataset_documents['document_title']]
    
    dataset_topics = dataset[['topic_title','document_title','document_last_edition', 'document_link', 'breadcrumb', 'document_identifier']]
    dataset_topics = dataset_topics[dataset_topics['topic_title'] != dataset_topics['document_title']]
    
    
    
    # GET THE LIST OF ERRATIC METADATA TOPICS
    unique_documents = list(dataset_documents['document_identifier'].unique())
    unique_topics = list(dataset_topics['document_identifier'].unique())
    missing_id_list = np.setdiff1d(unique_topics,unique_documents, assume_unique=True).tolist()
    
    
    
    # GET LINKS TO DOCUMENTS WITH ERRATIC TOPIC INSIDE
    erratic_documents = dataset[dataset['document_identifier'].isin(missing_id_list)]
    erratic_documents['erratic_link'] = erratic_documents['document_link'].str.split("\/").str[2]
    
    erratic_documents_links_list = list(erratic_documents['erratic_link'].unique())
    
    
    # PREPARE DATASET OF DOCUMENTS TO BE FIXED
    dataset['mid_link'] = dataset['document_link'].str.split("\/").str[2]
    
  
    
    """
    GROUP DATA BY MID LINK AND APPLY CLEANING FUNCTION ON THOSE GROUPS
    """


    fixed_dataset = pd.DataFrame()
    for element in erratic_documents_links_list:
        queryset = dataset[dataset['mid_link'] == element]
        fixed_data = fix_metadata(queryset)
        fixed_dataset = fixed_dataset.append(fixed_data)
    




    complete_documents = dataset[~dataset['mid_link'].isin(erratic_documents_links_list)]
    
    
    complete_documents = complete_documents.append(fixed_dataset)
    complete_documents = complete_documents.drop(['mid_link'], axis=1) 
    
    
    complete_documents.to_csv("documents_fixed_topics.csv",  encoding='utf-8-sig', index=False)


    return complete_documents





data = fix_topics("documents_unique_document_id.csv")






# QUICKCHECK
#data_0 = dataset[dataset['document_title'].str.contains( "Johnson Controls Enterprise Management: Hardware Installation Guide")]
#data_1 = fixed_dataset[fixed_dataset['document_title'].str.contains( "exacqVision Client User Manual")]
#data_2 = dataset[dataset['document_link'].str.contains( "/reader/EJncpncXUiFvyKgUNmpnyQ")]







    
    
    
    
    
    
    
    
    
    