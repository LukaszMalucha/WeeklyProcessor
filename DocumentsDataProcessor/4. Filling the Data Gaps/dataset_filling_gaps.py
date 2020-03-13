# -*- coding: utf-8 -*-
"""
Created on Fri Mar 13 12:12:40 2020

@author: LukaszMalucha
"""




import pandas as pd
import numpy as np


def remove_form_small(string):
    string = string.split("(Form")[0]
    return string

def remove_form_big(string):
    string = string.split("(FORM")[0]
    return string

def remove_form_gap(string):
    string = string.split("( Form")[0]
    return string


def remove_si(string):
    string = string.split("(SI")[0]
    return string

def software_enhancements_split(string):
    string = string.split(" Software Enhancements")[0]
    return string








def fill_brand_and_product_gaps(filename):
    """
    FILLING PRODUCT BRAND GAPS THEN PRODUCT NAMES WITH DOCUMENT TITLES
    """
       
    dataset = pd.read_csv(filename, encoding='utf-8-sig')
        
    dataset['get_name'] = np.where(dataset['product_name'] == "Not Specified", dataset['document_title'], "Not Specified")
    
    
    dataset['get_name'] = dataset['get_name'].apply(lambda x: remove_form_small(x))
    dataset['get_name'] = dataset['get_name'].apply(lambda x: remove_form_big(x))
    dataset['get_name'] = dataset['get_name'].apply(lambda x: remove_form_gap(x))
    
    dataset['get_name'] = dataset['get_name'].apply(lambda x: remove_si(x))
    dataset['get_name'] = dataset['get_name'].apply(lambda x: software_enhancements_split(x))
    
    # REPLACE
    dataset['get_name'] = dataset['get_name'].str.replace("ALL Liquid Cooled Solis State Starters Troubleshooting Output Current Imbalance ", "Liquid Cooled Solis State Starters")
    dataset['get_name'] = dataset['get_name'].str.replace("User’s: Introduction to Facility Explorer Administrator Tool for Validated Environments", "")
    dataset['get_name'] = dataset['get_name'].str.replace(". Module Installation and Programming Instructions", "")
    dataset['get_name'] = dataset['get_name'].str.replace("VSD Wiring Diagram, ", "")
    dataset['get_name'] = dataset['get_name'].str.replace(" Installtion Instructions", "")
    dataset['get_name'] = dataset['get_name'].str.replace("Service Information Letter", "")
    dataset['get_name'] = dataset['get_name'].str.replace(" Installation/Programming Instructions", "")
    dataset['get_name'] = dataset['get_name'].str.replace(" Quick Start Guide for Asia", "")
    dataset['get_name'] = dataset['get_name'].str.replace(" Wiring Instructions", "")
    dataset['get_name'] = dataset['get_name'].str.replace(" Quick Start Guide", "")
    dataset['get_name'] = dataset['get_name'].str.replace(" Engineering Guide", "")
    dataset['get_name'] = dataset['get_name'].str.replace(" Instruction Sheet", "")
    dataset['get_name'] = dataset['get_name'].str.replace(" Commissioning Guide", "")
    dataset['get_name'] = dataset['get_name'].str.replace(" User's Guide", "")
    dataset['get_name'] = dataset['get_name'].str.replace(" User Guide", "")
    dataset['get_name'] = dataset['get_name'].str.replace(" Sheets Manual", "")
    dataset['get_name'] = dataset['get_name'].str.replace(" Catalog Page", "")
    dataset['get_name'] = dataset['get_name'].str.replace(" Mandatory Returns", "")
    dataset['get_name'] = dataset['get_name'].str.replace(", Product Drawing", "")
    dataset['get_name'] = dataset['get_name'].str.replace(" Operations Manual", "")
    dataset['get_name'] = dataset['get_name'].str.replace(" Product Bulletin", "")
    dataset['get_name'] = dataset['get_name'].str.replace("Application Note - ", "")
    dataset['get_name'] = dataset['get_name'].str.replace(" Noise Troubleshooting, Repair and Replacement Details", "")
    dataset['get_name'] = dataset['get_name'].str.replace(" Implementation Conformance Statement", "")
    dataset['get_name'] = dataset['get_name'].str.replace(" Wiring Diagrams", "")
    dataset['get_name'] = dataset['get_name'].str.replace(" Replacement Instructions", "")
    dataset['get_name'] = dataset['get_name'].str.replace(" Maintenance Requirements / Chiller Log Sheets", "")
    dataset['get_name'] = dataset['get_name'].str.replace(" Shaft Alignment", "")
    dataset['get_name'] = dataset['get_name'].str.replace(" Product/Technical Bulletin", "")
    dataset['get_name'] = dataset['get_name'].str.replace(" Safety Data Sheet", "")
    dataset['get_name'] = dataset['get_name'].str.replace(" Operation Manual ", "")
    dataset['get_name'] = dataset['get_name'].str.replace(" Installation Instructions", "")
    dataset['get_name'] = dataset['get_name'].str.replace(" Installation and Upgrade Instructions", "")
    dataset['get_name'] = dataset['get_name'].str.replace(" Technical Bulletin", "")
    dataset['get_name'] = dataset['get_name'].str.replace(" Registration Form", "")
    dataset['get_name'] = dataset['get_name'].str.replace(" Applications Application Note", "")
    dataset['get_name'] = dataset['get_name'].str.replace(" Technical Bulletin", "")
    dataset['get_name'] = dataset['get_name'].str.replace(" Configuration Guide", "")
    dataset['get_name'] = dataset['get_name'].str.replace(" Application Note", "")
    dataset['get_name'] = dataset['get_name'].str.replace(" Installation", "")
    dataset['get_name'] = dataset['get_name'].str.replace("Technical Guide: ", "")
    dataset['get_name'] = dataset['get_name'].str.replace(" Guide: ", "")
    dataset['get_name'] = dataset['get_name'].str.replace(" Help: ", "")
    dataset['get_name'] = dataset['get_name'].str.replace(" Help", "")
    dataset['get_name'] = dataset['get_name'].str.replace(" Installation Instructions", "")
    dataset['get_name'] = dataset['get_name'].str.replace(" Literature Information ", "")
    dataset['get_name'] = dataset['get_name'].str.replace(" Product Drawing ", "")
    dataset['get_name'] = dataset['get_name'].str.replace(" Replacement Service Information Letter ", "")
    dataset['get_name'] = dataset['get_name'].str.replace(" Check Sheet (Form 160.00-CL2)", "")
    dataset['get_name'] = dataset['get_name'].str.replace(" Replacement Service Information (SI0275)", "")
    dataset['get_name'] = dataset['get_name'].str.replace(" Quick Start Guide", "")
    dataset['get_name'] = dataset['get_name'].str.replace(" Sequence of Operation Overview", "")
    dataset['get_name'] = dataset['get_name'].str.replace("Submittal Data Sheet: ", "")
    dataset['get_name'] = dataset['get_name'].str.replace(" Check Sheet", "")
    dataset['get_name'] = dataset['get_name'].str.replace("Installation Instructions for ", "")
    dataset['get_name'] = dataset['get_name'].str.replace(" Guide", "")
    dataset['get_name'] = dataset['get_name'].str.replace(" Checklist", "")
    dataset['get_name'] = dataset['get_name'].str.replace(" Appendices", "")
    dataset['get_name'] = dataset['get_name'].str.replace("Part Number Corrections for ", "")
    dataset['get_name'] = dataset['get_name'].str.replace("Application Note ", "")
    dataset['get_name'] = dataset['get_name'].str.replace(" Replacement Service Information", "")
    dataset['get_name'] = dataset['get_name'].str.replace(" Cross-Reference", "")
    dataset['get_name'] = dataset['get_name'].str.replace(" Maintenance", "")
    dataset['get_name'] = dataset['get_name'].str.replace("Troubleshooting ", "")
    dataset['get_name'] = dataset['get_name'].str.replace(" OPERATING INSTRUCTIONS", "")
    dataset['get_name'] = dataset['get_name'].str.replace(" Instructions", "")
    dataset['get_name'] = dataset['get_name'].str.replace(", Operation, Mainentance", "")
    dataset['get_name'] = dataset['get_name'].str.replace(", Operation, and Manual", "")
    dataset['get_name'] = dataset['get_name'].str.replace("Instruction", "")
    dataset['get_name'] = dataset['get_name'].str.replace(" Operating & ", "")
    dataset['get_name'] = dataset['get_name'].str.replace(" Operation & ", "")
    dataset['get_name'] = dataset['get_name'].str.replace(" Operation and ", "")
    dataset['get_name'] = dataset['get_name'].str.replace(", Operation ", "")
    dataset['get_name'] = dataset['get_name'].str.replace(" Operation ", "")
    dataset['get_name'] = dataset['get_name'].str.replace(" Wiring Diagram", "")
    dataset['get_name'] = dataset['get_name'].str.replace("Liquid Chillers,,", "Liquid Chillers")
    dataset['get_name'] = dataset['get_name'].str.replace(" Design Change Service Information ", "")
    dataset['get_name'] = dataset['get_name'].str.replace(" Service Information ", "")
    dataset['get_name'] = dataset['get_name'].str.replace(" Customers Annual Report Centrifugal Seasonal Inspection ", "")
    dataset['get_name'] = dataset['get_name'].str.replace(", Product", "")
    dataset['get_name'] = dataset['get_name'].str.replace(" and Start-Up ", "")
    dataset['get_name'] = dataset['get_name'].str.replace(" Start-Up ", "")
    dataset['get_name'] = dataset['get_name'].str.replace(" Start-Up ", "")
    dataset['get_name'] = dataset['get_name'].str.replace(", Operation, and ", "")
    dataset['get_name'] = dataset['get_name'].str.replace(", &", "")
    dataset['get_name'] = dataset['get_name'].str.replace(" Pre-Startup and Startup ", "")
    dataset['get_name'] = dataset['get_name'].str.replace(" / Log Sheet ", "")
    dataset['get_name'] = dataset['get_name'].str.replace(" Settings ", "")
    dataset['get_name'] = dataset['get_name'].str.replace(" - Auto Start", "")
    
    
    
    dataset['get_name'] = dataset['get_name'].str.replace('All TM & VSD Compressor Drives Using Mod Bus Comm. "Harmonic Filter Not Running" Warning Message ', "VSD Compressor")
    dataset['get_name'] = dataset['get_name'].str.replace('All YIA /YPC Absorption Chillers Mercury Manometers No Longer Available ', "YIA /YPC Absorption Chillers Mercury Manometers")
    
    
    
    # REVERSE ERRATIC TREASNFORMATIONS
    dataset['get_name'] = dataset['get_name'].str.replace("Language Program", "Language Installation Program")
    dataset['get_name'] = dataset['get_name'].str.replace("Multi-Unit Sequencing Operation & ", "Multi-Unit Sequencing Installation Operation & Maintenance")
    
    ## EQUALS
    
    dataset['get_name'] = np.where((dataset['brand'] == "Not Specified") & (dataset['get_name'] == "Related Links"), "Knowledge Exchange", dataset['get_name'])
    dataset['brand'] = np.where((dataset['brand'] == "Not Specified") & (dataset['get_name'] == "Related Links"), "Johnson Controls", dataset['brand'])
    dataset['brand'] = np.where((dataset['brand'] == "Not Specified") & (dataset['document_title'] == "Knowledge Exchange User Guide"), "Johnson Controls", dataset['brand'])
    
    
    dataset['get_name'] = np.where((dataset['brand'] == "Not Specified") & (dataset['document_title'] == "Trend Studies"), "Metasys SMP", dataset['get_name'])
    dataset['brand'] = np.where((dataset['brand'] == "Not Specified") & (dataset['document_title'] == "Trend Studies"), "Metasys", dataset['brand'])
    
    
    
    ## CONTAINS
    
    dataset['get_name'] = np.where((dataset['brand'] == "Not Specified") & (dataset['get_name'].str.contains("SQL Server")), "SQL Server", dataset['get_name'])
    dataset['brand'] = np.where((dataset['brand'] == "Not Specified") & (dataset['get_name'].str.contains("SQL Server")), "Johnson Controls", dataset['brand'])
    
    
    dataset['get_name'] = np.where((dataset['brand'] == "Not Specified") & (dataset['get_name'].str.contains("SQL Server")), "SQL Server", dataset['get_name'])
    dataset['brand'] = np.where((dataset['brand'] == "Not Specified") & (dataset['get_name'].str.contains("SQL Server")), "Johnson Controls", dataset['brand'])
    
    dataset['get_name'] = np.where((dataset['brand'] == "Not Specified") & (dataset['get_name'].str.contains("Johnson Controls® Enterprise Management")), "Johnson Controls® Enterprise Management", dataset['get_name'])
    dataset['brand'] = np.where((dataset['brand'] == "Not Specified") & (dataset['get_name'].str.contains("Johnson Controls® Enterprise Management")), "Johnson Controls", dataset['brand'])
    
    
    dataset['get_name'] = np.where((dataset['brand'] == "Not Specified") & (dataset['get_name'].str.contains("Knowledge Exchange")), "Knowledge Exchange", dataset['get_name'])
    dataset['brand'] = np.where((dataset['brand'] == "Not Specified") & (dataset['get_name'].str.contains("Knowledge Exchange")), "Johnson Controls", dataset['brand'])
    
    dataset['get_name'] = np.where((dataset['brand'] == "Not Specified") & (dataset['get_name'].str.contains("At a Glance")), "Metasys SMP", dataset['get_name'])
    dataset['brand'] = np.where((dataset['brand'] == "Not Specified") & (dataset['get_name'].str.contains("At a Glance")), "Metasys", dataset['brand'])
    
    
    dataset['get_name'] = np.where((dataset['brand'] == "Not Specified") & (dataset['get_name'].str.contains("CCS")), "CCS", dataset['get_name'])
    dataset['brand'] = np.where((dataset['brand'] == "Not Specified") & (dataset['get_name'].str.contains("CCS")), "YORK", dataset['brand'])
    
    dataset['get_name'] = np.where((dataset['brand'] == "Not Specified") & (dataset['get_name'].str.contains("CCT")), "CCT", dataset['get_name'])
    dataset['brand'] = np.where((dataset['brand'] == "Not Specified") & (dataset['get_name'].str.contains("CCT")), "Johnson Controls", dataset['brand'])
    
    
    dataset['brand'] = np.where((dataset['brand'] == "Not Specified") & (dataset['get_name'].str.contains("System License Information")), "BCPro", dataset['brand'])
    
    
    
    # METASYS
    
    dataset['brand'] = np.where((dataset['brand'] == "Not Specified") & (dataset['get_name'] == "Metasys SMP"), "Metasys", dataset['brand'])
    dataset['brand'] = np.where((dataset['brand'] == "Not Specified") & (dataset['get_name'].str.contains("Metasys")), "Metasys", dataset['brand'])
    dataset['brand'] = np.where((dataset['brand'] == "Not Specified") & (dataset['get_name'].str.contains("NIE")), "Metasys", dataset['brand'])
    dataset['brand'] = np.where((dataset['brand'] == "Not Specified") & (dataset['get_name'].str.contains("NxE")), "Metasys", dataset['brand'])
    dataset['brand'] = np.where((dataset['brand'] == "Not Specified") & (dataset['get_name'].str.contains("NAE85")), "Metasys", dataset['brand'])
    
    
    dataset['brand'] = np.where((dataset['brand'] == "Not Specified") & (dataset['get_name'].str.contains("Advanced Graphics Application")), "Metasys", dataset['brand'])
    dataset['brand'] = np.where((dataset['brand'] == "Not Specified") & (dataset['get_name'].str.contains("Controller Tool Help")), "Metasys", dataset['brand'])
    dataset['brand'] = np.where((dataset['brand'] == "Not Specified") & (dataset['get_name'].str.contains("Customer License Portal Help")), "Metasys", dataset['brand'])
    dataset['brand'] = np.where((dataset['brand'] == "Not Specified") & (dataset['get_name'].str.contains("Database Tools Commissioning Guide")), "Metasys", dataset['brand'])
    dataset['brand'] = np.where((dataset['brand'] == "Not Specified") & (dataset['get_name'].str.contains("Energy Essentials Installation Instructions")), "Metasys", dataset['brand'])
    dataset['brand'] = np.where((dataset['brand'] == "Not Specified") & (dataset['get_name'].str.contains("Graphics Conversion Utility")), "Metasys", dataset['brand'])
    dataset['brand'] = np.where((dataset['brand'] == "Not Specified") & (dataset['get_name'].str.contains("ABCS License Portal")), "Metasys", dataset['brand'])
    dataset['brand'] = np.where((dataset['brand'] == "Not Specified") & (dataset['get_name'].str.contains("License Portal ")), "Metasys", dataset['brand'])
    
    
    dataset['brand'] = np.where((dataset['brand'] == "Not Specified") & (dataset['get_name'].str.contains("Ready Access Portal")), "Metasys", dataset['brand'])
    
    dataset['brand'] = np.where((dataset['brand'] == "Not Specified") & (dataset['get_name'].str.contains("SCT")), "Metasys", dataset['brand'])
    dataset['brand'] = np.where((dataset['brand'] == "Not Specified") & (dataset['get_name'].str.contains("Security Administrator System")), "Metasys", dataset['brand'])
    dataset['brand'] = np.where((dataset['brand'] == "Not Specified") & (dataset['get_name'].str.contains("Software Activation Manager")), "Metasys", dataset['brand'])
    dataset['brand'] = np.where((dataset['brand'] == "Not Specified") & (dataset['get_name'].str.contains("Software License Activator")), "Metasys", dataset['brand'])
    dataset['brand'] = np.where((dataset['brand'] == "Not Specified") & (dataset['get_name'].str.contains("Temperature Data Acquisition")), "Metasys", dataset['brand'])
    dataset['brand'] = np.where((dataset['brand'] == "Not Specified") & (dataset['get_name'].str.contains("Language Installation Program")), "Metasys", dataset['brand'])
    dataset['brand'] = np.where((dataset['brand'] == "Not Specified") & (dataset['get_name'].str.contains("AS-CBLPRO-2")), "Metasys", dataset['brand'])
    dataset['brand'] = np.where((dataset['brand'] == "Not Specified") & (dataset['get_name'].str.contains(" License Portal")), "Metasys", dataset['brand'])
    dataset['brand'] = np.where((dataset['brand'] == "Not Specified") & (dataset['get_name'].str.contains("N2 Field Equipment Controllers and Related Products")), "Metasys", dataset['brand'])
    dataset['brand'] = np.where((dataset['brand'] == "Not Specified") & (dataset['get_name'].str.contains("Network and IT Guidance")), "Metasys", dataset['brand'])
    dataset['brand'] = np.where((dataset['brand'] == "Not Specified") & (dataset['get_name'].str.contains("Open Data Server")), "Metasys", dataset['brand'])
    dataset['brand'] = np.where((dataset['brand'] == "Not Specified") & (dataset['get_name'].str.contains("WNC1800")), "Metasys", dataset['brand'])
    
    
    
    # JC
    dataset['brand'] = np.where((dataset['brand'] == "Not Specified") & (dataset['get_name'].str.contains("A-4000")), "Johnson Controls", dataset['brand'])
    dataset['brand'] = np.where((dataset['brand'] == "Not Specified") & (dataset['get_name'].str.contains("A-Series")), "Johnson Controls", dataset['brand'])
    dataset['brand'] = np.where((dataset['brand'] == "Not Specified") & (dataset['get_name'].str.contains("ACC-")), "Johnson Controls", dataset['brand'])
    
    dataset['brand'] = np.where((dataset['brand'] == "Not Specified") & (dataset['get_name'].str.contains("Command Relays")), "Johnson Controls", dataset['brand'])
    dataset['brand'] = np.where((dataset['brand'] == "Not Specified") & (dataset['get_name'].str.contains("ContactInformation")), "Johnson Controls", dataset['brand'])
    dataset['brand'] = np.where((dataset['brand'] == "Not Specified") & (dataset['get_name'].str.contains("Controller Tool")), "Johnson Controls", dataset['brand'])
    dataset['brand'] = np.where((dataset['brand'] == "Not Specified") & (dataset['get_name'].str.contains("Database Tools")), "Johnson Controls", dataset['brand'])
    dataset['brand'] = np.where((dataset['brand'] == "Not Specified") & (dataset['get_name'].str.contains("Energy Essentials")), "Johnson Controls", dataset['brand'])
    
    dataset['brand'] = np.where((dataset['brand'] == "Not Specified") & (dataset['get_name'].str.contains("ODS")), "Johnson Controls", dataset['brand'])
    dataset['brand'] = np.where((dataset['brand'] == "Not Specified") & (dataset['get_name'].str.contains("LN Series")), "Johnson Controls", dataset['brand'])
    dataset['brand'] = np.where((dataset['brand'] == "Not Specified") & (dataset['get_name'].str.contains("LN-Series")), "Johnson Controls", dataset['brand'])
    dataset['brand'] = np.where((dataset['brand'] == "Not Specified") & (dataset['get_name'].str.contains("LN ")), "Johnson Controls", dataset['brand'])
    dataset['brand'] = np.where((dataset['brand'] == "Not Specified") & (dataset['get_name'].str.contains("FEC")), "Johnson Controls", dataset['brand'])
    dataset['brand'] = np.where((dataset['brand'] == "Not Specified") & (dataset['get_name'].str.contains("OT ")), "Johnson Controls", dataset['brand'])
    dataset['brand'] = np.where((dataset['brand'] == "Not Specified") & (dataset['get_name'].str.contains("T-3")), "Johnson Controls", dataset['brand'])
    dataset['brand'] = np.where((dataset['brand'] == "Not Specified") & (dataset['get_name'].str.contains("T-4")), "Johnson Controls", dataset['brand'])
    dataset['brand'] = np.where((dataset['brand'] == "Not Specified") & (dataset['get_name'].str.contains("C-2")), "Johnson Controls", dataset['brand'])
    dataset['brand'] = np.where((dataset['brand'] == "Not Specified") & (dataset['get_name'].str.contains("C-5")), "Johnson Controls", dataset['brand'])
    dataset['brand'] = np.where((dataset['brand'] == "Not Specified") & (dataset['get_name'].str.contains("C-7")), "Johnson Controls", dataset['brand'])
    dataset['brand'] = np.where((dataset['brand'] == "Not Specified") & (dataset['get_name'].str.contains("C-9")), "Johnson Controls", dataset['brand'])
    dataset['brand'] = np.where((dataset['brand'] == "Not Specified") & (dataset['get_name'].str.contains("CD-")), "Johnson Controls", dataset['brand'])
    dataset['brand'] = np.where((dataset['brand'] == "Not Specified") & (dataset['get_name'].str.contains("CSD")), "Johnson Controls", dataset['brand'])
    dataset['brand'] = np.where((dataset['brand'] == "Not Specified") & (dataset['get_name'].str.contains("CSD")), "Johnson Controls", dataset['brand'])
    dataset['brand'] = np.where((dataset['brand'] == "Not Specified") & (dataset['get_name'].str.contains("CTD")), "Johnson Controls", dataset['brand'])
    dataset['brand'] = np.where((dataset['brand'] == "Not Specified") & (dataset['get_name'].str.contains("ADS")), "Johnson Controls", dataset['brand'])
    dataset['brand'] = np.where((dataset['brand'] == "Not Specified") & (dataset['get_name'].str.contains("ADX")), "Johnson Controls", dataset['brand'])
    dataset['brand'] = np.where((dataset['brand'] == "Not Specified") & (dataset['get_name'].str.contains("H-")), "Johnson Controls", dataset['brand'])
    dataset['brand'] = np.where((dataset['brand'] == "Not Specified") & (dataset['get_name'].str.contains("HC-")), "Johnson Controls", dataset['brand'])
    dataset['brand'] = np.where((dataset['brand'] == "Not Specified") & (dataset['get_name'].str.contains("HE-")), "Johnson Controls", dataset['brand'])
    dataset['brand'] = np.where((dataset['brand'] == "Not Specified") & (dataset['get_name'].str.contains("HE-")), "Johnson Controls", dataset['brand'])
    dataset['brand'] = np.where((dataset['brand'] == "Not Specified") & (dataset['get_name'].str.contains("HF4")), "Johnson Controls", dataset['brand'])
    dataset['brand'] = np.where((dataset['brand'] == "Not Specified") & (dataset['get_name'].str.contains("HFC")), "Johnson Controls", dataset['brand'])
    dataset['brand'] = np.where((dataset['brand'] == "Not Specified") & (dataset['get_name'].str.contains("HH-")), "Johnson Controls", dataset['brand'])
    dataset['brand'] = np.where((dataset['brand'] == "Not Specified") & (dataset['get_name'].str.contains("HT ")), "Johnson Controls", dataset['brand'])
    dataset['brand'] = np.where((dataset['brand'] == "Not Specified") & (dataset['get_name'].str.contains("Hx-")), "Johnson Controls", dataset['brand'])
    dataset['brand'] = np.where((dataset['brand'] == "Not Specified") & (dataset['get_name'].str.contains("JP680BA ")), "Johnson Controls", dataset['brand'])
    
    dataset['brand'] = np.where((dataset['brand'] == "Not Specified") & (dataset['get_name'].str.contains("1CG0414")), "Johnson Controls", dataset['brand'])
    
    dataset['brand'] = np.where((dataset['brand'] == "Not Specified") & (dataset['get_name'].str.contains("KZ-4000")), "Johnson Controls", dataset['brand'])
    dataset['brand'] = np.where((dataset['brand'] == "Not Specified") & (dataset['get_name'].str.contains("LCS")), "Johnson Controls", dataset['brand'])
    dataset['brand'] = np.where((dataset['brand'] == "Not Specified") & (dataset['get_name'].str.contains("LN-Light")), "Johnson Controls", dataset['brand'])
    dataset['brand'] = np.where((dataset['brand'] == "Not Specified") & (dataset['get_name'].str.contains("LX ")), "Johnson Controls", dataset['brand'])
    dataset['brand'] = np.where((dataset['brand'] == "Not Specified") & (dataset['get_name'].str.contains("LX-")), "Johnson Controls", dataset['brand'])
    dataset['brand'] = np.where((dataset['brand'] == "Not Specified") & (dataset['get_name'].str.contains("Low Ambient Kit for DSH/DSV A/C Units")), "Johnson Controls", dataset['brand'])
    
    dataset['brand'] = np.where((dataset['brand'] == "Not Specified") & (dataset['get_name'].str.contains("M-2500")), "Johnson Controls", dataset['brand'])
    dataset['brand'] = np.where((dataset['brand'] == "Not Specified") & (dataset['get_name'].str.contains("Mixed Air ")), "Johnson Controls", dataset['brand'])
    dataset['brand'] = np.where((dataset['brand'] == "Not Specified") & (dataset['get_name'].str.contains("MS-BACEOL")), "Johnson Controls", dataset['brand'])
    
    dataset['brand'] = np.where((dataset['brand'] == "Not Specified") & (dataset['get_name'].str.contains("NCE ")), "Johnson Controls", dataset['brand'])
    dataset['brand'] = np.where((dataset['brand'] == "Not Specified") & (dataset['get_name'].str.contains("NS ")), "Johnson Controls", dataset['brand'])
    dataset['brand'] = np.where((dataset['brand'] == "Not Specified") & (dataset['get_name'].str.contains("N-6")), "Johnson Controls", dataset['brand'])
    dataset['brand'] = np.where((dataset['brand'] == "Not Specified") & (dataset['get_name'].str.contains("N-9")), "Johnson Controls", dataset['brand'])
    dataset['brand'] = np.where((dataset['brand'] == "Not Specified") & (dataset['get_name'].str.contains("NS8000")), "Johnson Controls", dataset['brand'])
    dataset['brand'] = np.where((dataset['brand'] == "Not Specified") & (dataset['get_name'].str.contains("NSD1380")), "Johnson Controls", dataset['brand'])
    dataset['brand'] = np.where((dataset['brand'] == "Not Specified") & (dataset['get_name'].str.contains("Accy. I/O - Var. Freq. Drive for 25, 30, 40 Ton package units")), "Johnson Controls", dataset['brand'])
    
    
    
    dataset['brand'] = np.where((dataset['brand'] == "Not Specified") & (dataset['get_name'].str.contains("OLS-")), "Johnson Controls", dataset['brand'])
    dataset['brand'] = np.where((dataset['brand'] == "Not Specified") & (dataset['get_name'].str.contains("Operator Workstation")), "Johnson Controls", dataset['brand'])
    
    
    dataset['brand'] = np.where((dataset['brand'] == "Not Specified") & (dataset['get_name'].str.contains("Pneumatic Control System")), "Johnson Controls", dataset['brand'])
    dataset['brand'] = np.where((dataset['brand'] == "Not Specified") & (dataset['get_name'].str.contains("P-3")), "Johnson Controls", dataset['brand'])
    dataset['brand'] = np.where((dataset['brand'] == "Not Specified") & (dataset['get_name'].str.contains("P-5")), "Johnson Controls", dataset['brand'])
    dataset['brand'] = np.where((dataset['brand'] == "Not Specified") & (dataset['get_name'].str.contains("P-7")), "Johnson Controls", dataset['brand'])
    dataset['brand'] = np.where((dataset['brand'] == "Not Specified") & (dataset['get_name'].str.contains("P-8")), "Johnson Controls", dataset['brand'])
    dataset['brand'] = np.where((dataset['brand'] == "Not Specified") & (dataset['get_name'].str.contains("R-2")), "Johnson Controls", dataset['brand'])
    dataset['brand'] = np.where((dataset['brand'] == "Not Specified") & (dataset['get_name'].str.contains("R-3")), "Johnson Controls", dataset['brand'])
    dataset['brand'] = np.where((dataset['brand'] == "Not Specified") & (dataset['get_name'].str.contains("R-4")), "Johnson Controls", dataset['brand'])
    dataset['brand'] = np.where((dataset['brand'] == "Not Specified") & (dataset['get_name'].str.contains("RG Series")), "Johnson Controls", dataset['brand'])
    dataset['brand'] = np.where((dataset['brand'] == "Not Specified") & (dataset['get_name'].str.contains("RH Series")), "Johnson Controls", dataset['brand'])
    dataset['brand'] = np.where((dataset['brand'] == "Not Specified") & (dataset['get_name'].str.contains("RPM1600")), "Johnson Controls", dataset['brand'])
    
    dataset['brand'] = np.where((dataset['brand'] == "Not Specified") & (dataset['get_name'].str.contains("S-2300 ")), "Johnson Controls", dataset['brand'])
    dataset['brand'] = np.where((dataset['brand'] == "Not Specified") & (dataset['get_name'].str.contains("Smart Equipment Controls")), "Johnson Controls", dataset['brand'])
    
    dataset['brand'] = np.where((dataset['brand'] == "Not Specified") & (dataset['get_name'].str.contains("T-2")), "Johnson Controls", dataset['brand'])
    dataset['brand'] = np.where((dataset['brand'] == "Not Specified") & (dataset['get_name'].str.contains("T-5")), "Johnson Controls", dataset['brand'])
    dataset['brand'] = np.where((dataset['brand'] == "Not Specified") & (dataset['get_name'].str.contains("TE-6")), "Johnson Controls", dataset['brand'])
    dataset['brand'] = np.where((dataset['brand'] == "Not Specified") & (dataset['get_name'].str.contains("TE-7")), "Johnson Controls", dataset['brand'])
    dataset['brand'] = np.where((dataset['brand'] == "Not Specified") & (dataset['get_name'].str.contains("TE7")), "Johnson Controls", dataset['brand'])
    dataset['brand'] = np.where((dataset['brand'] == "Not Specified") & (dataset['get_name'].str.contains("TEP")), "Johnson Controls", dataset['brand'])
    dataset['brand'] = np.where((dataset['brand'] == "Not Specified") & (dataset['get_name'].str.contains("Thermistor")), "Johnson Controls", dataset['brand'])
    
    dataset['brand'] = np.where((dataset['brand'] == "Not Specified") & (dataset['get_name'].str.contains("TM")), "Johnson Controls", dataset['brand'])
    dataset['brand'] = np.where((dataset['brand'] == "Not Specified") & (dataset['get_name'].str.contains("TRUERH")), "Johnson Controls", dataset['brand'])
    dataset['brand'] = np.where((dataset['brand'] == "Not Specified") & (dataset['get_name'].str.contains("TrueRH")), "Johnson Controls", dataset['brand'])
    
    dataset['brand'] = np.where((dataset['brand'] == "Not Specified") & (dataset['get_name'].str.contains("U-AI")), "Johnson Controls", dataset['brand'])
    dataset['brand'] = np.where((dataset['brand'] == "Not Specified") & (dataset['get_name'].str.contains("UAI")), "Johnson Controls", dataset['brand'])
    dataset['brand'] = np.where((dataset['brand'] == "Not Specified") & (dataset['get_name'].str.contains("UCB")), "Johnson Controls", dataset['brand'])
    
    dataset['brand'] = np.where((dataset['brand'] == "Not Specified") & (dataset['get_name'].str.contains("Y99")), "Johnson Controls", dataset['brand'])
    
    dataset['brand'] = np.where((dataset['brand'] == "Not Specified") & (dataset['get_name'].str.contains("Wireless Field Bus Coordinator")), "Johnson Controls", dataset['brand'])
    dataset['brand'] = np.where((dataset['brand'] == "Not Specified") & (dataset['get_name'].str.contains("What's New")), "Johnson Controls", dataset['brand'])
    dataset['brand'] = np.where((dataset['brand'] == "Not Specified") & (dataset['get_name'].str.contains("WRS")), "Johnson Controls", dataset['brand'])
    dataset['brand'] = np.where((dataset['brand'] == "Not Specified") & (dataset['get_name'].str.contains("WRZ")), "Johnson Controls", dataset['brand'])
    dataset['brand'] = np.where((dataset['brand'] == "Not Specified") & (dataset['get_name'].str.contains("W351")), "Johnson Controls", dataset['brand'])
    
    
    dataset['brand'] = np.where((dataset['brand'] == "Not Specified") & (dataset['get_name'].str.contains("ZFR")), "Johnson Controls", dataset['brand'])
    
    
    dataset['brand'] = np.where((dataset['brand'] == "Not Specified") & (dataset['get_name'].str.contains("Mobile Access Portal")), "Johnson Controls", dataset['brand'])
    
    
    
    
    # YORK
    
    dataset['brand'] = np.where((dataset['brand'] == "Not Specified") & (dataset['get_name'].str.contains("YORK")), "YORK", dataset['brand'])
    dataset['brand'] = np.where((dataset['brand'] == "Not Specified") & (dataset['get_name'].str.contains("York")), "YORK", dataset['brand'])
    
    
    
    
    dataset['brand'] = np.where((dataset['brand'] == "Not Specified") & (dataset['get_name'].str.contains("Bitzer")), "YORK", dataset['brand'])
    
    
    
    dataset['brand'] = np.where((dataset['brand'] == "Not Specified") & (dataset['get_name'].str.contains("CYK")), "YORK", dataset['brand'])
    dataset['brand'] = np.where((dataset['brand'] == "Not Specified") & (dataset['get_name'].str.contains("Chiller")), "YORK", dataset['brand'])
    dataset['brand'] = np.where((dataset['brand'] == "Not Specified") & (dataset['get_name'].str.contains("Copeland Compressor")), "YORK", dataset['brand'])
    dataset['brand'] = np.where((dataset['brand'] == "Not Specified") & (dataset['get_name'].str.contains("DX Evaporator ")), "YORK", dataset['brand'])
    dataset['brand'] = np.where((dataset['brand'] == "Not Specified") & (dataset['get_name'].str.contains("Gate Driver Test Mode")), "YORK", dataset['brand'])
    
    
    dataset['brand'] = np.where((dataset['brand'] == "Not Specified") & (dataset['get_name'].str.contains("HYP")), "YORK", dataset['brand'])
    
    
    dataset['brand'] = np.where((dataset['brand'] == "Not Specified") & (dataset['get_name'].str.contains("IGBT / Diode")), "YORK", dataset['brand'])
    dataset['brand'] = np.where((dataset['brand'] == "Not Specified") & (dataset['get_name'].str.contains("KVS Stepper")), "YORK", dataset['brand'])
    
    dataset['brand'] = np.where((dataset['brand'] == "Not Specified") & (dataset['get_name'].str.contains("Liquid Cooled")), "YORK", dataset['brand'])
    
    
    dataset['brand'] = np.where((dataset['brand'] == "Not Specified") & (dataset['get_name'].str.contains("MV VSD")), "YORK", dataset['brand'])
    dataset['brand'] = np.where((dataset['brand'] == "Not Specified") & (dataset['get_name'].str.contains("Millennium")), "YORK", dataset['brand'])
    dataset['brand'] = np.where((dataset['brand'] == "Not Specified") & (dataset['get_name'].str.contains("Medium Voltage Variable Speed Drive ")), "YORK", dataset['brand'])
    dataset['brand'] = np.where((dataset['brand'] == "Not Specified") & (dataset['get_name'].str.contains("Megger Testing 3-Phase Motors")), "YORK", dataset['brand'])
    dataset['brand'] = np.where((dataset['brand'] == "Not Specified") & (dataset['get_name'].str.contains("Multi-Unit Sequencing Installation Operation & Maintenance")), "YORK", dataset['brand'])
    
    dataset['brand'] = np.where((dataset['brand'] == "Not Specified") & (dataset['get_name'].str.contains("OM ")), "YORK", dataset['brand'])
    dataset['brand'] = np.where((dataset['brand'] == "Not Specified") & (dataset['get_name'].str.contains("Optiview")), "YORK", dataset['brand'])
    dataset['brand'] = np.where((dataset['brand'] == "Not Specified") & (dataset['get_name'].str.contains("OptiView")), "YORK", dataset['brand'])
    
    dataset['brand'] = np.where((dataset['brand'] == "Not Specified") & (dataset['get_name'].str.contains("SC-EQ Firmware")), "YORK", dataset['brand'])
    dataset['brand'] = np.where((dataset['brand'] == "Not Specified") & (dataset['get_name'].str.contains("Single Stage Centrifugal Compressor")), "YORK", dataset['brand'])
    dataset['brand'] = np.where((dataset['brand'] == "Not Specified") & (dataset['get_name'].str.contains("Small Tonnage Split Systems")), "YORK", dataset['brand'])
    dataset['brand'] = np.where((dataset['brand'] == "Not Specified") & (dataset['get_name'].str.contains("Solid State Starter Style A & B")), "YORK", dataset['brand'])
    
    dataset['brand'] = np.where((dataset['brand'] == "Not Specified") & (dataset['get_name'].str.contains("SSS")), "YORK", dataset['brand'])
    dataset['brand'] = np.where((dataset['brand'] == "Not Specified") & (dataset['get_name'].str.contains("System Status Printers, & Operation")), "YORK", dataset['brand'])
    
    dataset['brand'] = np.where((dataset['brand'] == "Not Specified") & (dataset['get_name'].str.contains("Titan")), "YORK", dataset['brand'])
    dataset['brand'] = np.where((dataset['brand'] == "Not Specified") & (dataset['get_name'].str.contains("Tube Expansion Procedures ")), "YORK", dataset['brand'])
    dataset['brand'] = np.where((dataset['brand'] == "Not Specified") & (dataset['get_name'].str.contains("Tube Extraction Procedures ")), "YORK", dataset['brand'])
    
    dataset['brand'] = np.where((dataset['brand'] == "Not Specified") & (dataset['get_name'].str.contains("VSD ")), "YORK", dataset['brand'])
    
    
    dataset['brand'] = np.where((dataset['brand'] == "Not Specified") & (dataset['get_name'].str.contains("YB")), "YORK", dataset['brand'])
    dataset['brand'] = np.where((dataset['brand'] == "Not Specified") & (dataset['get_name'].str.contains("YCAL")), "YORK", dataset['brand'])
    dataset['brand'] = np.where((dataset['brand'] == "Not Specified") & (dataset['get_name'].str.contains("YCAS")), "YORK", dataset['brand'])
    dataset['brand'] = np.where((dataset['brand'] == "Not Specified") & (dataset['get_name'].str.contains("YCAV")), "YORK", dataset['brand'])
    dataset['brand'] = np.where((dataset['brand'] == "Not Specified") & (dataset['get_name'].str.contains("YCIV")), "YORK", dataset['brand'])
    dataset['brand'] = np.where((dataset['brand'] == "Not Specified") & (dataset['get_name'].str.contains("YCRS")), "YORK", dataset['brand'])
    dataset['brand'] = np.where((dataset['brand'] == "Not Specified") & (dataset['get_name'].str.contains("YCWS")), "YORK", dataset['brand'])
    dataset['brand'] = np.where((dataset['brand'] == "Not Specified") & (dataset['get_name'].str.contains("YD ")), "YORK", dataset['brand'])
    dataset['brand'] = np.where((dataset['brand'] == "Not Specified") & (dataset['get_name'].str.contains("YDHA")), "YORK", dataset['brand'])
    dataset['brand'] = np.where((dataset['brand'] == "Not Specified") & (dataset['get_name'].str.contains("YDHD")), "YORK", dataset['brand'])
    dataset['brand'] = np.where((dataset['brand'] == "Not Specified") & (dataset['get_name'].str.contains("YG ")), "YORK", dataset['brand'])
    dataset['brand'] = np.where((dataset['brand'] == "Not Specified") & (dataset['get_name'].str.contains("YHAU ")), "YORK", dataset['brand'])
    dataset['brand'] = np.where((dataset['brand'] == "Not Specified") & (dataset['get_name'].str.contains("YIA ")), "YORK", dataset['brand'])
    dataset['brand'] = np.where((dataset['brand'] == "Not Specified") & (dataset['get_name'].str.contains("YK ")), "YORK", dataset['brand'])
    dataset['brand'] = np.where((dataset['brand'] == "Not Specified") & (dataset['get_name'].str.contains("YK, ")), "YORK", dataset['brand'])
    dataset['brand'] = np.where((dataset['brand'] == "Not Specified") & (dataset['get_name'].str.contains("YKEP ")), "YORK", dataset['brand'])
    dataset['brand'] = np.where((dataset['brand'] == "Not Specified") & (dataset['get_name'].str.contains("YLAA ")), "YORK", dataset['brand'])
    dataset['brand'] = np.where((dataset['brand'] == "Not Specified") & (dataset['get_name'].str.contains("YLAA,")), "YORK", dataset['brand'])
    dataset['brand'] = np.where((dataset['brand'] == "Not Specified") & (dataset['get_name'].str.contains("YMC2 ")), "YORK", dataset['brand'])
    dataset['brand'] = np.where((dataset['brand'] == "Not Specified") & (dataset['get_name'].str.contains("YPAL ")), "YORK", dataset['brand'])
    dataset['brand'] = np.where((dataset['brand'] == "Not Specified") & (dataset['get_name'].str.contains("YR ")), "YORK", dataset['brand'])
    dataset['brand'] = np.where((dataset['brand'] == "Not Specified") & (dataset['get_name'].str.contains("YS ")), "YORK", dataset['brand'])
    dataset['brand'] = np.where((dataset['brand'] == "Not Specified") & (dataset['get_name'].str.contains("YST")), "YORK", dataset['brand'])
    dataset['brand'] = np.where((dataset['brand'] == "Not Specified") & (dataset['get_name'].str.contains("YT ")), "YORK", dataset['brand'])
    
    
    dataset['brand'] = np.where((dataset['brand'] == "Not Specified") & (dataset['get_name'].str.contains("YVAA ")), "YORK", dataset['brand'])
    dataset['brand'] = np.where((dataset['brand'] == "Not Specified") & (dataset['get_name'].str.contains("YVWA")), "YORK", dataset['brand'])
    dataset['brand'] = np.where((dataset['brand'] == "Not Specified") & (dataset['get_name'].str.contains("YVFA ")), "YORK", dataset['brand'])
    dataset['brand'] = np.where((dataset['brand'] == "Not Specified") & (dataset['get_name'].str.contains("YZ ")), "YORK", dataset['brand'])
    
    
    
    
    
    
    dataset['brand'] = np.where((dataset['brand'] == "Not Specified") & (dataset['get_name'].str.contains("Air Handling Unit")), "Facility Explorer", dataset['brand'])
    dataset['brand'] = np.where((dataset['brand'] == "Not Specified") & (dataset['get_name'].str.contains("Commercial Zoning")), "Facility Explorer", dataset['brand'])
    
    
    
    dataset['brand'] = np.where((dataset['brand'] == "Not Specified") & (dataset['get_name'].str.contains("Fan Coil Unit")), "Facility Explorer", dataset['brand'])
    dataset['brand'] = np.where((dataset['brand'] == "Not Specified") & (dataset['get_name'].str.contains("FX ")), "Facility Explorer", dataset['brand'])
    
    dataset['brand'] = np.where((dataset['brand'] == "Not Specified") & (dataset['get_name'].str.contains("FX ")), "Facility Explorer", dataset['brand'])
    dataset['brand'] = np.where((dataset['brand'] == "Not Specified") & (dataset['get_name'].str.contains("FX-")), "Facility Explorer", dataset['brand'])
    dataset['brand'] = np.where((dataset['brand'] == "Not Specified") & (dataset['get_name'].str.contains("FX0")), "Facility Explorer", dataset['brand'])
    dataset['brand'] = np.where((dataset['brand'] == "Not Specified") & (dataset['get_name'].str.contains("FX1")), "Facility Explorer", dataset['brand'])
    dataset['brand'] = np.where((dataset['brand'] == "Not Specified") & (dataset['get_name'].str.contains("FX2")), "Facility Explorer", dataset['brand'])
    dataset['brand'] = np.where((dataset['brand'] == "Not Specified") & (dataset['get_name'].str.contains("FX4")), "Facility Explorer", dataset['brand'])
    dataset['brand'] = np.where((dataset['brand'] == "Not Specified") & (dataset['get_name'].str.contains("FX7")), "Facility Explorer", dataset['brand'])
    dataset['brand'] = np.where((dataset['brand'] == "Not Specified") & (dataset['get_name'].str.contains("FX8")), "Facility Explorer", dataset['brand'])
    dataset['brand'] = np.where((dataset['brand'] == "Not Specified") & (dataset['get_name'].str.contains("FXR")), "Facility Explorer", dataset['brand'])
    dataset['brand'] = np.where((dataset['brand'] == "Not Specified") & (dataset['get_name'].str.contains("FXV")), "Facility Explorer", dataset['brand'])
    dataset['brand'] = np.where((dataset['brand'] == "Not Specified") & (dataset['get_name'].str.contains("Hot Water System")), "Facility Explorer", dataset['brand'])
    
    
    dataset['brand'] = np.where((dataset['brand'] == "Not Specified") & (dataset['get_name'].str.contains("LP-KI")), "Facility Explorer", dataset['brand'])
    dataset['brand'] = np.where((dataset['brand'] == "Not Specified") & (dataset['get_name'].str.contains("MD20")), "Facility Explorer", dataset['brand'])
    dataset['brand'] = np.where((dataset['brand'] == "Not Specified") & (dataset['get_name'].str.contains("Network Room Module")), "Facility Explorer", dataset['brand'])
    dataset['brand'] = np.where((dataset['brand'] == "Not Specified") & (dataset['get_name'].str.contains("NDIO")), "Facility Explorer", dataset['brand'])
    dataset['brand'] = np.where((dataset['brand'] == "Not Specified") & (dataset['get_name'].str.contains("Option Card")), "Facility Explorer", dataset['brand'])
    dataset['brand'] = np.where((dataset['brand'] == "Not Specified") & (dataset['get_name'].str.contains("Rooftop Top Unit")), "Facility Explorer", dataset['brand'])
    dataset['brand'] = np.where((dataset['brand'] == "Not Specified") & (dataset['get_name'].str.contains("Unit Ventilator (UV) Controller")), "Facility Explorer", dataset['brand'])
    dataset['brand'] = np.where((dataset['brand'] == "Not Specified") & (dataset['get_name'].str.contains("VAV Box Balancing Sensor")), "Facility Explorer", dataset['brand'])
    dataset['brand'] = np.where((dataset['brand'] == "Not Specified") & (dataset['get_name'].str.contains("VRF Smart Gateway")), "Facility Explorer", dataset['brand'])
    
    
    
    
    
    
    dataset['brand'] = np.where((dataset['brand'] == "Not Specified") & (dataset['get_name'].str.contains("A4903")), "Autocall", dataset['brand'])
    dataset['brand'] = np.where((dataset['brand'] == "Not Specified") & (dataset['get_name'].str.contains("CO SSD Base CORC")), "Autocall", dataset['brand'])
    
    dataset['brand'] = np.where((dataset['brand'] == "Not Specified") & (dataset['get_name'].str.contains("TrueAlert")), "Autocall", dataset['brand'])
    
    
    
    
    
    dataset['brand'] = np.where((dataset['brand'] == "Not Specified") & (dataset['get_name'].str.contains("2084")), "Simplex", dataset['brand'])
    dataset['brand'] = np.where((dataset['brand'] == "Not Specified") & (dataset['get_name'].str.contains("2081")), "Simplex", dataset['brand'])
    dataset['brand'] = np.where((dataset['brand'] == "Not Specified") & (dataset['get_name'].str.contains("4009")), "Simplex", dataset['brand'])
    dataset['brand'] = np.where((dataset['brand'] == "Not Specified") & (dataset['get_name'].str.contains("4090")), "Simplex", dataset['brand'])
    dataset['brand'] = np.where((dataset['brand'] == "Not Specified") & (dataset['get_name'].str.contains("4099")), "Simplex", dataset['brand'])
    dataset['brand'] = np.where((dataset['brand'] == "Not Specified") & (dataset['get_name'].str.contains("4100")), "Simplex", dataset['brand'])
    dataset['brand'] = np.where((dataset['brand'] == "Not Specified") & (dataset['get_name'].str.contains("4602")), "Simplex", dataset['brand'])
    dataset['brand'] = np.where((dataset['brand'] == "Not Specified") & (dataset['get_name'].str.contains("ES-PS and ES-XPS")), "Simplex", dataset['brand'])
    dataset['brand'] = np.where((dataset['brand'] == "Not Specified") & (dataset['get_name'].str.contains("LED Strobe, Wall Weatherproof")), "Simplex", dataset['brand'])
    
    
    
    dataset['brand'] = np.where((dataset['brand'] == "Not Specified") & (dataset['get_name'].str.contains("Facility Explorer ")), "Facility Explorer", dataset['brand'])
    dataset['brand'] = np.where((dataset['brand'] == "Not Specified") & (dataset['get_name'].str.contains("Champion ")), "Champion", dataset['brand'])
    dataset['brand'] = np.where((dataset['brand'] == "Not Specified") & (dataset['get_name'].str.contains("Coleman ")), "Coleman", dataset['brand'])
    dataset['brand'] = np.where((dataset['brand'] == "Not Specified") & (dataset['get_name'].str.contains("Fraser-Johnston ")), "Fraser-Johnston", dataset['brand'])
    dataset['brand'] = np.where((dataset['brand'] == "Not Specified") & (dataset['get_name'].str.contains("Johnson Controls ")), "Johnson Controls", dataset['brand'])
    dataset['brand'] = np.where((dataset['brand'] == "Not Specified") & (dataset['get_name'].str.contains("Luxaire ")), "Luxaire", dataset['brand'])
    dataset['brand'] = np.where((dataset['brand'] == "Not Specified") & (dataset['get_name'].str.contains("TempMaster ")), "TempMaster", dataset['brand'])
    dataset['brand'] = np.where((dataset['brand'] == "Not Specified") & (dataset['get_name'].str.contains("Facility Explorer")), "Facility Explorer", dataset['brand'])
    
    
    ## MANUAL FIX
    dataset['brand'] = np.where(dataset['document_link'] == "/viewer/document/TCNCraBPZLaItV3Ek6xG2g", "Facility Explorer", dataset['brand'])
    dataset['brand'] = np.where(dataset['document_link'] == "/viewer/document/HnZ14~UAOaaIZVs73ZjUPQ", "Facility Explorer", dataset['brand'])
    
    
    
    
    dataset['product_name'] = np.where(dataset['product_name'] == "Not Specified", dataset['get_name'], dataset['product_name'])
    
    dataset = dataset.drop(['get_name'], axis=1)
    
    
    
    # SOME MISSING BRANDS
    dataset['brand'] = np.where(dataset['product_name'] == "Multi-Unit Sequencing", "YORK", dataset['brand'])
    dataset['brand'] = np.where(dataset['product_name'] == "System Status Printers", "YORK", dataset['brand'])
    dataset['brand'] = np.where(dataset['product_name'] == "YD", "YORK", dataset['brand'])
    dataset['brand'] = np.where(dataset['product_name'] == "YK", "YORK", dataset['brand'])
    dataset['brand'] = np.where(dataset['product_name'] == "YMC2-Magnetic Bearing Control", "YORK", dataset['brand'])
    dataset['brand'] = np.where(dataset['product_name'] == "YR", "YORK", dataset['brand'])
    dataset['brand'] = np.where(dataset['product_name'] == "YS", "YORK", dataset['brand'])
    dataset['brand'] = np.where(dataset['product_name'] == "YT", "YORK", dataset['brand'])
    dataset['brand'] = np.where(dataset['product_name'] == "ZNT06-T12", "TempMaster", dataset['brand'])
    
    
    dataset['product_name'] = dataset['product_name'].str.strip()
    
    
    
    # CHECK
#    missing_brands = dataset[dataset['brand'] == "Not Specified"]
#    missing_product_name = dataset[dataset['product_name'] == "Not Specified"]
   
    
    dataset.to_csv("documents_gaps_filled.csv",  encoding='utf-8-sig', index=False)
    
    return dataset




data = fill_brand_and_product_gaps("documents_cleaned.csv")








brands = list(data['brand'].unique())





















