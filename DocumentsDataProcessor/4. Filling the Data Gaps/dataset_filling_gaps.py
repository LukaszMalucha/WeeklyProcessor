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
    
    tryit = dataset[dataset['topic_title'].str.contains("-3S Series")]
    
    # REPLACE
    dataset['get_name'] = dataset['get_name'].str.replace(" Refrigerants -12, -22 and 502", "")
    dataset['get_name'] = dataset['get_name'].str.replace(" Refrigerants -12, -22, and 502", "")
    dataset['get_name'] = dataset['get_name'].str.replace(" Refrigerants -12 and -22", "")
    dataset['get_name'] = dataset['get_name'].str.replace(" Refrigerants -12, -22, 502 and -717", "")
    dataset['get_name'] = dataset['get_name'].str.replace(" Refrigerants -12, -22, 502 and -717", "")
    dataset['get_name'] = dataset['get_name'].str.replace(" Refrigerant -22, SS42A, SS62A, SS82A", "")
    
    
    dataset['get_name'] = dataset['get_name'].str.replace(" Installation Guide", "")
    dataset['get_name'] = dataset['get_name'].str.replace("Operation and Maintenance", "")
    dataset['get_name'] = dataset['get_name'].str.replace(" Operating Instructions", "")
    dataset['get_name'] = dataset['get_name'].str.replace(" User’s Guide", "")
    dataset['get_name'] = dataset['get_name'].str.replace(" Express User Guide", "")
    dataset['get_name'] = dataset['get_name'].str.replace(" Service Instructions ", "")
    dataset['get_name'] = dataset['get_name'].str.replace(" Administration Guide", "")
    dataset['get_name'] = dataset['get_name'].str.replace("General Specifications", "")
    dataset['get_name'] = dataset['get_name'].str.replace(" Replacement Procedure Small Tonnage (SI0198)", "")
    dataset['get_name'] = dataset['get_name'].str.replace("Assembly Installation Guide", "")
    dataset['get_name'] = dataset['get_name'].str.replace("Networks Installation Instructions and Troubleshooting Guide", "")
    dataset['get_name'] = dataset['get_name'].str.replace(", and", " and ")
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
    dataset['get_name'] = dataset['get_name'].str.replace(" Integration Guide", "")
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
    dataset['get_name'] = dataset['get_name'].str.replace("Solution-to-Solution Heat Exchange End Sheet Deflection", "")
    dataset['get_name'] = dataset['get_name'].str.replace("Elimination of BZT During Commissioning", "")
    dataset['get_name'] = dataset['get_name'].str.replace("Changes in Coolant Procedures and for ", "")
    dataset['get_name'] = dataset['get_name'].str.replace(" - Discontinuation of PressurePak Enhancement Product", "")
    dataset['get_name'] = dataset['get_name'].str.replace(" Design Change", "")
    dataset['get_name'] = dataset['get_name'].str.replace(" Design Change", "")
    dataset['get_name'] = dataset['get_name'].str.replace("While On A Service Call Or When Replacing A ", "")
    dataset['get_name'] = dataset['get_name'].str.replace(" Method to Diagnose DXS Compressor Unloading Problems", "")
    dataset['get_name'] = dataset['get_name'].str.replace(" Intermittent High Motor Current Faults", "")
    dataset['get_name'] = dataset['get_name'].str.replace(" - VSD Power Conduit Cutout Sealing Procedure", "")
    dataset['get_name'] = dataset['get_name'].str.replace(" Changes in Rapture Disks on Absorption Units", "")
    dataset['get_name'] = dataset['get_name'].str.replace(" Lithium Bromide Sample Testing", "")
    dataset['get_name'] = dataset['get_name'].str.replace(" Torque Requirements and Procedure for Sealing Shell and Water Side Gaskets", "")
    dataset['get_name'] = dataset['get_name'].str.replace(" Adjusting and Calibrating", "")
    dataset['get_name'] = dataset['get_name'].str.replace(" Specialfor Mix-Match Units", "")
    dataset['get_name'] = dataset['get_name'].str.replace(" Correction for Part Number to Fuses Used in 1278A HYP Model VSD", "")
    dataset['get_name'] = dataset['get_name'].str.replace(" - Solution and Refrigerant Charges", "")
    dataset['get_name'] = dataset['get_name'].str.replace(" Guide", "")
    dataset['get_name'] = dataset['get_name'].str.replace(" Cutout Template", "")
    dataset['get_name'] = dataset['get_name'].str.replace(" Application Integration", "")
    dataset['get_name'] = dataset['get_name'].str.replace(" Submittal Sheet", "")
    dataset['get_name'] = dataset['get_name'].str.replace("Renewal Parts Manual", "Renewal Parts")
    dataset['get_name'] = dataset['get_name'].str.replace("Outputs", "Output")
    dataset['get_name'] = dataset['get_name'].str.replace("Output", "Outputs")
    dataset['get_name'] = dataset['get_name'].str.replace(" Assembly", "")
    dataset['get_name'] = dataset['get_name'].str.replace(" Subassembly", "")
    dataset['get_name'] = dataset['get_name'].str.replace(" Catalog Page", "")
    dataset['get_name'] = dataset['get_name'].str.replace("Transducers", "Transducer")
    dataset['get_name'] = dataset['get_name'].str.replace("Transducer", "Transducers")
    dataset['get_name'] = dataset['get_name'].str.replace("Controllers", "Controller")
    dataset['get_name'] = dataset['get_name'].str.replace("Controller", "Controllers")
    dataset['get_name'] = dataset['get_name'].str.replace(" Assembly", "")
    dataset['get_name'] = dataset['get_name'].str.replace("- Metastat", "")
    dataset['get_name'] = dataset['get_name'].str.replace(" Bulletin", "")
    dataset['get_name'] = dataset['get_name'].str.replace(" Compatibility Chart", "")
    dataset['get_name'] = dataset['get_name'].str.replace("Installation Manual: ", "")
    dataset['get_name'] = dataset['get_name'].str.replace(" - Listings and Approvals", "")
    
    
    
    
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
    
    
    dataset['brand'] = np.where(dataset['document_link'] == "/viewer/document/lGAyVRovyBLjhD9ZOCeYQQ", "Johnson Controls", dataset['brand'])
    dataset['brand'] = np.where(dataset['document_link'] == "/viewer/document/3vU~yz9aMbRGka0dz6UgRw", "Johnson Controls", dataset['brand'])
    dataset['brand'] = np.where(dataset['document_link'] == "/viewer/document/hy16wOTDQOwUTrcR7y7itA", "Johnson Controls", dataset['brand'])
    
    
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
    
    
    
    dataset['get_name'] = dataset['get_name'].str.replace("YK Compressors YDHA, YDHB and YDHG High Speed Forward Thrust (029-20896-002, 029-20900-002) and Journal Bearing (064-48207-000, 064-48208-000) Design Change, Compressor", "YK")
    
    
    
    
    
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
    
    
    
    
    
    """
    CLEANINGS
    """
    dataset['product_name'] = np.where(dataset['product_name'].str.contains('Installing Ferrite Beads with "Wired" MEDIA Cards'), "4020 Fire Alarm Control Panel, 4100 Fire Alarm Control Panel, 4120 Fire Alarm Control Panel, 4010ES Fire Alarm Control Panel", dataset['product_name'])
    
    
    
    
    
    """
    AD HOC FINDINGS FROM MARCH
    """
    
    # DOUCMENT PART NUMBER HAVING PARENTHESES
    dataset['document_number'] = dataset['document_number'].str.replace("\(\)", "")
    dataset['document_part_number'] = dataset['document_part_number'].str.replace("\(\)", "")
    
    
    # YORK FROM MARCH
    
    dataset['product_name'] = np.where(dataset['product_name'].str.contains("Chillers with K3, K4, and K7 Compressors"), "Chillers", dataset['product_name'])
    dataset['product_name'] = np.where(dataset['product_name'].str.contains("YVAA, YLAA, and YPAL Micro Channel Coil"), "YVAA, YLAA, YPAL", dataset['product_name'])
    dataset['product_name'] = np.where(dataset['product_name'].str.contains("YLAA, YLUA, YCAL, and YCUL "), "YLAA, YLUA, YCAL, YCUL", dataset['product_name'])
    dataset['product_name'] = np.where(dataset['product_name'].str.contains("YCAV, YCIV , YLAA, and YVAA Chillers QTI"), "YCAV, YCIV, YLAA, YVAA", dataset['product_name'])
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
    dataset['product_name'] = np.where(dataset['product_name'].str.contains("YK High Speed Forward Thrust "), "YK", dataset['product_name'])
    
    
    
    
    
    
    
    # OTHER FIX
    
    dataset['product_name'] = np.where(dataset['product_name'].str.contains("AMB-2010 and AMB -1100 Anti-theft System Deactivator"), "AMB-2010  Anti-theft System Deactivator, AMB-1100 Anti-theft System Deactivator", dataset['product_name'])
    dataset['product_name'] = np.where(dataset['product_name'].str.contains("YS "), "YR Chillers", dataset['product_name'])
    dataset['product_name'] = np.where(dataset['product_name'] == "UltraMax System", "UltraMax Systems", dataset['product_name'])
    dataset['product_name'] = np.where(dataset['product_name'] == " 064-48207-000", "YK", dataset['product_name'])
    dataset['product_name'] = np.where(dataset['product_name'] == " 4100/4120-Series VESDA Interface Cards", "4100,4120", dataset['product_name'])
    
    
    # CLEAN RECREATED TITLES
    
    dataset['product_name'] = np.where(dataset['product_name'].str.contains("ADS/ADX"), "ADS,ADX", dataset['product_name'])
    
    
    
    dataset['product_name'] = np.where(dataset['product_name'].str.contains("YCWS 0100-0140, 0180-0240 "), "YCWS", dataset['product_name'])
    dataset['product_name'] = np.where(dataset['product_name'].str.contains("YCAV 0569, 0639, 0679, 0719, 0739, 0819, 0889, 0969 "), "YCAV", dataset['product_name'])
    dataset['product_name'] = np.where(dataset['product_name'].str.contains("York Model YDTL 108, 120, & 126"), "YDTL", dataset['product_name'])
    dataset['product_name'] = np.where(dataset['product_name'].str.contains("SSS, MVSD, EMS Variable Speed Drive, 292 HP – 50 Hz, 400VAC, 351 HP – 60 Hz, 460VAC, 419 HP – 50 Hz, 400VAC, 424 HP – 60 Hz, 575VAC, 503 HP – 60 Hz, 460VAC, 608 HP – 60 Hz, 575VAC, Renewal"), "Variable Speed Drive", dataset['product_name'])
    dataset['product_name'] = np.where(dataset['product_name'].str.contains("YK Medium Voltage Variable Speed Drive"), "Variable Speed Drive", dataset['product_name'])
    dataset['product_name'] = np.where(dataset['product_name'].str.contains("YK Medium Voltage Variable Speed Drives"), "Variable Speed Drive", dataset['product_name'])
    
    
    
    tryit = dataset[dataset['product_name'].str.contains("APS-100")]
    
    
    # PRODUCT UNIFICATION
    
    
    dataset['product_name'] = np.where(dataset['product_name'].str.contains("APS-1000"), "APS-100 Exit Anti-Theft System", dataset['product_name'])
    dataset['product_name'] = np.where(dataset['product_name'].str.contains(" DACT"), "Digital Alarm Communicating Transmitter", dataset['product_name'])
    dataset['product_name'] = np.where(dataset['product_name'].str.contains("2081 Series "), "Digital Alarm Communicating Transmitter", dataset['product_name'])
    dataset['product_name'] = np.where(dataset['product_name'].str.contains("2081-9046 "), "Digital Alarm Communicating Transmitter", dataset['product_name'])
    dataset['product_name'] = np.where(dataset['product_name'].str.contains("2084 Series"), "Digital Alarm Communicating Transmitter", dataset['product_name'])
    dataset['product_name'] = np.where(dataset['product_name'].str.contains("2084-9023 "), "Digital Alarm Communicating Transmitter", dataset['product_name'])
    dataset['product_name'] = np.where(dataset['product_name'].str.contains("2098 Series "), "Digital Alarm Communicating Transmitter", dataset['product_name'])
    dataset['product_name'] = np.where(dataset['product_name'].str.contains("2098 Series "), "Digital Alarm Communicating Transmitter", dataset['product_name'])
    dataset['product_name'] = np.where(dataset['product_name'].str.contains("2098-9829C "), "Digital Alarm Communicating Transmitter", dataset['product_name'])
    dataset['product_name'] = np.where(dataset['product_name'].str.contains("2099 Series "), "Digital Alarm Communicating Transmitter", dataset['product_name'])
    dataset['product_name'] = np.where(dataset['product_name'].str.contains("2099-9136 "), "Digital Alarm Communicating Transmitter", dataset['product_name'])
    dataset['product_name'] = np.where(dataset['product_name'].str.contains("2190-9173 "), "Digital Alarm Communicating Transmitter", dataset['product_name'])
    dataset['product_name'] = np.where(dataset['product_name'].str.contains("2901 Series "), "Digital Alarm Communicating Transmitter", dataset['product_name'])
    dataset['product_name'] = np.where(dataset['product_name'].str.contains("2902 Series "), "Digital Alarm Communicating Transmitter", dataset['product_name'])
    
    dataset['product_name'] = np.where(dataset['product_name'].str.contains("36 Gallon "), "36 Gallon Bladder Tank and Foam Station", dataset['product_name'])
    
    
    dataset['product_name'] = np.where(dataset['product_name'].str.contains("YVAA Evaporator Freeze Damage Potential Due to Refrigerant Migration "), "YVAA", dataset['product_name'])
    dataset['product_name'] = np.where(dataset['product_name'].str.contains("Adj. Diff. Floating Switchover: Selecting Proper Differential"), "Accessories", dataset['product_name'])
    dataset['product_name'] = np.where(dataset['product_name'].str.contains("All Chillers Parts Identification Requirements"), "Chillers", dataset['product_name'])
    dataset['product_name'] = np.where(dataset['product_name'].str.contains("All Single Stage Centrifugal Chillers Condenser Waterbox Procedure"), "Centrifugal Chillers", dataset['product_name'])
    dataset['product_name'] = np.where(dataset['product_name'].str.contains("Application Considerations: Three-Way Valve Equal Percentage Flow Characteristic"), "Three-Way Valve", dataset['product_name'])
    dataset['product_name'] = np.where(dataset['product_name'].str.contains("Application and Data Server (ADS) and Extended Application and Data Server (ADX)"), "ADS, ADX", dataset['product_name'])
    dataset['product_name'] = np.where(dataset['product_name'].str.contains("Approved Discharge Devices For Use With Ansul Foam Concentrates"), "Ansul Foam Concentrates", dataset['product_name'])
    dataset['product_name'] = np.where(dataset['product_name'].str.contains("Centrifugal Chillers Long-Term Storage Requirements - Field Preparation Service Policy and Procedures"), "Centrifugal Chillers", dataset['product_name'])
    dataset['product_name'] = np.where(dataset['product_name'].str.contains("Cross-Reference of VT Series Threaded NPT Valves to VG7000 Series Valves"), "VT Series, VG7000 Series", dataset['product_name'])
    dataset['product_name'] = np.where(dataset['product_name'].str.contains("Cross-Reference of VT Series Union End Valves to VG7000 Series Valves"), "VT Series, VG7000 Series", dataset['product_name'])
    dataset['product_name'] = np.where(dataset['product_name'].str.contains("Cross-reference of V-7x16 Series Valves to VG7000 Series Valves"), "V-8 Series, VG7000 Series", dataset['product_name'])
    dataset['product_name'] = np.where(dataset['product_name'].str.contains("CLK3502 Time Clock"), "CLK3502 Time Clock", dataset['product_name'])
    dataset['product_name'] = np.where(dataset['product_name'].str.contains("Effects of Moisture in Refrigerant Systems"), "Chillers", dataset['product_name'])
    dataset['product_name'] = np.where(dataset['product_name'].str.contains("Effects of Moisture in Refrigerant Systems"), "Chillers", dataset['product_name'])
    dataset['product_name'] = np.where(dataset['product_name'].str.contains("F59 Series Two-Pole Liquid Level Switches Sump or Open Tank Float or Weight"), "F59 Series", dataset['product_name'])
    dataset['product_name'] = np.where(dataset['product_name'].str.contains("FX-PC Series Controllers Enumeration Sets"), "FX Workbench", dataset['product_name'])
    dataset['product_name'] = np.where(dataset['product_name'].str.contains("Facility Explorer Administrator Tool for Validated Environments User’sIntroduction to Facility Explorer Administrator Tool for Validated Environments"), "Facility Explorer Administrator Tool", dataset['product_name'])
    dataset['product_name'] = np.where(dataset['product_name'].str.contains("LonWorks® Network Thermostat"), "LonWorks Network Thermostat Controllers", dataset['product_name'])
    dataset['product_name'] = np.where(dataset['product_name'].str.contains("Facility Explorer Supervisory Products Networking"), "FX20 Supervisory Controller, FX30E Supervisory Controller, FX60 and FX60E Supervisory Controller, FX Server, FX Workbench", dataset['product_name'])
    dataset['product_name'] = np.where(dataset['product_name'].str.contains('HF/HE "P" Series Compressors (HF52 O-Ring Kit) Renewal Parts Literature Supplement - 160.73-RP2 (LS01)(406)'), 'HF/HE P Series Compressors (HF52 O-Ring Kit) Renewal Parts', dataset['product_name'])
    dataset['product_name'] = np.where(dataset['product_name'].str.contains("CD15 to CD28"), "Relia Choice CD15 to CD28", dataset['product_name'])
    dataset['product_name'] = np.where(dataset['product_name'].str.contains("Foam Definitions For Use With Ansul Foam Concentrates"), "Foam Sprinkler Equipment", dataset['product_name'])
    dataset['product_name'] = np.where(dataset['product_name'].str.contains("GRINNELL G-FIRE Gasket Service Recommendations for Fire Grooved Products"), "GRINNELL", dataset['product_name'])
    dataset['product_name'] = np.where(dataset['product_name'].str.contains("J Series Electric Zone Valves — Two-Way Spring Closed Normally Closed"), "J Series Electric Zone Valves", dataset['product_name'])
    dataset['product_name'] = np.where(dataset['product_name'].str.contains("CD15 to CD28"), "Relia Choice CD15 to CD28", dataset['product_name'])
    dataset['product_name'] = np.where(dataset['product_name'].str.contains("Mates Behavior Watch - ExacqVision Integration"), "VMS Software", dataset['product_name'])
    dataset['product_name'] = np.where(dataset['product_name'].str.contains("Model DPV-1 Dry Pipe Valve"), "Model DPV-1 Dry Pipe Valve", dataset['product_name'])
    dataset['product_name'] = np.where(dataset['product_name'].str.contains("OM & YST "), "OM Chillers, YST Chillers", dataset['product_name'])
    dataset['product_name'] = np.where(dataset['product_name'].str.contains("Power Element Style Chart for Charged Temperature Elements and Bellows Pressure Elements"), "Electromechanical Pressure Control, Electromechanical Temperature Control", dataset['product_name'])
    dataset['product_name'] = np.where(dataset['product_name'].str.contains("Prevention of Electrostatic Discharges that Destroys Electronic Printed Circuit Boards Handling"), "Chillers", dataset['product_name'])
    dataset['product_name'] = np.where(dataset['product_name'].str.contains("Release of Flat Spring Washers for YK Centrifugal Liquid Chiller Compressor"), "YK Centrifugal Chillers", dataset['product_name'])
    dataset['product_name'] = np.where(dataset['product_name'].str.contains("Replacing a Local Device Manager"), "Wireless Device Manager BIM, Wireless Module BIX", dataset['product_name'])
    dataset['product_name'] = np.where(dataset['product_name'].str.contains("Screw and Scroll Compressors - System Clean Up Procedure After Compressor Burnout"), "Reciprocating, Screw Air Cooled, Screw Water Cooled, Scroll Air Cooled, Scroll Water Cooled", dataset['product_name'])
    dataset['product_name'] = np.where(dataset['product_name'].str.contains("Use of Oil Filters to Maintain Control System Air Quality"), "Oil Filters", dataset['product_name'])
    dataset['product_name'] = np.where(dataset['product_name'].str.contains("Wiring Diagram - Field Connections Millennium Model YT Chillers (Style J) with Variable Speed Drive "), "YT Chillers", dataset['product_name'])
    dataset['product_name'] = np.where(dataset['product_name'].str.contains("YCAS Series F Compressors Error Regarding Priming Literature Supplement "), "YCAS", dataset['product_name'])
    dataset['product_name'] = np.where(dataset['product_name'].str.contains("YCAS0693; YCAS0773;"), "YCAS", dataset['product_name'])
    dataset['product_name'] = np.where(dataset['product_name'].str.contains("YCAS0693EC-0953EC"), "YCAS", dataset['product_name'])
    
    
    
    dataset['product_name'] = dataset['product_name'].str.replace("Chiller,", "Chiller")
    dataset['product_name'] = dataset['product_name'].str.replace(" Quick Reference", "")
    dataset['product_name'] = dataset['product_name'].str.replace(" Catalog Page", "")
    dataset['product_name'] = dataset['product_name'].str.replace("Ki ", "Kit")
    dataset['product_name'] = dataset['product_name'].str.replace("Sensors", "Sensor")
    dataset['product_name'] = dataset['product_name'].str.replace("Systems", "System")
    dataset['product_name'] = dataset['product_name'].str.replace("Transmitters", "Transmitter")
    dataset['product_name'] = dataset['product_name'].str.replace("Transducers", "Transducer")
    dataset['product_name'] = dataset['product_name'].str.replace("Controllers", "Controller")
    dataset['product_name'] = dataset['product_name'].str.replace("Chillers", "Chiller")
    
    dataset['product_name'] = dataset['product_name'].str.replace(" Renewal Parts", "")
    
    
    
    # DOUBLE SPACES
    dataset['product_name'] = dataset['product_name'].str.replace("  ", " ")
    dataset['product_name'] = dataset['product_name'].str.replace("  ", " ")
    
    
    dataset['product_name'] = dataset['product_name'].str.strip()
    
    
    
    # CHECK
#    missing_brands = dataset[dataset['brand'] == "Not Specified"]
#    missing_product_name = dataset[dataset['product_name'] == "Not Specified"]
   
    
    dataset.to_csv("4_documents_gaps_filled.csv",  encoding='utf-8-sig', index=False)
    
    return dataset

#
#
#
data = fill_brand_and_product_gaps("3_documents_cleaned.csv")
#
#
#
#
## CHECK
dataset = pd.read_csv("4_documents_gaps_filled.csv", encoding='utf-8-sig')
brands = list(data['brand'].unique())


#tryit = dataset[dataset['product_name'].str.contains("Fan Control and Occupancy Sensing Capability")]
#    
#dataset_error = dataset[dataset['product_name'].str.len() > 250]     
#product_unique = list(dataset['product_name'].unique())
#product_unique = ", ".join(product_unique)
#product_unique = product_unique.split(", ")
#product_unique = list(set(product_unique))
#    
#    
#product_error = []
#
#for string in product_unique:
#    if len(string) > 40:
#        product_error.append(string)
#    
#    
    













