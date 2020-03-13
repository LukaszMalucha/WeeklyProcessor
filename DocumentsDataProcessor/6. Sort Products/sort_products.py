# -*- coding: utf-8 -*-
"""
Created on Fri Mar 13 17:13:35 2020

@author: LukaszMalucha
"""


import pandas as pd
import numpy as np




def clean_products_splitter(filename):
    """
    SORTING PRODUCT NAMES BEFORE CREATING ID
    """
    

    dataset = pd.read_csv(filename, encoding='utf-8-sig')
    
    dataset = dataset.drop_duplicates()
    
    
    """
    UNIFY AND SIMPLIFY PRODUCT NAMES
    """
    
    # GET ALL LISTS FIRST
    dataset['product_name'] = dataset['product_name'].str.replace(" & ", " and ")
    dataset['product_name'] = dataset['product_name'].str.replace("Turbomaster", "TurboMaster")
    dataset['product_name'] = dataset['product_name'].str.replace(" - Listings and Approvals", "")
    dataset['product_name'] = dataset['product_name'].str.replace(" Trouble Shooting Chart", "")
    dataset['product_name'] = dataset['product_name'].str.replace(" Trouble", "")
    dataset['product_name'] = dataset['product_name'].str.replace("Imersion", "Immersion")
    dataset['product_name'] = dataset['product_name'].str.replace("Line‐Voltage", "Line Voltage")
    dataset['product_name'] = dataset['product_name'].str.replace("Thermostsat", "Thermostat")
    dataset['product_name'] = dataset['product_name'].str.replace("TRUERH", "TrueRH")
    dataset['product_name'] = dataset['product_name'].str.replace("™", "")
    dataset['product_name'] = dataset['product_name'].str.replace("Gas-Engine-Drive", "Gas Engine Drive")
    dataset['product_name'] = dataset['product_name'].str.replace("Centrifugal Chiller", "Centrifugal Liquid Chiller")
    dataset['product_name'] = dataset['product_name'].str.replace("the OptiView", "OptiView")
    dataset['product_name'] = dataset['product_name'].str.replace("®", "")
    
    
    
    # MULTIPLE IN A LIST
    dataset['product_name'] = np.where(dataset['product_name'].str.contains("1/2 or 3/4 Inch NPT 6 ESFR Sprinklers"), "1/2 Inch NPT 6 ESFR Sprinklers, 3/4 Inch NPT 6 ESFR Sprinklers", dataset['product_name'])
    dataset['product_name'] = np.where(dataset['product_name'].str.contains("Chillers with 292/351 and 419/503 VSD Drives - Trap Filter Resistor Wire Routing"), "Chillers with 292/351 & 419/503 VSD Drives Trap Filter Resistor Wire Routing", dataset['product_name'])
    dataset['product_name'] = np.where(dataset['product_name'].str.contains("Metasys System UL 864 10th Edition UUKL/ORD-C100-13 UUKLC Smoke Control System"), "Metasys System UL 864 10th Edition UUKL/ORD-C100-13 UUKLC Standard Smoke Control", dataset['product_name'])
    dataset['product_name'] = np.where(dataset['product_name'].str.contains("Speaker/Visible Notification Appliance with TrueAlert"), "Speaker/Visible Notification Appliances with TrueAlert", dataset['product_name'])
    dataset['product_name'] = np.where(dataset['product_name'].str.contains("F4-CGM General Purpose Application Controllers"), "F4-CGM General Purpose Application Controllers", dataset['product_name'])
    dataset['product_name'] = np.where(dataset['product_name'].str.contains("YCAL and YCUL Style A Chillers Piping Replacement"), "YCAL Style A Chillers Piping Replacement, YCUL Style A Chillers Piping Replacement", dataset['product_name'])
    dataset['product_name'] = np.where(dataset['product_name'].str.contains("YCAL/YCUL Chillers Using Copeland Scroll Compressors"), "YCAL Chillers Using Copeland Scroll Compressors, YCUL Chillers Using Copeland Scroll Compressors", dataset['product_name'])
    dataset['product_name'] = np.where(dataset['product_name'].str.contains("YD, YK, YB, YG, YST, YS, YR, YT"), "YD Centrifugal Liquid Chillers, YK Centrifugal Liquid Chillers, YB Centrifugal Liquid Chillers, YG Centrifugal Liquid Chillers, YST Centrifugal Liquid Chillers, YS Centrifugal Liquid Chillers, YR Centrifugal Liquid Chillers, YT Centrifugal Liquid Chillers", dataset['product_name'])
    
    
    # YB FIX
    dataset['product_name'] = np.where(dataset['document_link'] == "/viewer/document/HiNK6l4VBWjJRlXV6832Fg", "MicroComputer Control Center", dataset['product_name'])
    dataset['product_name'] = np.where(dataset['document_link'] == "/viewer/document/7lxnU2jU52bhl0hD8F02YA", "YB Design Level A Field Connections Microcomputer Control Center", dataset['product_name'])
    dataset['product_name'] = np.where(dataset['document_link'] == "/viewer/document/RY7sHgddCKj1lgMLLjbQ7g", "YB Design Level A Field Control Modifications Diagram Microcomputer Control Center", dataset['product_name'])
    dataset['product_name'] = np.where(dataset['document_link'] == "/viewer/document/7u_6Od2UnqkxSqVO_wADzA", "YB Design Level A Millennium Gas-Engine-Drive Chillers", dataset['product_name'])
    dataset['product_name'] = np.where(dataset['document_link'] == "/viewer/document/yCbTCYz2lF7ewGzhk~YGng", "YB Design Level A Millennium Gas-Engine-Drive Chillers MicroComputer Control Center 371-01469-000, Control Panel", dataset['product_name'])
    dataset['product_name'] = np.where(dataset['document_link'] == "/viewer/document/DNrYv_JqmOoJlN~xNIgSXw", "YB Design Level A Millennium Gas-Engine-Drive Chillers", dataset['product_name'])
    dataset['product_name'] = np.where(dataset['document_link'] == "/viewer/document/DNrYv_JqmOoJlN~xNIgSXw", "YB Design Level A Wiring Diagram Microcomputer Control Center", dataset['product_name'])
    dataset['product_name'] = np.where(dataset['document_link'] == "/viewer/document/kJRJ3V1JCifOZWLocxORKQ", "YB Design Level A Millennium Gas-Engine-Drive Chillers", dataset['product_name'])
    dataset['product_name'] = np.where(dataset['document_link'] == "/viewer/document/6oC3oIr9_6mVOVY5~86KZw", "YB Design Level A Millennium Gas-Engine-Drive Chillers", dataset['product_name'])
    dataset['product_name'] = np.where(dataset['document_link'] == "/viewer/document/nK5Erc53vXIoy8bVvat_wQ", "YB Style A Millennium Gas Engine Drive Chiller, YG Style A Millennium Gas Engine Drive Chiller", dataset['product_name'])
    dataset['product_name'] = np.where(dataset['document_link'] == "/viewer/document/mr~dEWMlqLZjA1MYTCLdzQ", "YB Style A Millennium Gas Engine Drive Chiller System Status Printers, YG Style A Millennium Gas Engine Drive Chiller System Status Printers", dataset['product_name'])
    dataset['product_name'] = np.where(dataset['document_link'] == "/viewer/document/J3VpswGdTD4C1jK~RHptnQ", "YB Style B Flexlogix Control Center Gas Engine Liquid Chiller Control Panel, YG Style B Flexlogix Control Center Gas Engine Liquid Chiller Control Panel", dataset['product_name'])
    dataset['product_name'] = np.where(dataset['document_link'] == "/viewer/document/SQ~7ugoT~l4NqVg85xJ~VQ", "YD, YK, YB, YG, YST, YS, YR, YT", dataset['product_name'])
    dataset['product_name'] = np.where(dataset['document_link'] == "/viewer/document/1PRW3hsZTn9wCIjusRw1QQ", "YG Style A Millennium Centrifugal Liquid Chillers, YB Style A Millennium Centrifugal Liquid Chillers", dataset['product_name'])
    dataset['product_name'] = np.where(dataset['document_link'] == "/viewer/document/_qLr3eBTJvuf8PszgL6yvg", "YK Centrifugal Liquid Chillers, YD Centrifugal Liquid Chillers, YR Centrifugal Liquid Chillers, YB Centrifugal Liquid Chillers, YG Centrifugal Liquid Chillers", dataset['product_name'])
    dataset['product_name'] = np.where(dataset['document_link'] == "/viewer/document/vPV38hKdWIdnM482qAweRQ", "Model YC Styles A thru D Internally Compounded Compressor Units", dataset['product_name'])
    dataset['product_name'] = np.where(dataset['document_link'] == "/viewer/document/IJeX0VyW1lRGsQE259LMFQ", "R Series - Compressor Units", dataset['product_name'])
    dataset['product_name'] = np.where(dataset['document_link'] == "/viewer/document/VoCgTeQYx2skajELwlKgkg", "2-5/8 Bore V/W Compressors", dataset['product_name'])
    
    
    
    ############ SPLIT  ###############
    dataset['product_name'] = dataset['product_name'].apply(lambda x: x.split(',')) 
    product_name_column = dataset.apply(lambda x: pd.Series(x['product_name']), axis=1).stack().reset_index(level=1, drop=True)
    product_name_column.name = 'product_name'
    dataset = dataset.drop('product_name', axis=1).join(product_name_column)
    dataset['product_name'] = pd.Series(dataset['product_name'], dtype=object)
    
    
    
    # SINGLE
    dataset['product_name'] = np.where(dataset['product_name'] == "OM Compressor", "OM Centrifugal Compressor", dataset['product_name'])
    dataset['product_name'] = np.where(dataset['product_name'] == "OT", "OT Open Turbopak Centrifugal Liquid Chillers", dataset['product_name'])
    dataset['product_name'] = np.where(dataset['product_name'] == "P1000 Series Pressure Independent Valve", "P1000 Series Pressure Independent Valves", dataset['product_name'])
    dataset['product_name'] = np.where(dataset['product_name'] == "PCA", "PCA Control Panel", dataset['product_name'])
    dataset['product_name'] = np.where(dataset['product_name'] == "PCG", "PCG Control Panel", dataset['product_name'])
    dataset['product_name'] = np.where(dataset['product_name'] == "PCX", "PCX Control Panel", dataset['product_name'])
    dataset['product_name'] = np.where(dataset['product_name'] == "SAPPHIRE", "SAPPHIRE Fire Suppression Systems", dataset['product_name'])
    dataset['product_name'] = np.where(dataset['product_name'] == "YB", "YB Style A Millennium Gas-Engine-Drive Chiller", dataset['product_name'])
    dataset['product_name'] = np.where(dataset['product_name'] == "YK", "YK Centrifugal Liquid Chillers", dataset['product_name'])
    dataset['product_name'] = np.where(dataset['product_name'] == "YK Centrifugal Chillers -", "YK Centrifugal Liquid Chillers", dataset['product_name'])
    dataset['product_name'] = np.where(dataset['product_name'] == "YK Chiller", "YK Centrifugal Liquid Chillers", dataset['product_name'])
    dataset['product_name'] = np.where(dataset['product_name'] == "CD15-28", "CD15 - CD28", dataset['product_name'])
    dataset['product_name'] = np.where(dataset['product_name'] == "DC090-150", "DC090 - DC150", dataset['product_name'])
    dataset['product_name'] = np.where(dataset['product_name'] == "DC090 - DC150", "DC090 - DC150", dataset['product_name'])
    dataset['product_name'] = np.where(dataset['product_name'] == "PC090 - 240", "PC090 - PC240", dataset['product_name'])
    dataset['product_name'] = np.where(dataset['product_name'] == "PD180 - 240", "PD180 - PD240", dataset['product_name'])
    dataset['product_name'] = np.where(dataset['product_name'] == "T-3000", "T-3100 Thermostat", dataset['product_name'])
    dataset['product_name'] = np.where(dataset['product_name'] == "T-3111", "T-3111 Thermostat", dataset['product_name'])
    dataset['product_name'] = np.where(dataset['product_name'] == "T-3102", "T-3102 Heating Cooling Deadband Thermostat", dataset['product_name'])
    dataset['product_name'] = np.where(dataset['product_name'] == "T-5312", "T-5312 Receiver-Controller", dataset['product_name'])
    dataset['product_name'] = np.where(dataset['product_name'] == "T2000 Thermostat", "T2000 Fan Coil Thermostat", dataset['product_name'])
    dataset['product_name'] = np.where(dataset['product_name'] == "T2000", "T2000 Fan Coil Thermostat", dataset['product_name'])
    dataset['product_name'] = np.where(dataset['product_name'] == "YD", "YD Centrifugal Liquid Chillerss", dataset['product_name'])
    
    
    
    # PROBLEMATIC
    dataset['product_name'] = np.where(dataset['document_link'] == "/viewer/document/vPV38hKdWIdnM482qAweRQ", "Reciprocating Compressors", dataset['product_name'])
    dataset['product_name'] = np.where(dataset['document_link'] == "/viewer/document/tRBtrRbkMuIu7xa1f~OWvA", "Model YC Styles A thru D Internally Compounded Compressor Units", dataset['product_name'])
    dataset['product_name'] = np.where(dataset['document_link'] == "/viewer/document/IJeX0VyW1lRGsQE259LMFQ", "R Series - Compressor Units", dataset['product_name'])
    dataset['product_name'] = np.where(dataset['document_link'] == "/viewer/document/6gp0iUEo7CJAwoNj3RhjJg", "YK Medium Voltage Variable Speed Drive", dataset['product_name'])
    dataset['product_name'] = np.where(dataset['document_link'] == "/viewer/document/SZCWEgCoCZ1DPZEBnMVR~Q", "Millennium Variable Speed Drive, CF-CN, 5CC-5CI, with Optional Harmonic Filter", dataset['product_name'])
    dataset['product_name'] = np.where(dataset['product_name'] == '"B" and "C" All Mod Levels', "HT/OT & YT Chillers W/Air-Cooled SSS Mod", dataset['product_name'])
    dataset['product_name'] = np.where(dataset['product_name'] == "-22 and 502", "Types H and F Series", dataset['product_name'])
    
    
    # CHILLER/CHILLERS FIX
    
    dataset['product_name'] = dataset['product_name'].str.replace("Chillerss", "Chiller")
    dataset['product_name'] = dataset['product_name'].str.replace("Chillers", "Chiller")
    dataset['product_name'] = dataset['product_name'].str.replace("Chiller", "Chillers")
    
    
    
    dataset['product_name'] = dataset['product_name'].str.strip()





    dataset.to_csv("documents_sorted_products.csv",  encoding='utf-8-sig', index=False)
    
    
    return dataset


data = clean_products_splitter("documents_splitted_products.csv")





# CHECK
#unique_products = list(dataset['product_name'].unique())
#c = dataset[dataset['product_name'].str.contains('Chillerss')]   
#c = dataset[dataset['product_name'] == ('Ch')]   
#    
#    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    

