# -*- coding: utf-8 -*-
"""
Created on Fri Mar  6 13:46:33 2020

@author: jmalucl
"""

import pandas as pd
import numpy as np
import re

string2 = "EntraPass Corporate Edition Administration Guide" 

def first_letters(string):
    """First and last letter of a word to create some unique id"""
    string = string.replace("exacqVision-Entrapass", "eV-EP")  
    string = string.replace("exacqVision", "eV")
    string = string.replace("LN Series  ", "LN ")
    string = string.replace("NS Series  ", "NS ")
    string = string.replace("Metasys ", "")
    string = string.replace("CD-W00-x0-2 Series  ", "x0-2 ")
    string = string.replace("CD-Px", "")    
    string = string.replace(" Series Duct Mount CO2 Transmitters ", "")
    string = string.replace("CD-Px0-00-0 Series Duct Mount CO2 Transmitters ", "00-0 ")
    string = string.replace("Language Installation Program", "LIP")
    string = string.replace("EntraPass", "EP")
    
    first = string[:10]    
    ints = [x for x in re.findall('\d+', string)]
    ints = "".join(ints)
    length = str(len(string))
    return first + "-" + str(ints) + "-L" + length


asd = first_letters(string2)

def get_form_id(string):
    """Get from id from title"""
    if "(Form " in string:
        new_string = string.split("(Form ")[-1]
        new_string = new_string.replace("))", "]")
        new_string = new_string.replace(")", "")
        new_string = new_string.replace("]", ")")
        return new_string
    return "Not Specified"



def unique_document_id(filename):
    
    pass


dataset = pd.read_csv("documents_unique_product_id.csv", encoding='utf-8-sig')


dataset = dataset[~dataset['document_title'].str.contains('miramo')]
dataset = dataset[~dataset['document_title'].str.contains('.fm')]
dataset = dataset[~dataset['document_title'].str.contains('.pdf')]
dataset = dataset[~dataset['document_title'].str.contains('yki')]
dataset = dataset[~dataset['document_title'].str.contains('untitled')]

# REMOVE ANSUL TEMPLATE SHEETS

dataset = dataset[~dataset['document_title'].str.contains('ANSUL Instruction Sheet Template__A4_Rev-00')]
dataset = dataset[~dataset['document_title'].str.contains('JCI Data Sheet A4 Template Rev')]
dataset = dataset[~dataset['document_title'].str.contains('JCI datablad A4 mal Rev. 02')]
dataset = dataset[~dataset['document_title'].str.contains('JCI-datablad A4 rev. av mal 02')]
dataset = dataset[dataset['document_title'].str[:] != "Rev. 01"]


"""
THERE ARE FORM DOCUMENTS THAT HAVE NO METADATA BUT FORM ID IN PARETHESES
THAT ID SHOULD BE DOCUMENT NUMBER
"""


dataset['form_number'] = dataset['document_title'].apply(lambda x: get_form_id(x))

dataset['document_number'] = np.where(dataset['document_number'] == "Not Specified", dataset['form_number'], dataset['document_number'])


dataset = dataset.drop(['form_number'], axis=1)



check = dataset[dataset['document_title'] == "PROFILE Panels Installation Guide"]
check = dataset[dataset['document_title'].str.contains("\(Form")]


"""
Metadata fix
""" 

# 4100 OPERATING INSTRUCTIONS

dataset['document_number'] = np.where(dataset['document_link'] == "/viewer/document/cJuUdasllIGtgJOLmXn~Gw", "579-995AC", dataset['document_number'])
dataset['document_revision'] = np.where(dataset['document_link'] == "/viewer/document/cJuUdasllIGtgJOLmXn~Gw", "A", dataset['document_revision'])

dataset['document_number'] = np.where(dataset['document_link'] == "/viewer/document/X3LImsh8GGALyOIxs_~j2w", "579-684AC", dataset['document_number'])
dataset['document_revision'] = np.where(dataset['document_link'] == "/viewer/document/X3LImsh8GGALyOIxs_~j2w", "B", dataset['document_revision'])



# Keep later version of "exacq and KiwiVision Integration"


dataset = dataset.drop(dataset[(dataset['document_title'] == 'exacq and KiwiVision Integration') & (dataset['document_created_at'] == "2016-09-30")].index)



# A4906 Series TrueAlert Addressable Multi-Candela Alert Strobe


dataset['document_number'] = np.where(dataset['document_link'] == "/viewer/document/Zkmqgvq8p_JViZwGGW_xew", "579-828AC", dataset['document_number'])
dataset['document_revision'] = np.where(dataset['document_link'] == "/viewer/document/Zkmqgvq8p_JViZwGGW_xew", "F", dataset['document_revision'])

dataset['document_number'] = np.where(dataset['document_link'] == "/viewer/document/Q5AGlnGuLZWH1vBqUDEIsA", "579-847AC", dataset['document_number'])
dataset['document_revision'] = np.where(dataset['document_link'] == "/viewer/document/Q5AGlnGuLZWH1vBqUDEIsA", "D", dataset['document_revision'])

dataset['document_number'] = np.where(dataset['document_link'] == "/viewer/document/jnfuKop56jBfpPAiMjDVmg", "579-848AC", dataset['document_number'])
dataset['document_revision'] = np.where(dataset['document_link'] == "/viewer/document/jnfuKop56jBfpPAiMjDVmg", "C", dataset['document_revision'])

dataset['document_number'] = np.where(dataset['document_link'] == "/viewer/document/dYj~IYUNNTCdZJNFwhc7cA", "579-808AC", dataset['document_number'])
dataset['document_revision'] = np.where(dataset['document_link'] == "/viewer/document/dYj~IYUNNTCdZJNFwhc7cA", "G", dataset['document_revision'])



# Delete duplicate "Appendix: Installing SQL Server Management Studio Express"
dataset = dataset.drop(dataset[(dataset['document_link'] == '/reader/rKaUaPzNsfYl8765Nx7vEw/root')].index)


# ADS/ADX Commissioning Guide

dataset['document_number'] = np.where(dataset['document_link'] == "/viewer/document/o2UTK2nGaN5qqKlmaBRTfg", "LIT-1201645", dataset['document_number'])
dataset['document_revision'] = np.where(dataset['document_link'] == "/viewer/document/o2UTK2nGaN5qqKlmaBRTfg", "10.0", dataset['document_revision'])


dataset['document_number'] = np.where(dataset['document_link'] == "/viewer/document/pYTBR_R5LBqujsni893h4g", "LIT-1201645", dataset['document_number'])



# Advanced Graphics Application Help


dataset['document_number'] = np.where(dataset['document_link'] == "/viewer/document/3Gb~n3TXhMLjO7Ott8mbVg", "LIT-1201850", dataset['document_number'])
dataset['document_revision'] = np.where(dataset['document_link'] == "/viewer/document/3Gb~n3TXhMLjO7Ott8mbVg", "9.0", dataset['document_revision'])

dataset['document_number'] = np.where(dataset['document_link'] == "/viewer/document/c~DiTrDpN3hQYypZGQqZew", "LIT-1201850", dataset['document_number'])
dataset['document_revision'] = np.where(dataset['document_link'] == "/viewer/document/c~DiTrDpN3hQYypZGQqZew", "10.0", dataset['document_revision'])



# Application Note Rooftop Top Unit (RTU) Controller
dataset['document_number'] = np.where(dataset['document_link'] == "/viewer/document/WhM_LqsTBdNIvliSBeOX7Q", "LIT-12011437", dataset['document_number'])



# REMOVE "CD-WAx-00-2 Installation Instruction 24-10863-9 Rev. A" for other LANGS!!!
dataset = dataset.drop(dataset[(dataset['document_link'] == '/viewer/document/gyreVcACg2afS_FTHo24jw')].index)
dataset = dataset.drop(dataset[(dataset['document_link'] == '/viewer/document/a_gtOrXvsh0leLuVpvOsfA')].index)
dataset = dataset.drop(dataset[(dataset['document_link'] == '/viewer/document/o1t3Dl97k5Oyu~Y746MSWQ')].index)
dataset = dataset.drop(dataset[(dataset['document_link'] == '/viewer/document/9h3XTaaN01bZYin4d~cCwQ')].index)
dataset = dataset.drop(dataset[(dataset['document_link'] == '/viewer/document/gcPLAh1htdMXq65nVu40Hw')].index)
dataset = dataset.drop(dataset[(dataset['document_link'] == '/viewer/document/czott9GLup6o6SOEOe1MNg')].index)
dataset = dataset.drop(dataset[(dataset['document_link'] == '/viewer/document/9LOzy79cqy3fjMBAJA54Iw')].index)
dataset = dataset.drop(dataset[(dataset['document_link'] == '/viewer/document/s0HPE6yURTybzL1IMpVdHw')].index)
dataset = dataset.drop(dataset[(dataset['document_link'] == '/viewer/document/BC2gv2s~UMPbae3zCccZFw')].index)
dataset = dataset.drop(dataset[(dataset['document_link'] == '/viewer/document/EDeFJm~LEzoVuqrNSW69Lg')].index)
dataset = dataset.drop(dataset[(dataset['document_link'] == '/viewer/document/JzuxUNd9kiWI45j5I6JhXQ')].index)

dataset = dataset.drop(dataset[(dataset['document_link'] == '/viewer/document/JzuxUNd9kiWI45j5I6JhXQ')].index)
dataset = dataset.drop(dataset[(dataset['document_link'] == '/viewer/document/xlSYBo~gAQ2acAmDyScFOg')].index)

dataset = dataset.drop(dataset[(dataset['document_link'] == '/viewer/document/wUVS1tY5cKJq9mB_NysFQQ')].index)
dataset = dataset.drop(dataset[(dataset['document_link'] == '/viewer/document/h_X3JnyEGaWuyXVexJrjVg')].index)
dataset = dataset.drop(dataset[(dataset['document_link'] == '/viewer/document/pQg9cxOQyZvN5mLyAawCNQ')].index)
dataset = dataset.drop(dataset[(dataset['document_link'] == '/viewer/document/dy8zcCuhDMjwceMbuI8_SA')].index)
dataset = dataset.drop(dataset[(dataset['document_link'] == '/viewer/document/rKvlNjqRTqkh_kzBlDZhKQ')].index)
dataset = dataset.drop(dataset[(dataset['document_link'] == '/viewer/document/rpIxgxckWQ_J_rXP5X637g')].index)
dataset = dataset.drop(dataset[(dataset['document_link'] == '/viewer/document/eb9BfwazP4e45ZEgni6m3Q')].index)
dataset = dataset.drop(dataset[(dataset['document_link'] == '/viewer/document/DzCMNWDptYP4SnshUTi~YQ')].index)
dataset = dataset.drop(dataset[(dataset['document_link'] == '/viewer/document/T0mgSRBVH~bHmpa5jU4~Dg')].index)
dataset = dataset.drop(dataset[(dataset['document_link'] == '/viewer/document/Rz_YfNYBKDaQrXrnpzxRmA')].index)

dataset = dataset.drop(dataset[(dataset['document_link'] == '/viewer/document/w5fmUwAbr~kNWz8bRnSKwA')].index)
dataset = dataset.drop(dataset[(dataset['document_link'] == '/viewer/document/P9gOsjUlOlD7ohtKnSy4vA')].index)
dataset = dataset.drop(dataset[(dataset['document_link'] == '/viewer/document/VY9xS0cNxMCTSGDT1izBtg')].index)
dataset = dataset.drop(dataset[(dataset['document_link'] == '/viewer/document/KijoZjpV0jno_yXCQ6EO8g')].index)

dataset = dataset.drop(dataset[(dataset['document_link'] == '/viewer/document/ywLyVPAtvCaEQnInmPld1w')].index)
dataset = dataset.drop(dataset[(dataset['document_link'] == '/viewer/document/KijoZjpV0jno_yXCQ6EO8g')].index)

dataset = dataset.drop(dataset[(dataset['document_link'] == '/viewer/document/vXFKRA0AB2dL28hkESUu0A')].index)



## NO METADATA DUPLCIATES VARIOUS

dataset = dataset.drop(dataset[(dataset['document_link'] == '/viewer/document/XUcNsFHov97a7xxWfm8ONw')].index)
dataset = dataset.drop(dataset[(dataset['document_link'] == '/viewer/document/uTqBts88gBilZfRVXtkdsQ')].index)
dataset = dataset.drop(dataset[(dataset['document_link'] == '/viewer/document/~MpE5qAPT96kyCwqRvGgJg')].index)


# Erratic duplicate dates
dataset = dataset.drop(dataset[(dataset['document_link'] == '/viewer/document/6tN_ICW699afn66_yv42fA')  & (dataset['document_created_at'] == "2016-12-01")].index)
dataset = dataset.drop(dataset[(dataset['document_link'] == '/viewer/document/a64m82Bgs0QaLLOI_wmNng')  & (dataset['document_created_at'] == "2016-12-01")].index)
dataset = dataset.drop(dataset[(dataset['document_link'] == '/viewer/document/PIGe3jav7ZDIZJecfZS20g')  & (dataset['document_created_at'] == "2016-12-01")].index)
dataset = dataset.drop(dataset[(dataset['document_link'] == '/viewer/document/LvZmp8qoI5tj02uBP30lPQ')  & (dataset['document_created_at'] == "2017-03-01")].index)
dataset = dataset.drop(dataset[(dataset['document_link'] == '/viewer/document/o21Iwk~HmZSPaJSHyzDb2g')  & (dataset['document_created_at'] == "2017-03-01")].index)
dataset = dataset.drop(dataset[(dataset['document_link'] == '/viewer/document/vhdOwZlLoE9bQg8T_LyWcg')  & (dataset['document_created_at'] == "2017-03-01")].index)
dataset = dataset.drop(dataset[(dataset['document_link'] == '/viewer/document/gVnOZD2k514cbOVITkD_pg')  & (dataset['document_created_at'] == "2017-03-01")].index)
dataset = dataset.drop(dataset[(dataset['document_link'] == '/viewer/document/pxPQPNMck1qQagMP4GfLRw')  & (dataset['document_created_at'] == "2017-10-01")].index)
dataset = dataset.drop(dataset[(dataset['document_link'] == '/viewer/document/UwJE93hrmmiJ2g_udl9g1Q')  & (dataset['document_created_at'] == "2017-10-01")].index)
dataset = dataset.drop(dataset[(dataset['document_link'] == '/viewer/document/rVSYtBSAdmNpVCr0P0_aKA')  & (dataset['document_created_at'] == "2017-10-01")].index)
dataset = dataset.drop(dataset[(dataset['document_link'] == '/viewer/document/hyuHiSdGKOxMkASMYzdz7w')  & (dataset['document_created_at'] == "2017-10-01")].index)
dataset = dataset.drop(dataset[(dataset['document_link'] == '/viewer/document/flEgXHsWsrsiPLtjdILRrg')  & (dataset['document_created_at'] == "2017-10-01")].index)
dataset = dataset.drop(dataset[(dataset['document_link'] == '/viewer/document/6tN_ICW699afn66_yv42fA')  & (dataset['document_created_at'] == "2017-10-01")].index)
dataset = dataset.drop(dataset[(dataset['document_link'] == '/viewer/document/fUb5nW~LKUdJgbjp_LQ6Tg')  & (dataset['document_created_at'] == "2017-03-01")].index)
dataset = dataset.drop(dataset[(dataset['document_link'] == '/viewer/document/_PJPPtIfN4JOYLZmp3GCnA')  & (dataset['document_created_at'] == "2017-03-01")].index)
dataset = dataset.drop(dataset[(dataset['document_link'] == '/viewer/document/lC8Nnzevg04yDafKL1uQag')  & (dataset['document_created_at'] == "2017-10-01")].index)
dataset = dataset.drop(dataset[(dataset['document_link'] == '/viewer/document/m8gzl4IgrycPGN6sqnBLEg')  & (dataset['document_created_at'] == "2017-10-01")].index)
dataset = dataset.drop(dataset[(dataset['document_link'] == '/viewer/document/YHMJtXSivajbg0oYwDtfqw')  & (dataset['document_created_at'] == "2017-10-01")].index)
dataset = dataset.drop(dataset[(dataset['document_link'] == '/viewer/document/m8gzl4IgrycPGN6sqnBLEg')  & (dataset['document_created_at'] == "2018-05-01")].index)
dataset = dataset.drop(dataset[(dataset['document_link'] == '/viewer/document/Nr7gA_ARIPRm~dbP4v1qdw')  & (dataset['document_created_at'] == "2018-05-01")].index)


# CE Declaration of Conformity

dataset['document_title'] = np.where(dataset['document_link'] == "/viewer/document/s2IGEmEL9vCGp9fP3lvWBA", "CE Declaration of Conformity F2A Series", dataset['document_title'])
dataset['document_title'] = np.where(dataset['document_link'] == "/viewer/document/bwUUDHUbXA_~0lkiQx3p7g", "CE Declaration of Conformity R2A Series", dataset['document_title'])
dataset['document_title'] = np.where(dataset['document_link'] == "/viewer/document/GoyDRD5OlVlRDiXBZWJoRA", "CE Declaration of Conformity C-Series 32 Stream", dataset['document_title'])
dataset['document_title'] = np.where(dataset['document_link'] == "/viewer/document/bwUUDHUbXA_~0lkiQx3p7g", "CE Declaration of Conformity C-Series 16 Stream", dataset['document_title'])
dataset['document_title'] = np.where(dataset['document_link'] == "/viewer/document/2ALlbYsit1fwbNS~rI2KkA", "CE Declaration of Conformity C-Series 16 Stream", dataset['document_title'])



# Commercial Comfort System (CCS) Variable Air Volume (VAV) Zone - Pressure Independent Controller Installation Instructions
dataset['document_number'] = np.where(dataset['document_link'] == "/viewer/document/I52yrJGUVoC0oJyITn8ITg", "LIT-12011998-utb-c-0119", dataset['document_number'])
dataset['document_number'] = np.where(dataset['document_link'] == "/viewer/document/TnXGRHL9B774U1M0cX~upQ", "5127912-usd-a-0515", dataset['document_number'])
dataset['document_number'] = np.where(dataset['document_link'] == "/viewer/document/t5za~Zl2OkU_DWzFJEyXOA", "5127914-utg-b-1116", dataset['document_number'])
dataset['document_number'] = np.where(dataset['document_link'] == "/viewer/document/x9Al8Hf_kT8egdIENAw_VQ", "1154578-utg-a-0515", dataset['document_number'])
dataset['document_number'] = np.where(dataset['document_link'] == "/viewer/document/13k0muux3Egoovg94MrhGw", "5127910-usd-a-0515", dataset['document_number'])
dataset['document_number'] = np.where(dataset['document_link'] == "/viewer/document/D4CjC6pfMWgXnB9P6nV0Cw", "1154576-uim-b-0615.pdf", dataset['document_number'])
dataset['document_number'] = np.where(dataset['document_link'] == "/viewer/document/hFNjk1kdFwYBASnWORrPoQ", "LIT-12011998-utb-b-0418", dataset['document_number'])
dataset['document_number'] = np.where(dataset['document_link'] == "/viewer/document/8hYs9r5eZh3D3my9b2l1QA", "5127911-usd-a-0515", dataset['document_number'])


# Duplicate "CD-Px0... Series Duct Mount CO2 Transmitters Product Bulletin" other langs removed
dataset = dataset.drop(dataset[(dataset['document_link'] == '/viewer/document/L_o~SyvhgZNSk3ouppatxQ')].index)
dataset = dataset.drop(dataset[(dataset['document_link'] == '/viewer/document/KdPgJ6d01g05ygYQmTXfAw')].index)
dataset = dataset.drop(dataset[(dataset['document_link'] == '/viewer/document/4sbsQOjnh7DWWZ4XlI4Y9w')].index)
dataset = dataset.drop(dataset[(dataset['document_link'] == '/viewer/document/RhJuaynjc0XRYIwu~S5UAg')].index)
dataset = dataset.drop(dataset[(dataset['document_link'] == '/viewer/document/RhJuaynjc0XRYIwu~S5UAg')].index)
dataset = dataset.drop(dataset[(dataset['document_link'] == '/viewer/document/makQGmBO_ep0uNyqFbTsuQ')].index)
dataset = dataset.drop(dataset[(dataset['document_link'] == '/viewer/document/QyDLYwTz45x2hADAPzsV0A')].index)
dataset = dataset.drop(dataset[(dataset['document_link'] == '/viewer/document/s64o_wTqN6gX7zW55TEraw')].index)
dataset = dataset.drop(dataset[(dataset['document_link'] == '/viewer/document/mnPRnorEE~ejgOE2jWb1vg')].index)
dataset = dataset.drop(dataset[(dataset['document_link'] == '/viewer/document/D9RBHEOi38QEGRcf1k12wQ')].index)
dataset = dataset.drop(dataset[(dataset['document_link'] == '/viewer/document/I0a7BSq7nTpvcgbFw_RQrw')].index)





# CSD Series Current Devices—Solid Core Installation Instructions
dataset['document_number'] = np.where(dataset['document_link'] == "/viewer/document/GXg7sp0Bt8evbNKuv3kTbw", "24-10345-18", dataset['document_number'])
dataset['document_number'] = np.where(dataset['document_link'] == "/viewer/document/HczkbTV7q4EmrGRKXFmU0Q", "24-10345-34", dataset['document_number'])
dataset['document_number'] = np.where(dataset['document_link'] == "/viewer/document/Q1ehUpr_3sSelw5GYeo_5g", "24-10345-42", dataset['document_number'])




# LN SERIES duplicates
dataset = dataset.drop(dataset[(dataset['document_link'] == '/viewer/document/ae0NdKdEkDRsxJ7Lqcv6Kw')].index)
dataset = dataset.drop(dataset[(dataset['document_link'] == '/viewer/document/posLIKe0MRJ1ycidLc0Gwg')].index)
dataset = dataset.drop(dataset[(dataset['document_link'] == '/viewer/document/aGPFAcZtizylqo_vz84NIg')].index)
dataset = dataset.drop(dataset[(dataset['document_link'] == '/viewer/document/ZPVYTOVVv7Ab7uEtgfhSZw')].index)



# Database Tools Commissioning Guide
dataset['document_number'] = np.where(dataset['document_link'] == "/viewer/document/tcE4LMqvBRKT9ASB4tn9hA", "LIT-12012254", dataset['document_number'])
dataset['document_revision'] = np.where(dataset['document_link'] == "/viewer/document/tcE4LMqvBRKT9ASB4tn9hA", "9.0", dataset['document_revision'])

dataset['document_number'] = np.where(dataset['document_link'] == "/viewer/document/2unzhvgE60l7plKKHc7Q2Q", "LIT-12012254", dataset['document_number'])
dataset['document_revision'] = np.where(dataset['document_link'] == "/viewer/document/2unzhvgE60l7plKKHc7Q2Q", "10.0", dataset['document_revision'])



dataset = dataset[['topic_title','document_title', 'document_number', 'document_part_number', 'document_version', 
                   'document_revision', 'document_type', 'document_created_at', 'product_brand',
                   'document_last_edition', 'document_last_publication', 
                   'document_revised_modified', 'document_link', 'maps_link', 
                   'product_identifier']]


"""
IF DOCUMENT PART NUMBER PRESENT AND NO DOCUMENT NUMBER THEN DOCPART BECOMES DOCNUM
IF DOC NUM PRESENT BUT NO DOC PART NUMBER THEN DOCNUM BECOMES DOCPART
"""



dataset['document_number'] = np.where(dataset['document_number'] == "Not Specified", dataset['document_part_number'], dataset['document_number'])
dataset['document_part_number'] = np.where(dataset['document_part_number'] == "Not Specified", dataset['document_number'], dataset['document_part_number'])









"""
DOCUMENT UNIQUE IDENTIFIER
NUMBER OF UNIQUE ID SHOULD BE EQAUL TO NUMBER OF DOCUMENTS
document_title(shortened) + document_number + document_revision
"""

dataset['document_title_id'] = dataset['document_title'].apply(lambda x: first_letters(str(x)))
dataset['document_brand_id'] = dataset['product_brand'].apply(lambda x: x[:3])

dataset['document_identifier'] = dataset['document_title_id'] + "-" + dataset['document_number'] + dataset['document_part_number'] + "-" + dataset['document_version'] + "-" + dataset['document_revision'] + "-" + dataset['document_brand_id']
dataset['document_identifier'] = dataset['document_identifier'].str.replace('Not Specified', 'XX')
dataset['document_identifier'] = dataset['document_identifier'].str.replace(' ', '_')


# COMPARISON CHECK
document_id_unique = list(dataset['document_identifier'].unique())

docs = dataset[dataset['topic_title'] == dataset['document_title']]
docs = docs.drop_duplicates()
#docs = list(dataset['document_identifier'].unique())
docs = docs.drop(['topic_title'], axis=1)

erratic = docs[docs['document_number'] == "Not Specified"]
erratic_2 = erratic[erratic['document_part_number'] == "Not Specified"]


erratic_2['duplicate'] = erratic_2.duplicated(subset=['document_identifier'])
erratic_3 = erratic_2[erratic_2['document_created_at'] == "2017-03-01"]

erratic_true = erratic_2[erratic_2['duplicate'] == True]









# SIMPLIFICATION


#
##dataset_documents = dataset_documents.drop_duplicates()
#
#erratic = dataset_documents[dataset_documents['document_number'] == "Not Specified"]
#erratic_2 = erratic[erratic['document_part_number'] == "Not Specified"]
#
#dataset_documents = dataset_documents.drop(['topic_title'], axis=1)
#
#dataset_documents = dataset_documents.drop_duplicates()
#
#
#
### SPRAWDZIĆ
#
#
#D-4070, Damper Actuator
#
#
#
#




#
#"""
#IF DOCUMENT HAS THE SAME COLUMN VALUES EXCEPT DOCUMENT LINK IT MEANS
#THAT IT WAS SUBMITTED TWICE
#"""
#
#
#dataset_documents = dataset_documents.sort_values('document_title').drop_duplicates(subset=[
#                                                        'document_title', 'document_number', 'document_part_number',
#                                                       'document_revision', 'document_type', 'document_created_at',
#                                                       'document_last_edition', 'document_last_publication', 
#                                                       'document_revised_modified','product_identifier'], keep='last')


