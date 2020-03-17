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




    
dataset = pd.read_csv("9_documents_fixed_topics.csv", encoding='utf-8-sig')


brands = list(dataset['brand'].unique())
unique_products = list(dataset['product_name'].unique())
unique_document_numbers = list(dataset['document_number'].unique())
unique_document_part_numbers = list(dataset['document_part_number'].unique())





"""
FIXING MISSING METADATA
"""





## DOUCMENT PART NUMBER HAVING PARENTHESES
dataset['document_number'] = dataset['document_number'].str.replace("\(\)", "")
dataset['document_part_number'] = dataset['document_part_number'].str.replace("\(\)", "")






# YORK FROM MARCH
dataset['product_name'] = np.where(dataset['product_name'].str.contains(", and YPAL Micro Channel Coil MCHX Cleaning"), "YPAL", dataset['product_name'])
dataset['product_name'] = np.where(dataset['product_name'].str.contains(", and YVAA Chillers QTI Thermistor Sensor Returns"), "YVAA", dataset['product_name'])
dataset['product_name'] = np.where(dataset['product_name'].str.contains("HT/OT & YT Chillers"), "HT, OT, YT Chillers", dataset['product_name'])
dataset['product_name'] = np.where(dataset['product_name'].str.contains("HT/OT and YT Chillers"), "HT, OT, YT Chillers", dataset['product_name'])
dataset['product_name'] = np.where(dataset['product_name'].str.contains("All Single Stage Centrifugal Liquid Chillers"), "Single Stage Centrifugal Liquid Chillers", dataset['product_name'])
dataset['product_name'] = np.where(dataset['product_name'].str.contains('Style “None” and Style “A” Liquid Cooled Solid State Starter LCSSS'), "Style “A” Liquid Cooled Solid State Starter LCSSS", dataset['product_name'])
dataset['product_name'] = np.where(dataset['product_name'].str.contains('OT and YT Chillers'), "OT, YT ", dataset['product_name'])
dataset['product_name'] = np.where(dataset['product_name'].str.contains('Type S Model Absorption Chillers Globe Valve Design Change'), "Type S Model Absorption Chillers", dataset['product_name'])
dataset['product_name'] = np.where(dataset['product_name'].str.contains("Where TXV's are used YCAL / YLAA / YCWS / YCAS / YCWL / YCRL"), "YCAL, YLAA, YCWS, YCAS, YCWL, YCRL", dataset['product_name'])
dataset['product_name'] = np.where(dataset['product_name'].str.contains("YCAS / YCWS"), "YCAS, YCWS", dataset['product_name'])
dataset['product_name'] = np.where(dataset['product_name'].str.contains("YCAL; YCUL; YLAA; YLUA; YCWL; YCRL; Scroll Compressor: Heater"), "YCAL, YCUL, YLAA, YLUA, YCWL, YCRL", dataset['product_name'])
dataset['product_name'] = np.where(dataset['product_name'].str.contains("YCAV - YCIV - YVAA - YVWA"), "YCAV, YCIV, YVAA, YVWA", dataset['product_name'])
dataset['product_name'] = np.where(dataset['product_name'].str.contains("YCAV and YCIV"), "YCAV, YCIV", dataset['product_name'])
dataset['product_name'] = np.where(dataset['product_name'].str.contains("YCIV and YVAA"), "YCIV, YVAA", dataset['product_name'])
dataset['product_name'] = np.where(dataset['product_name'].str.contains("YIA / YPC"), "YIA, YPC", dataset['product_name'])
dataset['product_name'] = np.where(dataset['product_name'].str.contains("YS and YR"), "YS, YR", dataset['product_name'])
dataset['product_name'] = np.where(dataset['product_name'].str.contains("YS and YT"), "YS, YT", dataset['product_name'])
dataset['product_name'] = np.where(dataset['product_name'].str.contains("YST / YK"), "YST, YK", dataset['product_name'])
dataset['product_name'] = np.where(dataset['product_name'].str.contains("YST and CYK"), "YST, CYK", dataset['product_name'])
dataset['product_name'] = np.where(dataset['product_name'].str.contains("YT and YK "), "YT, YK ", dataset['product_name'])
dataset['product_name'] = np.where(dataset['product_name'].str.contains("YT/HT/OT"), "YT, HT, OT", dataset['product_name'])
dataset['product_name'] = np.where(dataset['product_name'].str.contains("YVAA, YLAA, and YCAL"), "YVAA, YLAA, YCAL", dataset['product_name'])
dataset['product_name'] = np.where(dataset['product_name'].str.contains("YVWA and YVAA"), "YVWA, YVAA", dataset['product_name'])
dataset['product_name'] = np.where(dataset['product_name'].str.contains("YK, CYK, YKEP, YST, and YD"), "YK, CYK, YKEP, YST, YD", dataset['product_name'])

dataset['product_name'] = np.where(dataset['product_name'].str.contains("YVWA "), "YVWA", dataset['product_name'])
dataset['product_name'] = np.where(dataset['product_name'].str.contains("YIA"), "YIA Absorption Chillers", dataset['product_name'])
dataset['product_name'] = np.where(dataset['product_name'].str.contains("YMC2 Mod B Correction"), "YMC2 Mod B", dataset['product_name'])
dataset['product_name'] = np.where(dataset['product_name'].str.contains("YPC"), "YPC Absorption Chillers", dataset['product_name'])
dataset['product_name'] = np.where(dataset['product_name'].str.contains("YR "), "YR Chillers", dataset['product_name'])
dataset['product_name'] = np.where(dataset['product_name'].str.contains("YS "), "YR Chillers", dataset['product_name'])
dataset['product_name'] = np.where(dataset['product_name'].str.contains("OM and YST Chillers"), "OM, YST", dataset['product_name'])

# OTHER FIX

dataset['product_name'] = np.where(dataset['product_name'].str.contains("AMB-2010 and AMB -1100 Anti-theft System Deactivator"), "AMB-2010  Anti-theft System Deactivator, AMB-1100 Anti-theft System Deactivator", dataset['product_name'])
dataset['product_name'] = np.where(dataset['product_name'].str.contains("YS "), "YR Chillers", dataset['product_name'])








error = dataset[dataset['document_title'].str.contains("All Single Stage")]







