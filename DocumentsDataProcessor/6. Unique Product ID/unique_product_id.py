# -*- coding: utf-8 -*-
"""
Created on Sun Mar  1 18:14:40 2020

@author: LukaszMalucha
"""

import pandas as pd
import numpy as np
import hashlib



def unique_elements(string):
    """Get unique elements after merging strings"""
    new_list = string.split(', ')
    new_list = list(set(new_list))
    new_list = ', '.join(sorted(new_list))
    new_list = new_list.replace(", Not Specified", "")
    new_list = new_list.replace("Not Specified, ", "")      
    return new_list


def sort_list(string):
    """sort/unique string"""
    new_list = string.split(', ')
    new_list = list(set(new_list))
    new_list = ', '.join(sorted(new_list))         
    return new_list


#def first_letters(string):
#    """First and last letter of a word to create some unique id"""
#    first = string[0]
#    last = string[-1]
#    return first + last


def unique_product_id(filename):    
    
    """
    CLEAR PRODUCT CATEGORIES
    if product name and brand are the same then take all categories together and create one long list separated by comma
    """
    
    
    dataset = pd.read_csv(filename, encoding='utf-8-sig')
    
    dataset = dataset.drop_duplicates()
    
    """
    FROM FURTHER DATA CLEANING - 4 ITEMS WITH NO BRAND
    """
    
    # KNOWLEDGE EXCHANGE
    dataset['brand'] = np.where(dataset['product_name'] == "Knowledge Exchange", "Johnson Controls", dataset['brand'])
    
    
    # METASYS SMP
    dataset['brand'] = np.where(dataset['product_name'] == "Metasys SMP", "Metasys", dataset['brand'])
    
    
    # OM COMPRESSORS
    dataset['brand'] = np.where(dataset['document_title'].str.contains("OM Compressors"), "YORK", dataset['brand'])
    dataset['product_name'] = np.where(dataset['document_title'].str.contains("OM Compressors"), "OM Compressor", dataset['product_name'])
    dataset['product_category'] = np.where(dataset['document_title'].str.contains("OM Compressors"), "Centrifugal", dataset['product_category'])
    
    # ZNT06 - ZNT12
    dataset['brand'] = np.where(dataset['document_title'].str.contains("ZNT06 - ZNT12"), "TempMaster", dataset['brand'])
    
    
    # PRODUCT CATEGORIES
    dataset['product_category'] = dataset['product_category'].str.replace("DN40,DN50", "DN40,DN50")
    
    
    
    # TYCO FIX
    

    dataset['product_name'] = np.where(dataset['document_number'] == "TFP1305A", "DV-5A", dataset['product_name'])
    dataset['product_name'] = np.where(dataset['document_number'] == "TFP1305", "DV-5A", dataset['product_name'])
    dataset['product_name'] = np.where(dataset['document_number'] == "TFP1310", "DV-5A", dataset['product_name'])
    dataset['product_name'] = np.where(dataset['document_number'] == "TFP1315", "DV-5A", dataset['product_name'])
    dataset['product_name'] = np.where(dataset['document_number'] == "TFP1320", "DV-5A", dataset['product_name'])
    dataset['product_name'] = np.where(dataset['document_number'] == "TFP1335", "DV-5A", dataset['product_name'])
    dataset['product_name'] = np.where(dataset['document_number'] == "TFP1338", "DV-5A", dataset['product_name'])
    
    dataset['product_name'] = np.where(dataset['document_number'] == "TFP1410", "DV-5A", dataset['product_name'])  
    dataset['product_name'] = np.where(dataset['document_number'] == "TFP1415", "DV-5A", dataset['product_name'])
    dataset['product_name'] = np.where(dataset['document_number'] == "TFP1420", "DV-5A", dataset['product_name'])
    dataset['product_name'] = np.where(dataset['document_number'] == "TFP1460", "DV-5A", dataset['product_name'])   
    dataset['product_name'] = np.where(dataset['document_number'] == "TFP1465", "DV-5A", dataset['product_name'])
    



    
    dataset['product_name'] = np.where(dataset['document_number'] == "TFP1915", "CPVC BlazeMaster", dataset['product_name'])
    dataset['product_name'] = np.where(dataset['document_number'] == "TFP1920", "Model SHB1", dataset['product_name'])
    dataset['product_name'] = np.where(dataset['document_number'] == "TFP1925", "Rapid Seal Adapter", dataset['product_name'])
    dataset['product_name'] = np.where(dataset['document_number'] == "TFP1990", "TFP-500", dataset['product_name'])
    dataset['product_name'] = np.where(dataset['document_number'] == "TFP1994", "TFP-600", dataset['product_name'])
    dataset['product_name'] = np.where(dataset['document_number'] == "TFP1415", "DV-5A", dataset['product_name'])
    dataset['product_name'] = np.where(dataset['document_number'] == "TFP1950", "Model 3002", dataset['product_name'])
    
    
    dataset['product_name'] = np.where(dataset['document_title'] == "Model AMD-1 Automatic Air Maintenance Device Pressure Reducing Type with Field-Adjustable Pressure Regulator", "Model AMD-1", dataset['product_name'])
    dataset['product_name'] = np.where(dataset['document_title'] == "Model AMD-2 Automatic Air Maintenance Device Compressor Control Type with Field-Adjustable Pressure Switch", "Model AMD-2", dataset['product_name'])
    dataset['product_name'] = np.where(dataset['document_number'] == "Model AMD-3 Automatic Nitrogen Maintenance Device High Pressure (Cylinder) Reducing Type with Field-Adjustable Pressure Regulator", "Model AMD-3", dataset['product_name'])


    dataset['product_name'] = np.where(dataset['document_title'] == "Model ACC-1 Dry Pipe Valve Accelerator External Resetting Quick Opening Device for Dry Pipe Valves", "Model ACC-1", dataset['product_name'])
    dataset['product_name'] = np.where(dataset['document_title'] == "Model DPV-1 Dry Pipe Valve Model ACC-1 Dry Pipe Valve Accelerator Europen Conformity Valve Trim", "Model DPV-1", dataset['product_name'])
    dataset['product_name'] = np.where(dataset['document_number'] == "VIZOR Electronic Dry Pipe Accelerator (EDPA) Quick-Opening Device for Dry Pipe Systems", "VIZOR", dataset['product_name'])
    dataset['product_name'] = np.where(dataset['document_number'] == "Model DPV-1 Dry Pipe Valve External Resetting", "DPV-1", dataset['product_name'])
    dataset['product_name'] = np.where(dataset['document_number'] == "VIZOR Electronic Dry Pipe Accelerator (EDPA) Quick-Opening Device for Dry Pipe Systems", "VIZOR", dataset['product_name'])

    dataset['product_name'] = np.where(dataset['document_number'] == "Model QRS Electronic Accelerator (Quick Opening Device) For Dry Pipe or Preaction systems", "Model QRS", dataset['product_name'])
    dataset['product_name'] = np.where(dataset['document_number'] == "Model QRS Electronic Accelerator (Quick Opening Device) For Dry Pipe or Preaction systems", "Model QRS", dataset['product_name'])

    

    dataset['product_category'] = np.where(dataset['product_name'] == "DV-5A", "Deluge Fire Protection System, Deluge System Valves and Accessories", dataset['product_category'])
    
    dataset['product_name'] = np.where(dataset['document_number'] == "TFP890", "Blow-off Plugs", dataset['product_name'])
    
    dataset['product_name'] = np.where(dataset['document_number'] == "TFP1895", "GRINNELL", dataset['product_name'])
    
    dataset['product_name'] = np.where(dataset['document_number'] == "TFP1540", "Resilient-Seated Gate Valves", dataset['product_name'])
    dataset['product_name'] = np.where(dataset['document_number'] == "TFP1545", "Resilient-Seated Gate Valves", dataset['product_name'])


    dataset['product_name'] = np.where(dataset['document_number'] == "TFP1541", "Model TJR Resilient-Seated Gate Valves", dataset['product_name'])

    
    dataset['product_name'] = np.where(dataset['document_number'] == "TFP1546", "Model TJP Resilient-Seated Gate Valves", dataset['product_name'])


    dataset['product_name'] = np.where((dataset['brand'] == "Tyco") & (dataset['document_title'].str.contains("Solenoid Valves")), "Solenoid Valves For Deluge and Preaction Systems", dataset['product_name'])
    dataset['product_name'] = np.where((dataset['brand'] == "Tyco") & (dataset['document_title'].str.contains("Preaction System")), "Preaction System", dataset['product_name'])
    dataset['product_name'] = np.where((dataset['brand'] == "Tyco") & (dataset['document_title'].str.contains("Model BFV-300/BFV-300C")), "Model BFV-300/BFV-300C", dataset['product_name'])
    dataset['product_name'] = np.where((dataset['brand'] == "Tyco") & (dataset['document_title'].str.contains("Model BFV-250")), "Model BFV-250", dataset['product_name'])
    dataset['product_name'] = np.where((dataset['brand'] == "Tyco") & (dataset['document_title'].str.contains("Model TJR")), "Model TJR", dataset['product_name'])
    dataset['product_name'] = np.where((dataset['brand'] == "Tyco") & (dataset['document_title'].str.contains("Model TJP")), "Model TJR", dataset['product_name'])
    dataset['product_name'] = np.where((dataset['brand'] == "Tyco") & (dataset['document_title'].str.contains("Model CV-1F")), "Model CV-1F", dataset['product_name'])
    dataset['product_name'] = np.where((dataset['brand'] == "Tyco") & (dataset['document_title'].str.contains("Model CV-300B")), "Model CV-300B", dataset['product_name'])
    dataset['product_name'] = np.where((dataset['brand'] == "Tyco") & (dataset['document_title'].str.contains("Model PRV-1")), "Model PRV-1", dataset['product_name'])
    dataset['product_name'] = np.where((dataset['brand'] == "Tyco") & (dataset['document_title'].str.contains("GRINNELL")), "GRINNELL", dataset['product_name'])
    dataset['product_name'] = np.where((dataset['brand'] == "Tyco") & (dataset['document_title'].str.contains("Model F822 thru F834")), "Model F822 - F834", dataset['product_name'])
    dataset['product_name'] = np.where((dataset['brand'] == "Tyco") & (dataset['document_title'].str.contains("Model B-1 - 3.0")), "Model B-1 - 3.0", dataset['product_name'])
    dataset['product_name'] = np.where((dataset['brand'] == "Tyco") & (dataset['document_title'].str.contains("Model F822S Through F834S")), "Model F822S - F834S", dataset['product_name'])
    dataset['product_name'] = np.where((dataset['brand'] == "Tyco") & (dataset['document_title'].str.contains("Model TN-17")), "Model TN-17", dataset['product_name'])
    dataset['product_name'] = np.where((dataset['brand'] == "Tyco") & (dataset['document_title'].str.contains("Model TN-25")), "Model TN-25", dataset['product_name'])
    dataset['product_name'] = np.where((dataset['brand'] == "Tyco") & (dataset['document_title'].str.contains("Type 1 and 2 Cooling Tower Nozzles")), "Type 1 and 2", dataset['product_name'])
    dataset['product_name'] = np.where((dataset['brand'] == "Tyco") & (dataset['document_title'].str.contains("Type D3 PROTECTOSPRAY")), "Type D3 Protectospray", dataset['product_name'])
    dataset['product_name'] = np.where((dataset['brand'] == "Tyco") & (dataset['document_title'].str.contains("Type D3S PROTECTOSPRAY")), "Type D3S Protectospray", dataset['product_name'])
    dataset['product_name'] = np.where((dataset['brand'] == "Tyco") & (dataset['document_title'].str.contains("Type D4a Protectospray")), "Type D4a Protectospray", dataset['product_name'])
    dataset['product_name'] = np.where((dataset['brand'] == "Tyco") & (dataset['document_title'].str.contains("Type DN-5")), "Type DN-5", dataset['product_name'])
    dataset['product_name'] = np.where((dataset['brand'] == "Tyco") & (dataset['document_title'].str.contains("Type EA-1")), "Type EA-1", dataset['product_name'])
    dataset['product_name'] = np.where((dataset['brand'] == "Tyco") & (dataset['document_title'].str.contains("Type G")), "Type G", dataset['product_name'])
    dataset['product_name'] = np.where((dataset['brand'] == "Tyco") & (dataset['document_title'].str.contains("High Velocity Directional Spray Nozzles")), "High Velocity Directional Spray Nozzles", dataset['product_name'])
    dataset['product_name'] = np.where((dataset['brand'] == "Tyco") & (dataset['document_title'].str.contains("Type MV-R Reverse Action and Type MV-T")), "Type MV-R - MV-T", dataset['product_name'])
    dataset['product_name'] = np.where((dataset['brand'] == "Tyco") & (dataset['document_title'].str.contains("FASTFLEX")), "Flexible Sprinkler Hose", dataset['product_name'])
    dataset['product_name'] = np.where((dataset['brand'] == "Tyco") & (dataset['document_title'].str.contains("Model EG-25")), "Model EG-25", dataset['product_name'])
    dataset['product_name'] = np.where((dataset['brand'] == "Tyco") & (dataset['document_title'].str.contains("Model FH-1")), "Model FH-1", dataset['product_name'])
    dataset['product_name'] = np.where((dataset['brand'] == "Tyco") & (dataset['document_title'].str.contains("Sprinkler Cabinets")), "Sprinkler Cabinets", dataset['product_name'])
    dataset['product_name'] = np.where((dataset['brand'] == "Tyco") & (dataset['document_title'].str.contains("Sprinkler Guard")), "Sprinkler Guards", dataset['product_name'])
    
    dataset['product_name'] = np.where((dataset['brand'] == "Tyco") & (dataset['document_title'].str.contains("Flush Escutcheon")), "Flush Escutcheon", dataset['product_name'])
    dataset['product_name'] = np.where((dataset['brand'] == "Tyco") & (dataset['document_title'].str.contains("Pipe Fittings NPT Threaded, Ductile Iron")), "Pipe Fittings NPT Threaded, Ductile Iron", dataset['product_name'])
    dataset['product_name'] = np.where((dataset['brand'] == "Tyco") & (dataset['document_title'].str.contains("DV-5A")), "DV-5A Automatic Water Control Valve Preaction Type A Systems", dataset['product_name'])
    dataset['product_name'] = np.where((dataset['brand'] == "Tyco") & (dataset['document_title'].str.contains("DV-5A")), "DV-5A Automatic Water Control Valve Preaction Type A Systems", dataset['product_name'])
    dataset['product_name'] = np.where((dataset['brand'] == "Tyco") & (dataset['document_title'].str.contains("DPV-1")), "Model DPV-1 Preaction Type B Valves", dataset['product_name'])
    dataset['product_name'] = np.where((dataset['brand'] == "Tyco") & (dataset['document_title'].str.contains("Series LFII")), "Series LFII Residential Sprinkler", dataset['product_name'])
    dataset['product_name'] = np.where((dataset['brand'] == "Tyco") & (dataset['document_title'].str.contains("Two-Piece Recessed Escutcheons and Protective Paint Caps")), "Two-Piece Recessed Escutcheons and Protective Paint Caps", dataset['product_name'])
    
    
    
    # JC FIX
    dataset['product_name'] = np.where((dataset['brand'] == "Johnson Controls") & (dataset['document_title'].str.contains("LN Series Communicating Sensors")), "LN Series Communicating Sensors", dataset['product_name'])
    dataset['product_name'] = np.where((dataset['brand'] == "Johnson Controls") & (dataset['document_title'].str.contains("AS-CBLTSTAT Cable Adapter")), "AS-CBLTSTAT Cable Adapter", dataset['product_name'])
    dataset['product_name'] = np.where((dataset['brand'] == "Johnson Controls") & (dataset['document_title'].str.contains("Adj. Diff. Floating Switchover")), "Adj. Diff. Floating Switchover", dataset['product_name'])
    dataset['product_name'] = np.where((dataset['brand'] == "Johnson Controls") & (dataset['document_title'].str.contains("Three-Way Valve")), "Three-Way Valve", dataset['product_name'])
    dataset['product_name'] = np.where((dataset['brand'] == "Johnson Controls") & (dataset['document_title'].str.contains("BACnet")), "BACnet Router", dataset['product_name'])
    dataset['product_name'] = np.where((dataset['brand'] == "Johnson Controls") & (dataset['document_title'].str.contains("Bronze Cage Trim Valves")), "Bronze Cage Trim Valves", dataset['product_name'])
    dataset['product_name'] = np.where((dataset['brand'] == "Johnson Controls") & (dataset['document_title'].str.contains("Cast Iron Flanged Globe Valves")), "Cast Iron Flanged Globe Valves", dataset['product_name'])
    dataset['product_name'] = np.where((dataset['brand'] == "Johnson Controls") & (dataset['document_title'].str.contains("Johnson Controls Enterprise Management")), "Johnson Controls Enterprise Management", dataset['product_name'])
    dataset['product_name'] = np.where((dataset['brand'] == "Johnson Controls") & (dataset['document_title'].str.contains("Johnson Controls VGA9905-GGA Valve")), "Johnson Controls VGA9905-GGA Valve", dataset['product_name'])
    dataset['product_name'] = np.where((dataset['brand'] == "Johnson Controls") & (dataset['document_title'].str.contains("LN-Builder")), "LN-Builder", dataset['product_name'])
    dataset['product_name'] = np.where((dataset['brand'] == "Johnson Controls") & (dataset['document_title'].str.contains("Water Source/Geothermal Heat Pump")), "Water Source/Geothermal Heat Pump", dataset['product_name'])
    dataset['product_name'] = np.where((dataset['brand'] == "Johnson Controls") & (dataset['document_title'].str.contains("Water Source Heat Pumps")), "Water Source Heat Pumps", dataset['product_name'])
    dataset['product_name'] = np.where((dataset['brand'] == "Johnson Controls") & (dataset['document_title'].str.contains("LonWorks Network")), "LonWorks Network", dataset['product_name'])
    dataset['product_name'] = np.where((dataset['brand'] == "Johnson Controls") & (dataset['document_title'].str.contains("Replacement Diaphragms for Valve Actuators")), "Replacement Diaphragms for Valve Actuators", dataset['product_name'])
    dataset['product_name'] = np.where((dataset['brand'] == "Johnson Controls") & (dataset['document_title'].str.contains("Spring Return on Jobs with Electric Actuators")), "Spring Return on Jobs with Electric Actuators", dataset['product_name'])
    dataset['product_name'] = np.where((dataset['brand'] == "Johnson Controls") & (dataset['document_title'].str.contains("TSS Single-Duct VAV Terminals")), "TSS Single-Duct VAV Terminals", dataset['product_name'])
    dataset['product_name'] = np.where((dataset['brand'] == "Johnson Controls") & (dataset['document_title'].str.contains("VT Series Terminal Unit Valves")), "VT Series Terminal Unit Valves", dataset['product_name'])
    dataset['product_name'] = np.where((dataset['brand'] == "Johnson Controls") & (dataset['document_title'].str.contains("WRZ Series One-to-One Wireless Room Sensing System")), "WRZ Series One-to-One Wireless Room Sensing System", dataset['product_name'])
    dataset['product_name'] = np.where((dataset['brand'] == "Johnson Controls") & (dataset['document_title'].str.contains("TSS Single-Duct VAV Terminals")), "TSS Single-Duct VAV Terminals", dataset['product_name'])
    dataset['product_name'] = np.where((dataset['brand'] == "Johnson Controls") & (dataset['document_title'].str.contains("WT-BAC-IP Gateway")), "WT-BAC-IP Gateway", dataset['product_name'])
    dataset['product_name'] = np.where((dataset['brand'] == "Johnson Controls") & (dataset['document_title'].str.contains("ZFR Checkout Tool")), "ZFR Checkout Tool", dataset['product_name'])



    # PENN CONTROLS FIX
    dataset['product_name'] = np.where((dataset['brand'] == "PENN Controls") & (dataset['document_title'].str.contains("A11 Series Low Temperature Cutout")), "A11 Series Low Temperature Cutout", dataset['product_name'])
    dataset['product_name'] = np.where((dataset['brand'] == "PENN Controls") & (dataset['document_title'].str.contains("A19CAC Automatic Changeover Control")), "A19CAC Automatic Changeover Control", dataset['product_name'])
    dataset['product_name'] = np.where((dataset['brand'] == "PENN Controls") & (dataset['document_title'].str.contains("A19D Series Surface Mounted Temperature Controls")), "A19D Series Surface Mounted Temperature Controls", dataset['product_name'])
    dataset['product_name'] = np.where((dataset['brand'] == "PENN Controls") & (dataset['document_title'].str.contains("A19E Series Warm Air Fan and Duct Controls Low or Line Voltage")), "A19E Series Warm Air Fan and Duct Controls Low or Line Voltage", dataset['product_name'])
    dataset['product_name'] = np.where((dataset['brand'] == "PENN Controls") & (dataset['document_title'].str.contains("A350EB-4C Electronic Cooling Control")), "A350EB-4C Electronic Cooling Control", dataset['product_name'])
    dataset['product_name'] = np.where((dataset['brand'] == "PENN Controls") & (dataset['document_title'].str.contains("CLK3502 Time Clock")), "CLK3502 Time Clock", dataset['product_name'])    
    dataset['product_name'] = np.where((dataset['brand'] == "PENN Controls") & (dataset['document_title'].str.contains("350TM")), "System 350TM", dataset['product_name'])
    dataset['product_name'] = np.where((dataset['brand'] == "PENN Controls") & (dataset['document_title'].str.contains("Chilled Water Reset")), "Chilled Water Reset", dataset['product_name'])
    dataset['product_name'] = np.where((dataset['brand'] == "PENN Controls") & (dataset['document_title'].str.contains("Electronic On/Off Cooling Control")), "Electronic On/Off Cooling Control", dataset['product_name'])
    dataset['product_name'] = np.where((dataset['brand'] == "PENN Controls") & (dataset['document_title'].str.contains("Electronic Temperature Reset Module")), "Electronic Temperature Reset Module", dataset['product_name'])
    dataset['product_name'] = np.where((dataset['brand'] == "PENN Controls") & (dataset['document_title'].str.contains("MR5 Series Panel Mount Case Controller")), "MR5 Series Panel Mount Case Controller", dataset['product_name'])
    dataset['product_name'] = np.where((dataset['brand'] == "PENN Controls") & (dataset['document_title'].str.contains("Modular Electronic Sequencer")), "Modular Electronic Sequencer", dataset['product_name'])
    dataset['product_name'] = np.where((dataset['brand'] == "PENN Controls") & (dataset['document_title'].str.contains("P266 Series Single-Phase Condenser Fan Speed Control")), "P266 Series Single-Phase Condenser Fan Speed Control", dataset['product_name'])
    dataset['product_name'] = np.where((dataset['brand'] == "PENN Controls") & (dataset['document_title'].str.contains("P352 Staged ON/OFF Pressure Control")), "P352 Staged ON/OFF Pressure Control", dataset['product_name'])
    dataset['product_name'] = np.where((dataset['brand'] == "PENN Controls") & (dataset['document_title'].str.contains("Charged Temperature Elements and Bellows Pressure Elements")), "Charged Temperature Elements and Bellows Pressure Elements", dataset['product_name'])    
    dataset['product_name'] = np.where((dataset['brand'] == "PENN Controls") & (dataset['document_title'].str.contains("Proportional Plus Integral Temperature Stage Module")), "Proportional Plus Integral Temperature Stage Module", dataset['product_name'])
    dataset['product_name'] = np.where((dataset['brand'] == "PENN Controls") & (dataset['document_title'].str.contains("R353 Sequencer and S353 Stage Module")), "R353 Sequencer and S353 Stage Module", dataset['product_name'])
    dataset['product_name'] = np.where((dataset['brand'] == "PENN Controls") & (dataset['document_title'].str.contains("Series P315PR")), "Series P315PR Controllers", dataset['product_name'])  
    dataset['product_name'] = np.where((dataset['brand'] == "PENN Controls") & (dataset['document_title'].str.contains("Series P315PR Direct Mount Pressure Actuated Condenser Fan Speed Controllers")), "Series P315PR Direct Mount Pressure Actuated Condenser Fan Speed Controllers", dataset['product_name'])
    dataset['product_name'] = np.where((dataset['brand'] == "PENN Controls") & (dataset['document_title'].str.contains("Transformers Product")), "Transformers Product", dataset['product_name'])
    dataset['product_name'] = np.where((dataset['brand'] == "PENN Controls") & (dataset['document_title'].str.contains("Style B Bulb Sensing Element")), "Style B Bulb Sensing Element", dataset['product_name'])    
    dataset['product_name'] = np.where((dataset['brand'] == "PENN Controls") & (dataset['document_title'].str.contains("System 350")), "System 350 Controls", dataset['product_name'])
    dataset['product_name'] = np.where((dataset['brand'] == "PENN Controls") & (dataset['document_title'].str.contains("System 450")), "System 450 Controls", dataset['product_name'])       
    dataset['product_name'] = np.where((dataset['brand'] == "PENN Controls") & (dataset['document_title'].str.contains("T19PC Type Temperature Control")), "T19PC Type Temperature Control", dataset['product_name'])
    dataset['product_name'] = np.where((dataset['brand'] == "PENN Controls") & (dataset['document_title'].str.contains("Temperature Slave Stage Module")), "Temperature Slave Stage Module", dataset['product_name'])       
    dataset['product_name'] = np.where((dataset['brand'] == "PENN Controls") & (dataset['document_title'].str.contains("V50 Series Self-Operated Modulating Valves For Outdoor Crop Dryer Service")), "V50 Series Self-Operated Modulating Valves For Outdoor Crop Dryer Service", dataset['product_name'])               
    dataset['product_name'] = np.where((dataset['brand'] == "PENN Controls") & (dataset['document_title'].str.contains("Approximate Duty Cycling")), "Approximate Duty Cycling", dataset['product_name']) 
    
    
    
    dataset['product_name'] = np.where((dataset['brand'] == "PENN Controls") & (dataset['document_title'].str.contains("Proportional Temperature Control")), "Proportional Temperature Control", dataset['product_name']) 
    dataset['product_name'] = np.where((dataset['brand'] == "PENN Controls") & (dataset['document_title'].str.contains("Pressure Control")), "Pressure Control", dataset['product_name']) 
    dataset['product_name'] = np.where((dataset['brand'] == "PENN Controls") & (dataset['document_title'].str.contains("Floating temperature Control")), "Floating temperature Control", dataset['product_name']) 
    dataset['product_name'] = np.where((dataset['brand'] == "PENN Controls") & (dataset['document_title'].str.contains("Electronic Proportional Plus Integral Pressure Control")), "Electronic Proportional Plus Integral Pressure Control", dataset['product_name']) 
    dataset['product_name'] = np.where((dataset['brand'] == "PENN Controls") & (dataset['document_title'].str.contains("Pressure Display Module")), "Pressure Display Module", dataset['product_name']) 
    dataset['product_name'] = np.where((dataset['brand'] == "PENN Controls") & (dataset['document_title'].str.contains("Cooling Tower Control")), "Cooling Tower Control", dataset['product_name']) 
    dataset['product_name'] = np.where((dataset['brand'] == "PENN Controls") & (dataset['document_title'].str.contains("Two Speed Motor Control")), "Two Speed Motor Control", dataset['product_name']) 
    dataset['product_name'] = np.where((dataset['brand'] == "PENN Controls") & (dataset['document_title'].str.contains("Pressurization Control")), "Pressurization Control", dataset['product_name']) 
    dataset['product_name'] = np.where((dataset['brand'] == "PENN Controls") & (dataset['document_title'].str.contains("Cooling Tower Control")), "Cooling Tower Control", dataset['product_name']) 
    
    dataset['product_name'] = np.where((dataset['brand'] == "PENN Controls") & (dataset['document_title'].str.contains("Humidity Control")), "Humidity Control", dataset['product_name']) 
    dataset['product_name'] = np.where((dataset['brand'] == "PENN Controls") & (dataset['document_title'].str.contains("Humidity Transmitter")), "Humidity Transmitter", dataset['product_name']) 
    dataset['product_name'] = np.where((dataset['brand'] == "PENN Controls") & (dataset['document_title'].str.contains("Zone Temperature Reset")), "Zone Temperature Reset", dataset['product_name']) 
    dataset['product_name'] = np.where((dataset['brand'] == "PENN Controls") & (dataset['document_title'].str.contains("350TM")), "350TM", dataset['product_name']) 

    dataset['product_name'] = np.where((dataset['brand'] == "PENN Controls") & (dataset['document_title'].str.contains("Cooling Control")), "Cooling Control", dataset['product_name']) 
    dataset['product_name'] = np.where((dataset['brand'] == "PENN Controls") & (dataset['document_title'].str.contains("Electronic Temperature Reset Module")), "Electronic Temperature Reset Module", dataset['product_name']) 
    dataset['product_name'] = np.where((dataset['brand'] == "PENN Controls") & (dataset['document_title'].str.contains("Pressurization Control")), "Pressurization Control", dataset['product_name']) 
    dataset['product_name'] = np.where((dataset['brand'] == "PENN Controls") & (dataset['document_title'].str.contains("Cooling Tower Control")), "Cooling Tower Control", dataset['product_name']) 
    
    dataset['product_name'] = np.where((dataset['brand'] == "PENN Controls") & (dataset['document_title'].str.contains("Humidity Display Module")), "Humidity Display Module", dataset['product_name']) 
    dataset['product_name'] = np.where((dataset['brand'] == "PENN Controls") & (dataset['document_title'].str.contains("Humidity Stage Module")), "Humidity Stage Module", dataset['product_name']) 
    dataset['product_name'] = np.where((dataset['brand'] == "PENN Controls") & (dataset['document_title'].str.contains("Modular Electronic Sequencer")), "Modular Electronic Sequencer", dataset['product_name']) 
    dataset['product_name'] = np.where((dataset['brand'] == "PENN Controls") & (dataset['document_title'].str.contains("Power Module")), "Power Module", dataset['product_name']) 
    dataset['product_name'] = np.where((dataset['brand'] == "PENN Controls") & (dataset['document_title'].str.contains("Pressurization Control")), "Pressurization Control", dataset['product_name']) 
    dataset['product_name'] = np.where((dataset['brand'] == "PENN Controls") & (dataset['document_title'].str.contains("Cooling Tower Control")), "Cooling Tower Control", dataset['product_name']) 
    
    dataset['product_name'] = np.where((dataset['brand'] == "PENN Controls") & (dataset['document_title'].str.contains("Pressure Stage Module")), "Pressure Stage Module", dataset['product_name']) 
    dataset['product_name'] = np.where((dataset['brand'] == "PENN Controls") & (dataset['document_title'].str.contains("Proportional Plus Integral Temperature Stage Module")), "Proportional Plus Integral Temperature Stage Module", dataset['product_name']) 
    dataset['product_name'] = np.where((dataset['brand'] == "PENN Controls") & (dataset['document_title'].str.contains("Temperature Display Module")), "Pressurization Control", dataset['product_name']) 
    dataset['product_name'] = np.where((dataset['brand'] == "PENN Controls") & (dataset['document_title'].str.contains("Temperature Slave Stage Module")), "Temperature Slave Stage Module", dataset['product_name']) 
    dataset['product_name'] = np.where((dataset['brand'] == "PENN Controls") & (dataset['document_title'].str.contains("Temperature Stage Module")), "Temperature Stage Module", dataset['product_name']) 
    dataset['product_name'] = np.where((dataset['brand'] == "PENN Controls") & (dataset['document_title'].str.contains("Electronic Pressure Control")), "Electronic Pressure Control", dataset['product_name']) 
    dataset['product_name'] = np.where((dataset['brand'] == "PENN Controls") & (dataset['document_title'].str.contains("Modular Electronic Sequencer")), "Modular Electronic Sequencer", dataset['product_name']) 
    dataset['product_name'] = np.where((dataset['brand'] == "PENN Controls") & (dataset['document_title'].str.contains("Electronic Temperature Control")), "Electronic Temperature Control", dataset['product_name']) 
    dataset['product_name'] = np.where((dataset['brand'] == "PENN Controls") & (dataset['document_title'].str.contains("Electronic Cooling Control")), "Electronic Cooling Control", dataset['product_name']) 
    dataset['product_name'] = np.where((dataset['brand'] == "PENN Controls") & (dataset['document_title'].str.contains("Electronic Proportional Plus Integral Pressure Control")), "Electronic Proportional Plus Integral Pressure Control", dataset['product_name']) 
    dataset['product_name'] = np.where((dataset['brand'] == "PENN Controls") & (dataset['document_title'].str.contains("A19CAC Automatic Changeover Control")), "A19CAC Automatic Changeover Control", dataset['product_name']) 
    dataset['product_name'] = np.where((dataset['brand'] == "PENN Controls") & (dataset['document_title'].str.contains("A19E Series")), "A19E Series", dataset['product_name']) 
    dataset['product_name'] = np.where((dataset['brand'] == "PENN Controls") & (dataset['document_title'].str.contains("V50 Series Self-Operated Modulating Valves")), "V50 Series Self-Operated Modulating Valves", dataset['product_name']) 
    dataset['product_name'] = np.where((dataset['brand'] == "PENN Controls") & (dataset['document_title'].str.contains("Series P315PR Controllers")), "Series P315PR Controllers", dataset['product_name']) 
    dataset['product_name'] = np.where((dataset['brand'] == "PENN Controls") & (dataset['document_title'].str.contains("A19CAC Type Automatic Changeover Control")), "A19CAC Type Automatic Changeover Control", dataset['product_name']) 
    dataset['product_name'] = np.where((dataset['brand'] == "PENN Controls") & (dataset['document_title'].str.contains("P266 Series Single-Phase Condenser Fan Speed Control")), "P266 Series Single-Phase Condenser Fan Speed Control", dataset['product_name']) 
   
    
    
    dataset['product_name'] = np.where((dataset['brand'] == "PENN Controls") & (dataset['document_title'].str.contains("Thermostat")), "Thermostats", dataset['product_name']) 
    dataset['product_name'] = np.where((dataset['brand'] == "PENN Controls") & (dataset['document_title'].str.contains("Series P315PR Controllers")), "Series P315PR Controllers", dataset['product_name']) 
    dataset['product_name'] = np.where((dataset['brand'] == "PENN Controls") & (dataset['document_title'].str.contains("T22")), "Thermostats", dataset['product_name']) 
    dataset['product_name'] = np.where((dataset['brand'] == "PENN Controls") & (dataset['document_title'].str.contains("S26")), "S26 Series Switching Subbase", dataset['product_name'])         
    dataset['product_name'] = np.where((dataset['brand'] == "PENN Controls") & (dataset['document_title'].str.contains("Bulb Wells")), "Bulb Wells", dataset['product_name'])
    
    dataset['product_name'] = np.where((dataset['brand'] == "PENN Controls") & (dataset['document_title'].str.contains("Y63")), "Y63", dataset['product_name']) 
    dataset['product_name'] = np.where((dataset['brand'] == "PENN Controls") & (dataset['document_title'].str.contains("R310A Series Current Sensing Switch")), "R310A Series Current Sensing Switch", dataset['product_name']) 
    dataset['product_name'] = np.where((dataset['brand'] == "PENN Controls") & (dataset['document_title'].str.contains("SEC99A UltraCap Armored Capillary")), "SEC99A UltraCap Armored Capillary", dataset['product_name']) 
    dataset['product_name'] = np.where((dataset['brand'] == "PENN Controls") & (dataset['document_title'].str.contains("Universal Mounting Brackets")), "Universal Mounting Brackets", dataset['product_name'])         
    dataset['product_name'] = np.where((dataset['brand'] == "PENN Controls") & (dataset['document_title'].str.contains("Bulb Wells")), "Bulb Wells", dataset['product_name'])
    
    dataset['product_name'] = np.where((dataset['brand'] == "PENN Controls") & (dataset['document_title'].str.contains("V50 Series Crop Drying Module")), "V50 Series Crop Drying Module", dataset['product_name'])
    
    dataset['product_name'] = np.where((dataset['brand'] == "PENN Controls") & (dataset['document_title'].str.contains("Bulb Wells")), "Bulb Wells", dataset['product_name'])
    

    
#    tyco_fix =  dataset[dataset['product_category'].str.contains("Pilot Actuation")]
#    tyco_fix =  dataset[dataset['document_title'].str.contains("Flush Escutcheon")]
    
    
    ## GROUP BY THE SAME NAME + BRAND AND CREATE LONG CATEGORY LIST 
    dataset_cat = dataset.groupby(['product_name','brand'], as_index=False).agg(', '.join)
    dataset_cat['product_category_long'] = dataset_cat['product_category'].apply(lambda x: unique_elements(x)) 
    
    dataset_cat = dataset_cat[['product_name','brand','product_category_long']]
    
    
    dataset = dataset.merge(dataset_cat, how = "left", on = ['product_name','brand'])
    
    
    dataset['product_category'] = dataset['product_category_long']
    dataset = dataset.drop(['product_category_long'], axis=1)
    
    dataset = dataset.drop_duplicates()
    
    
    """
    CLEAN PRODUCT SERIES
    """
    
    ## GROUP BY THE SAME NAME + BRAND AND CREATE LONG CATEGORY LIST 
    dataset_series = dataset.groupby(['product_name','brand', 'product_category'], as_index=False).agg(', '.join)
    dataset_series['product_series_long'] = dataset_series['product_series'].apply(lambda x: unique_elements(x)) 
    
    dataset_series = dataset_series[['product_name','brand','product_category', 'product_series_long']]
    
    
    dataset = dataset.merge(dataset_series, how = "left", on = ['product_name','brand','product_category'])
    
    
    dataset['product_series'] = dataset['product_series_long']
    dataset = dataset.drop(['product_series_long'], axis=1)
    
    dataset = dataset.drop_duplicates()
    
    
    
    """
    SORT PRODUCT CODES
    """
    
    dataset['product_code'] = dataset['product_code'].apply(lambda x: sort_list(x))
    
    ## GROUP BY THE SAME NAME + BRAND AND CREATE LONG CATEGORY LIST 
    dataset_codes = dataset.groupby(['product_name','brand', 'product_category'], as_index=False).agg(', '.join)
    dataset_codes['product_code_long'] = dataset_codes['product_code'].apply(lambda x: unique_elements(x))
    
    dataset_codes = dataset_codes[['product_name','brand','product_category', 'product_code_long']]
    
    dataset = dataset.merge(dataset_codes, how = "left", on = ['product_name','brand','product_category'])
    
    dataset['product_code'] = dataset['product_code_long']
    dataset = dataset.drop(['product_code_long'], axis=1)
    
    dataset = dataset.drop_duplicates()
    
    
    
    """
    MERGE BUSINESSES FOR THE SAME PRODUCT
    """
    dataset_business = dataset.groupby(['product_name','brand','product_code', 'product_category'], as_index=False).agg(', '.join)
    dataset_business['product_business_long'] = dataset_business['business'].apply(lambda x: unique_elements(x))
    dataset_business = dataset_business[['product_name','brand','product_category', 'product_code', 'product_business_long']]
    dataset = dataset.merge(dataset_business, how = "left", on = ['product_name','brand','product_code', 'product_category'])
    dataset['business'] = dataset['product_business_long']
    dataset = dataset.drop(['product_business_long'], axis=1)
    
    dataset = dataset.drop_duplicates()
    
    
    """
    CREATING UNIQUE IDENTIFIER FOR ALL PRODUCTS
    first part of name + created_id + first three letters of brand ...
    """
    
    
#    dataset['product_name_first'] = dataset['product_name'].str.split(',').str[0]
#    dataset['product_name_id'] = dataset['product_name'].apply(lambda x: first_letters(str(x)))
#    dataset['brand_id'] = dataset['brand'].str[:3]
#    dataset['product_category_id'] = dataset['product_category'].apply(lambda x: first_letters(str(x)))
#    dataset['product_code_id'] = dataset['product_code'].apply(lambda x: first_letters(str(x)))   
    dataset['product_code_first'] = dataset['product_code'].str.split(',').str[0]
#    dataset['product_code_last'] = dataset['product_code'].str.split(',').str[-1]
#    dataset['product_series_id'] = dataset['product_series'].apply(lambda x: first_letters(str(x)))
#    dataset['product_business_id'] = dataset['business'].apply(lambda x: first_letters(str(x)))
#    
    """
    CREATE UNIQUE PRODUCT ID 
    """
    dataset['product_identifier'] = dataset['product_name'] + "-" + dataset['brand'] +  "-" + dataset['product_code_first']  + "-" + dataset['product_series'] + "-" + dataset['business']                
    dataset['product_identifier'] = dataset['product_identifier'].apply(lambda x: hashlib.sha1(str.encode(x)).hexdigest())
    
    # CHECK
#    product_id_unique = list(dataset['product_identifier'].unique())
    
    dataset = dataset.drop(['product_code_first'], axis=1)

    
    
    
    dataset.to_csv('documents_unique_product_id.csv',  encoding='utf-8-sig', index=False)
        
    
    return dataset






data = unique_product_id("documents_sorted_products.csv") 




















    

    