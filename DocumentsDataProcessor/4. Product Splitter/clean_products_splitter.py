# -*- coding: utf-8 -*-
"""
Created on Sat Feb 29 12:58:23 2020

@author: LukaszMalucha
"""

def to_replacer(string):
    """Helper function that replace 'to' with ' - ' for prod collections only"""
    if len(string) < 16:
        string = string.replace(" to ", " - ")
        
    return string    
        


import pandas as pd

def clean_products_splitter(filename):
    """Clean and split product names to separate rows"""
    
    dataset = pd.read_csv(filename, encoding='utf-8-sig')
    
    """
    Initial String Cleaning
    """
    dataset['product_name'] = dataset['product_name'].str.replace("M9102-AGA-2S, -3S and M9104-xxA-2S, -3S Series Electric Non-Spring Return Actuators", "M9102-AGA-2S, M9102-AGA-3S, M9104-AGA-2S, M9104-AGA-3S, M9104-IGA-2S, M9104-IGA-3S, M9104-GGA-2S, M9104-GGA-3S, M9104-IUA-2S" )
    dataset['product_name'] = dataset['product_name'].str.replace("VB-3766, VB-3966, VB-4332 Series Brass Flare Valve Bodies, 1/2 in. Two-Way and Three-Way", "VB-3766 Series Brass Flare Valve Bodies - 1/2 in./Two-Way/Three-Way, VB-3966 Series Brass Flare Valve Bodies - 1/2 in./Two-Way/Three-Way, VB-4332 Series Brass Flare Valve Bodies - 1/2 in./Two-Way/Three-Way")
    dataset['product_name'] = dataset['product_name'].str.replace("V-3766, V-3966 and V-4332 Brass Pneumatic Flare Valves, 1/2 in. Two-Way and Three-Way", "V-3766 Series  Brass Pneumatic Flare Valves - 1/2 in. Two-Way and Three-Way, V-3966 Series  Brass Pneumatic Flare Valves - 1/2 in. Two-Way and Three-Way, V-4332 Series  Brass Pneumatic Flare Valves - 1/2 in. Two-Way and Three-Way")
    dataset['product_name'] = dataset['product_name'].str.replace("Repair Parts for Use with V-3755 Normally Open Valves, 1/2 through 2 in.", "Repair Parts for Use with V-3755 Normally Open Valves - 1/2 through 2 in." )  
    dataset['product_name'] = dataset['product_name'].str.replace("EAS / Accent Detacher", "EAS|Accent Detacher" )
    dataset['product_name'] = dataset['product_name'].str.replace("D-4070, Damper Actuator", "D-4070 Damper Actuator" ) # FROM DOC ID CHECK
    dataset['product_name'] = dataset['product_name'].str.replace("—", "-" )
    
    
    """
    FIRST SPLIT BY COMMA
    """
    
    dataset['product_name'] = dataset['product_name'].apply(lambda x: x.split(',')) 
    product_name_column = dataset.apply(lambda x: pd.Series(x['product_name']), axis=1).stack().reset_index(level=1, drop=True)
    product_name_column.name = 'product_name'
    dataset = dataset.drop('product_name', axis=1).join(product_name_column)
    dataset['product_name'] = pd.Series(dataset['product_name'], dtype=object)
    
    # REMOVE (OTHER CHOICES AVAILABLE)
    dataset['product_name'] = dataset['product_name'].str.replace("other choices available", "")
    dataset['product_name'] = dataset['product_name'].str.replace("(", "")
    dataset['product_name'] = dataset['product_name'].str.replace(")", "")
    
    # REMOVE WHITESPACES
    dataset['product_name'] = dataset['product_name'].str.strip()    
    
    
    # Swtich double spaces to single spaces
    dataset['product_name'] = dataset['product_name'].str.replace("  ", " " )
    
    """
    GET RID OF UNNECESSARY 'AND' REPLACE SLASH
    
    """
    dataset['product_name'] = dataset['product_name'].str.replace("2 Tone and 3 Tone Alarming SuperTags", "2 Tone Alarming SuperTags, 3 Tone Alarming SuperTags" )
    dataset['product_name'] = dataset['product_name'].str.replace("2-Wire and 4-Wire Heat Detector", "2-Wire Heat Detector, 4-Wire Heat Detector" )
    dataset['product_name'] = dataset['product_name'].str.replace("A419 Temperature Control with NEMA 1 Enclosure and A99 Temperature Sensor", "A419 Temperature Control with NEMA 1 Enclosure, A99 Temperature Sensor" )
    dataset['product_name'] = dataset['product_name'].str.replace("AMS-1180 and AMS-1175", "AMS-1180, AMS-1175" )
    dataset['product_name'] = dataset['product_name'].str.replace("CBC-4050 and SmartEAS Local Device Manager", "CBC-4050, SmartEAS Local Device Manager" )
    dataset['product_name'] = dataset['product_name'].str.replace("EC and ED Oil‐Filled", "EC Oil‐Filled, ED Oil‐Filled")
    dataset['product_name'] = dataset['product_name'].str.replace("FLR-30-FP and FLR-90-FP Rim Seal Foam Pourer", "FLR-30-FP Rim Seal Foam Pourer, FLR-90-FP Rim Seal Foam Pourer")
    dataset['product_name'] = dataset['product_name'].str.replace("IDX-2000 and IDX-8000 RFID Reader", "IDX-2000 RFID Reader, IDX-8000 RFID Reader")
    dataset['product_name'] = dataset['product_name'].str.replace("IDX-4000 and IDX-8000 Reader", "IDX-4000 RFID Reader, IDX-8000 RFID Reader")
    dataset['product_name'] = dataset['product_name'].str.replace("JET-X-PFG-7 and JET-X-PFG-M Portable High Expansion Foam Generators", "JET-X-PFG-7 Portable High Expansion Foam Generators, JET-X-PFG-M Portable High Expansion Foam Generators")
    dataset['product_name'] = dataset['product_name'].str.replace("MET-L-X and LITH-X Dry Powder Suppressing Agents", "MET-L-X Dry Powder Suppressing Agents, LITH-X Dry Powder Suppressing Agents")
    dataset['product_name'] = dataset['product_name'].str.replace("Model S-150-C and Model S-350-C Stationary Fire Extinguishers", "Model S-150-C Stationary Fire Extinguishers, Model S-350-C Stationary Fire Extinguishers")
    dataset['product_name'] = dataset['product_name'].str.replace("Model SL and Model A-PC Fusible Links", "Model SL Fusible Links, Model A-PC Fusible Links")
    dataset['product_name'] = dataset['product_name'].str.replace("Model SW-20 and SW-24", "Model SW-20, Model SW-24")
    dataset['product_name'] = dataset['product_name'].str.replace("P20 and P21 Pressure Control", "P20 Pressure Control,P21 Pressure Control")
    dataset['product_name'] = dataset['product_name'].str.replace("P45 and P145 Lube Oil Pressure Control", "P45 Lube Oil Pressure Control, P145 Lube Oil Pressure Control")
    dataset['product_name'] = dataset['product_name'].str.replace("P72 and P170 Dual‐Pressure Control", "P72 Dual‐Pressure Control, P170 Dual‐Pressure Control")
    dataset['product_name'] = dataset['product_name'].str.replace("P72 and P170 High‐Pressure Control", "P72 High‐Pressure Control, P170 High‐Pressure Control")
    dataset['product_name'] = dataset['product_name'].str.replace("P72 and P170 Low‐Pressure Control", "P72 Low‐Pressure Control, P170 Low‐Pressure Control")
    dataset['product_name'] = dataset['product_name'].str.replace("QREV and PSHC Electronic Expansion Valve and Superheat Controller", "QREV Electronic Expansion Valve and Superheat Controller, PSHC Electronic Expansion Valve and Superheat Controller")
    dataset['product_name'] = dataset['product_name'].str.replace("YB25 and YB28", "YB25, YB28")
    dataset['product_name'] = dataset['product_name'].str.replace("YB25 and YB28", "YB25, YB28")
    dataset['product_name'] = dataset['product_name'].str.replace("Z-Series IPS 2U and Hybrid 2U", "Z-Series IPS 2U, Z-Series Hybrid 2U")
    dataset['product_name'] = dataset['product_name'].str.replace("V48 and V248 Valves Repair Kit", "V48 Valves Repair Kit, V248 Valves Repair Kit")
    dataset['product_name'] = dataset['product_name'].str.replace("830 Series 850 Series", "830 Series, 850 Series")
    dataset['product_name'] = dataset['product_name'].str.replace("KT-300 KT-400", "KT-300, KT-400")
    dataset['product_name'] = dataset['product_name'].str.replace("IDA-1000 IDA-2400 RFID Antennas", "IDA-1000 RFID Antenna, IDA-2400 RFID Antenna")
    dataset['product_name'] = dataset['product_name'].str.replace("AMS-1090/1091 Bumper Kit", "AMS-1090 Bumper Kit, AMS-1091 Bumper Kit")
    dataset['product_name'] = dataset['product_name'].str.replace("AMS-1090/1091 Bumper Kit", "AMS-1090 Bumper Kit, AMS-1091 Bumper Kit")
    dataset['product_name'] = dataset['product_name'].str.replace("AMS-1090/AMS-1130 Custom Panel Kit", "AMS-1090 Bumper Kit, AMS-1091 Bumper Kit")
    dataset['product_name'] = dataset['product_name'].str.replace("AMS-1140 / AMS-1150 Detection Systems", "AMS-1140 Detection Systems, AMS-1150 Detection Systems")
    dataset['product_name'] = dataset['product_name'].str.replace("AMS-1180 / 1175 Alarm Configuration", "AMS-1180 Alarm Configuration, AMS-1180 Alarm Configuration")
    dataset['product_name'] = dataset['product_name'].str.replace("AMS-1180 / AMS-1175 Pedestal", "AMS-1180 Pedestal, AMS-1175 Pedestal")
    dataset['product_name'] = dataset['product_name'].str.replace("AMS-1190/1180/1175 Stainless Steel Base Cover Kit", "AMS-1190 Stainless Steel Base Cover Kit, AMS-1180 Stainless Steel Base Cover Kit, AMS-1175 Stainless Steel Base Cover Kit")
    dataset['product_name'] = dataset['product_name'].str.replace("AMS-3000/3003 Metal-Clad Cable", "AMS-3000 Metal-Clad Cable, AMS-3003 Metal-Clad Cable")
    dataset['product_name'] = dataset['product_name'].str.replace("AMS-3000/3003 Metal-Clad Cable Capacitor Box Kit", "AMS-3000 Metal-Clad Cable Capacitor Box Kit, AMS-3003 Metal-Clad Cable Capacitor Box Kit")
    dataset['product_name'] = dataset['product_name'].str.replace("AMS-3003/3010/3030 Loop Antenna Surface Mount Kit", "AMS-3000 Metal-Clad Loop Antenna Surface Mount Kit, AMS-3010 Loop Antenna Surface Mount Kit, AMS-3030 Loop Antenna Surface Mount Kit")
    dataset['product_name'] = dataset['product_name'].str.replace("AMS-3004/3005 Loop 2Ma EAS System", "AMS-3004 Loop 2Ma EAS System, AMS-3005 Loop 2Ma EAS System")
    dataset['product_name'] = dataset['product_name'].str.replace("AMS-3004/3040 Loop System", "AMS-3004 Loop System, AMS-3040 Loop System")
    dataset['product_name'] = dataset['product_name'].str.replace("AMS-9030/9033 Controller", "AMS-9030 Controller, AMS-9033 Controller")
    dataset['product_name'] = dataset['product_name'].str.replace("AMS-9050/AMS-9040/AMS-1080 Controllers", "AMS-9050 Controllers, AMS-9040 Controllers, AMS-1080 Controllers")
    dataset['product_name'] = dataset['product_name'].str.replace("APS-100/APS-1000 Exit Anti-Theft System", "APS-100 Exit Anti-Theft System, APS-1000 Exit Anti-Theft System")
    dataset['product_name'] = dataset['product_name'].str.replace("CBC-4020/4030 Series UltraLink", "CBC-4020 Series UltraLink, CBC-4030 Series UltraLink")
    dataset['product_name'] = dataset['product_name'].str.replace("CBC-4020/4030 Series UltraLink Smart Device Manager", "CBC-4020 Series UltraLink Smart Device Manager, CBC-4020 Series UltraLink Smart Device Manager")
    dataset['product_name'] = dataset['product_name'].str.replace("CBC-4020/4030 Series UltraLink Smart Device Manager 1.5", "CBC-4020 Series UltraLink Smart Device Manager 1.5, CBC-4030 Series UltraLink Smart Device Manager 1.5")
    dataset['product_name'] = dataset['product_name'].str.replace("CBC-4020/4030 UltraLink Outdoor Enclosure", "CBC-4020 UltraLink Outdoor Enclosure, CBC-4030 UltraLink Outdoor Enclosure")
    dataset['product_name'] = dataset['product_name'].str.replace("CBC-4020/4030/405X Series Smart Device Manager 2.4", "CBC-4020 Series Smart Device Manager 2.4, CBC-4030 Series Smart Device Manager 2.4, CBC-405X Series Smart Device Manager 2.4")
    dataset['product_name'] = dataset['product_name'].str.replace("IDC-1000/IDC-1020 RF Reader", "IDC-1000 RF Reader,IDC-1020 RF Reader")
    dataset['product_name'] = dataset['product_name'].str.replace("IDKM-1000/IDKM-1010 SuperTag Detacher", "IDKM-1000 SuperTag Detacher, IDKM-1010 SuperTag Detacher")
    dataset['product_name'] = dataset['product_name'].str.replace("IDKM-1000/IDKM-1010 SuperTag Detacher RF Choke Kit", "IDKM-1000 SuperTag Detacher RF Choke Kit, IDKM-1010 SuperTag Detacher RF Choke Kit")
    dataset['product_name'] = dataset['product_name'].str.replace("IDKM-10XX/AMK-10XX SuperTag Detacher WDM BIX1000 Cable Kit", "IDKM-10XX SuperTag Detacher WDM BIX1000 Cable Kit, AMK-10XX SuperTag Detacher WDM BIX1000 Cable Kit")
    dataset['product_name'] = dataset['product_name'].str.replace("EC76/MC76 Digital Alarm", "EC76 Digital Alarm, MC76 Digital Alarm")
    dataset['product_name'] = dataset['product_name'].str.replace("MK190/MK200 Retrofit Bezel", "MK190 Retrofit Bezel, MK200 Retrofit Bezel")
    dataset['product_name'] = dataset['product_name'].str.replace("MK90/MK91 Retrofit Bezel", "MK90 Retrofit Bezel, MK91 Retrofit Bezel")
    dataset['product_name'] = dataset['product_name'].str.replace("MKD400 Ultra Tag/Ultra Lite Basic Detacher", "MKD400 Ultra Tag Basic Detacher, MKD400 Ultra Lite Basic Detacher")
    dataset['product_name'] = dataset['product_name'].str.replace("Model BFV-300/BFV-300C", "Model BFV-300, Model BFV-300C")
    dataset['product_name'] = dataset['product_name'].str.replace("Model GUMC/GUWSU", "Model GUMC, Model GUWSU")
    dataset['product_name'] = dataset['product_name'].str.replace("P28 and P128 Lube Oil Pressure Control", "P28 Lube Oil Pressure Control, P128 Lube Oil Pressure Control")
    dataset['product_name'] = dataset['product_name'].str.replace("UltraMax M2K/M4K Power Pack", "UltraMax M2K  Power Pack, UltraMax M4K Power Pack")
    dataset['product_name'] = dataset['product_name'].str.replace("UltraMax M2K/M4K/M4K Power Pack", "UltraMax M2K Power Pack, UltraMax M4K Power Pack")
    dataset['product_name'] = dataset['product_name'].str.replace("UltraMax MK90/190 Flush Mount Detacher Retrofit", "UltraMax MK90 Flush Mount Detacher Retrofit, UltraMax MK190 Flush Mount Detacher Retrofit")
    dataset['product_name'] = dataset['product_name'].str.replace("UltraMax Stand-Alone/EuroMax M2K EAS System", "UltraMax Stand-Alone M2K EAS System, UltraMax EuroMax M2K EAS System")
    
    
    
    dataset['product_name'] = dataset['product_name'].str.replace("|", "/")   
    
    """
    SECOND SPLIT AFTER CLEANING 
    """
    dataset['product_name'] = dataset['product_name'].apply(lambda x: x.split(',')) 
    product_name_column = dataset.apply(lambda x: pd.Series(x['product_name']), axis=1).stack().reset_index(level=1, drop=True)
    product_name_column.name = 'product_name'
    dataset = dataset.drop('product_name', axis=1).join(product_name_column)
    dataset['product_name'] = pd.Series(dataset['product_name'], dtype=object)
    
    # Final cleaning
    dataset['product_name'] = dataset['product_name'].str.replace("J06-12ZB", "J06 - J12ZB")
    dataset['product_name'] = dataset['product_name'].str.replace("ZN-06 THRU -12", "ZN-06 - ZN-12")
    dataset['product_name'] = dataset['product_name'].str.replace("ZNT06-T12", "ZNT06 - ZNT12")
    dataset['product_name'] = dataset['product_name'].str.replace("ZQ04-06", "ZQ04 - ZQ06")
    
    """
    REPLACE 'TO' with ' - ' in product name collections
    """
    dataset['product_name'] = dataset['product_name'].apply(lambda x: to_replacer(x)) 
    
    # REMOVE WHITESPACES
    dataset['product_name'] = dataset['product_name'].str.strip()    
    
    
    dataset.to_csv("documents_splitted_products.csv",  encoding='utf-8-sig', index=False)
    
    return dataset
    
    
data = clean_products_splitter("documents_cleaned.csv")    


# ERRATIC CHECK
#dataset = pd.read_csv("documents_cleaned.csv", encoding='utf-8-sig')
#erratic = dataset[dataset['product_code'].str.contains('\|')]
    
    
    
    
    
    
    