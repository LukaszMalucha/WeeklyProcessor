# -*- coding: utf-8 -*-
"""
Created on Fri Mar  6 13:46:33 2020

@author: jmalucl
"""

import pandas as pd
import numpy as np
import re
import hashlib

string2 = "EntraPass Corporate Edition Administration Guide" 

def first_letters(string):
    """First and last letter of a word to create some unique id"""
    string = string.replace("exacqVision-Entrapass", "eV-EP")  
    string = string.replace("exacqVision", "eV")
    string = string.replace("LN Series LN-VSTAT and LN-PSTAT Sensors ", "LN-VP")
    string = string.replace("LN Series VAV and VVT Controllers ", "VAVVVT")
    string = string.replace("LX Series Free Programmable Controllers  ", "LX")
    string = string.replace("LX Series Free Programmable LX-PRG203-11 Controller ", "LX-PRG")
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


def unique_elements(string):
    """Get unique elements after merging strings"""
    new_list = string.split(', ')
    new_list = list(set(new_list))
    new_list = ', '.join(sorted(new_list))
    new_list = new_list.replace(", Not Specified", "")
    new_list = new_list.replace("Not Specified, ", "")      
    return new_list




def unique_document_id(filename):
        
    
    dataset = pd.read_csv(filename, encoding='utf-8-sig')
    dataset = dataset.replace(np.nan, 'Not Specified', regex=True)
    
    # Remove erratic documents
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
    dataset = dataset[~dataset['document_title'].str.contains('05791229AC_B')]
    dataset = dataset[~dataset['document_title'].str.contains('05791328')]
    dataset = dataset[dataset['document_title'].str[:] != "Rev. 01"]
    
    
    """
    REMOVE "Part No." from product name columns
    """
    
    dataset['document_number'] = dataset['document_number'].str.replace("Part No. ", "")
    dataset['document_part_number'] = dataset['document_part_number'].str.replace("Part No. ", "")
    
      
    
    """
    THERE ARE FORM DOCUMENTS THAT HAVE NO METADATA BUT FORM ID IN PARETHESES
    THAT ID SHOULD BE DOCUMENT NUMBER
    """
    
    
    dataset['form_number'] = dataset['document_title'].apply(lambda x: get_form_id(x))
    
    dataset['document_number'] = np.where(dataset['document_number'] == "Not Specified", dataset['form_number'], dataset['document_number'])
    
    
    dataset = dataset.drop(['form_number'], axis=1)
    
    
#    
#    check = dataset[dataset['document_title'] == "PROFILE Panels Installation Guide"]
#    check = dataset[dataset['document_title'].str.contains("\(Form")]
#    
    
    """
    Metadata fix
    """ 
    
    
    # OTHER LANGS
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
    dataset = dataset.drop(dataset[(dataset['document_link'] == '/viewer/document/wtAd7YdWzEXTqdmxNHmTpA')].index)
    dataset = dataset.drop(dataset[(dataset['document_link'] == '/viewer/document/EN5XtgsB8gJEefGO2_9XrQ')].index)
    dataset = dataset.drop(dataset[(dataset['document_link'] == '/viewer/document/NLJ0Iblxy7ZekBWAGZWXOA')].index)
    dataset = dataset.drop(dataset[(dataset['document_link'] == '/viewer/document/NSfaGFKcRrVp1BB~rES8pA')].index)
    dataset = dataset.drop(dataset[(dataset['document_link'] == '/viewer/document/FHYyerK4LXW469aVS_o~HA')].index)
    dataset = dataset.drop(dataset[(dataset['document_link'] == '/viewer/document/_nbKQ5V8wS8CaqcEVBmfPg')].index)
    dataset = dataset.drop(dataset[(dataset['document_link'] == '/viewer/document/WSu_mTXPId68Gkit~lstMA')].index)
    dataset = dataset.drop(dataset[(dataset['document_link'] == '/viewer/document/dizazK2x5YGWyk0jj3E6Vw')].index)
    dataset = dataset.drop(dataset[(dataset['document_link'] == '/viewer/document/1mm5vv7wKDFca~mR_bnm2w')].index)
    dataset = dataset.drop(dataset[(dataset['document_link'] == '/viewer/document/1UuW4QF33~NYBFaMvu0vZQ')].index)
    dataset = dataset.drop(dataset[(dataset['document_link'] == '/viewer/document/Q20IoBi3vtb90EZlJMAYCA')].index)
    dataset = dataset.drop(dataset[(dataset['document_link'] == '/viewer/document/BBO4Jl34FyfmQI7JKSRTuQ')].index)
    dataset = dataset.drop(dataset[(dataset['document_link'] == '/viewer/document/HVpOIsn0ZHuwS~KAqInGWA')].index)
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
    dataset = dataset.drop(dataset[(dataset['document_link'] == '/viewer/document/ks4ksOG~xCIF5PDKURUrGQ')].index)
    dataset = dataset.drop(dataset[(dataset['document_link'] == '/viewer/document/_o0GHGxjYje7b9YIr6SzXA')].index)
    
    
    
    ## NO METADATA DUPLCIATES VARIOUS
    dataset = dataset.drop(dataset[(dataset['document_link'] == '/viewer/document/XUcNsFHov97a7xxWfm8ONw')].index)
    dataset = dataset.drop(dataset[(dataset['document_link'] == '/viewer/document/uTqBts88gBilZfRVXtkdsQ')].index)
    dataset = dataset.drop(dataset[(dataset['document_link'] == '/viewer/document/~MpE5qAPT96kyCwqRvGgJg')].index)
    dataset = dataset.drop(dataset[(dataset['document_link'] == '/viewer/document/upNXDJvuyEpMo7IJIC15pg')].index)
    dataset = dataset.drop(dataset[(dataset['document_link'] == '/viewer/document/2j_V~t2YFtOtksJODS2m9w')].index)
    dataset = dataset.drop(dataset[(dataset['document_link'] == '/viewer/document/5xTbkIPXn348Je7Natw4lw')].index)
    dataset = dataset.drop(dataset[(dataset['document_link'] == '/viewer/document/5xTbkIPXn348Je7Natw4lw')].index)
    dataset = dataset.drop(dataset[(dataset['document_link'] == '/viewer/document/gsMGbYdVvyPwxAzW70ndXw')].index)
    dataset = dataset.drop(dataset[(dataset['document_link'] == '/viewer/document/TjwtgyUKdsQz9w3oRuAzFA')].index)
    dataset = dataset.drop(dataset[(dataset['document_link'] == '/viewer/document/dl23NQiGQyJton9PDNiHdw')].index)
    dataset = dataset.drop(dataset[(dataset['document_link'] == '/viewer/document/xPs9B4pV6Q1QcpA9VWPFMg')].index)
    dataset = dataset.drop(dataset[(dataset['document_link'] == '/viewer/document/xDheXvfJOOmX2HJqdjhFDQ')].index)
    dataset = dataset.drop(dataset[(dataset['document_link'] == '/viewer/document/hcDfVivI8uPNjoN29OqVTA')].index)
    dataset = dataset.drop(dataset[(dataset['document_link'] == '/viewer/document/By61TcqLrytEshbAm2djBw')].index)
    dataset = dataset.drop(dataset[(dataset['document_link'] == '/viewer/document/_jRsNPSRmB0RtIR3iOhZsw')].index)
    dataset = dataset.drop(dataset[(dataset['document_link'] == '/viewer/document/7bJ0rVyeutSllyTB2DdSdA')].index)
    dataset = dataset.drop(dataset[(dataset['document_link'] == '/viewer/document/LyJx0ZzWIxl8dT4Kf8hajg')].index)
    
    # Erratic duplicate dates
    dataset = dataset.drop(dataset[(dataset['document_link'] == '/viewer/document/6tN_ICW699afn66_yv42fA')  & (dataset['document_created_at'] == "2016-12-01")].index)
    dataset = dataset.drop(dataset[(dataset['document_link'] == '/viewer/document/a64m82Bgs0QaLLOI_wmNng')  & (dataset['document_created_at'] == "2016-12-01")].index)
    dataset = dataset.drop(dataset[(dataset['document_link'] == '/viewer/document/PIGe3jav7ZDIZJecfZS20g')  & (dataset['document_created_at'] == "2016-12-01")].index)
    dataset = dataset.drop(dataset[(dataset['document_link'] == '/viewer/document/LvZmp8qoI5tj02uBP30lPQ')  & (dataset['document_created_at'] == "2017-03-01")].index)
    dataset = dataset.drop(dataset[(dataset['document_link'] == '/viewer/document/o21Iwk~HmZSPaJSHyzDb2g')  & (dataset['document_created_at'] == "2017-03-01")].index)
    dataset = dataset.drop(dataset[(dataset['document_link'] == '/viewer/document/vhdOwZlLoE9bQg8T_LyWcg')  & (dataset['document_created_at'] == "2017-03-01")].index)
    dataset = dataset.drop(dataset[(dataset['document_link'] == '/viewer/document/gVnOZD2k514cbOVITkD_pg')  & (dataset['document_created_at'] == "2019-03-01")].index)
    dataset = dataset.drop(dataset[(dataset['document_link'] == '/viewer/document/pxPQPNMck1qQagMP4GfLRw')  & (dataset['document_created_at'] == "2017-10-01")].index)
    dataset = dataset.drop(dataset[(dataset['document_link'] == '/viewer/document/UwJE93hrmmiJ2g_udl9g1Q')  & (dataset['document_created_at'] == "2017-10-01")].index)
    dataset = dataset.drop(dataset[(dataset['document_link'] == '/viewer/document/rVSYtBSAdmNpVCr0P0_aKA')  & (dataset['document_created_at'] == "2017-10-01")].index)
    dataset = dataset.drop(dataset[(dataset['document_link'] == '/viewer/document/hyuHiSdGKOxMkASMYzdz7w')  & (dataset['document_created_at'] == "2017-10-01")].index)
    dataset = dataset.drop(dataset[(dataset['document_link'] == '/viewer/document/flEgXHsWsrsiPLtjdILRrg')  & (dataset['document_created_at'] == "2017-10-01")].index)
    dataset = dataset.drop(dataset[(dataset['document_link'] == '/viewer/document/6tN_ICW699afn66_yv42fA')  & (dataset['document_created_at'] == "2017-10-01")].index)
    dataset = dataset.drop(dataset[(dataset['document_link'] == '/viewer/document/fUb5nW~LKUdJgbjp_LQ6Tg')  & (dataset['document_created_at'] == "2017-03-01")].index)
    dataset = dataset.drop(dataset[(dataset['document_link'] == '/viewer/document/_PJPPtIfN4JOYLZmp3GCnA')  & (dataset['document_created_at'] == "2017-03-01")].index)
    dataset = dataset.drop(dataset[(dataset['document_link'] == '/viewer/document/lC8Nnzevg04yDafKL1uQag')  & (dataset['document_created_at'] == "2017-10-01")].index)
    dataset = dataset.drop(dataset[(dataset['document_link'] == '/viewer/document/YHMJtXSivajbg0oYwDtfqw')  & (dataset['document_created_at'] == "2017-10-01")].index)
    dataset = dataset.drop(dataset[(dataset['document_link'] == '/viewer/document/m8gzl4IgrycPGN6sqnBLEg')  & (dataset['document_created_at'] == "2018-05-01")].index)
    dataset = dataset.drop(dataset[(dataset['document_link'] == '/viewer/document/Nr7gA_ARIPRm~dbP4v1qdw')  & (dataset['document_created_at'] == "2018-05-01")].index)
    dataset = dataset.drop(dataset[(dataset['document_link'] == '/viewer/document/V48d2ZFX56AJ4qpQmMFQ0w')  & (dataset['document_created_at'] == "2018-05-01")].index)
    dataset = dataset.drop(dataset[(dataset['document_link'] == '/viewer/document/jzJJH0_jWn4A_YrLXtQJVQ')  & (dataset['document_created_at'] == "2017-03-01")].index)
    dataset = dataset.drop(dataset[(dataset['document_link'] == '/viewer/document/~Qxdm78K_kFemtdefDyskA')  & (dataset['document_created_at'] == "2019-07-01")].index)
    dataset = dataset.drop(dataset[(dataset['document_link'] == '/viewer/document/Vf08F179r9JoyZ9TDczCIA')  & (dataset['document_created_at'] == "2018-12-01")].index)
    dataset = dataset.drop(dataset[(dataset['document_link'] == '/viewer/document/lC8Nnzevg04yDafKL1uQag')  & (dataset['document_created_at'] == "2019-03-01")].index)
    dataset = dataset.drop(dataset[(dataset['document_link'] == '/viewer/document/m8gzl4IgrycPGN6sqnBLEg')  & (dataset['document_created_at'] == "2018-07-01")].index)
    dataset = dataset.drop(dataset[(dataset['document_link'] == '/viewer/document/a_1Jrz5n1nsyIG4vGdhKgQ')  & (dataset['document_created_at'] == "2020-01-09")].index)
    dataset = dataset.drop(dataset[(dataset['document_title'] == 'exacq and KiwiVision Integration') & (dataset['document_created_at'] == "2016-09-30")].index)
    dataset = dataset.drop(dataset[(dataset['document_link'] == '/viewer/document/V48d2ZFX56AJ4qpQmMFQ0w')  & (dataset['document_created_at'] == "2017-05-01")].index)
    dataset = dataset.drop(dataset[(dataset['document_link'] == '/viewer/document/flEgXHsWsrsiPLtjdILRrg')  & (dataset['document_created_at'] == "2018-07-01")].index)
    dataset = dataset.drop(dataset[(dataset['document_link'] == '/viewer/document/6tN_ICW699afn66_yv42fA')  & (dataset['document_created_at'] == "2015-12-01")].index)
    dataset = dataset.drop(dataset[(dataset['document_link'] == '/viewer/document/Nr7gA_ARIPRm~dbP4v1qdw')  & (dataset['document_created_at'] == "2017-05-01")].index)
    dataset = dataset.drop(dataset[(dataset['document_link'] == '/viewer/document/o21Iwk~HmZSPaJSHyzDb2g')  & (dataset['document_created_at'] == "2016-03-01")].index)
    dataset = dataset.drop(dataset[(dataset['document_link'] == '/viewer/document/42Xe9gZeRbcAkYgIIe0NIQ')  & (dataset['document_created_at'] == "2018-05-01")].index)
    
    
    
    # 4100 OPERATING INSTRUCTIONS
    dataset['document_number'] = np.where(dataset['document_link'] == "/viewer/document/cJuUdasllIGtgJOLmXn~Gw", "579-995AC", dataset['document_number'])
    dataset['document_revision'] = np.where(dataset['document_link'] == "/viewer/document/cJuUdasllIGtgJOLmXn~Gw", "A", dataset['document_revision'])
    
    dataset['document_number'] = np.where(dataset['document_link'] == "/viewer/document/X3LImsh8GGALyOIxs_~j2w", "579-684AC", dataset['document_number'])
    dataset['document_revision'] = np.where(dataset['document_link'] == "/viewer/document/X3LImsh8GGALyOIxs_~j2w", "B", dataset['document_revision'])
    
    
    # Duplicate ROOT of related links
    dataset = dataset.drop(dataset[(dataset['document_link'] == '/reader/iNhXVoRZ8gU~FccRXbZiSg/root')].index)
    dataset = dataset.drop(dataset[(dataset['document_link'] == '/reader/rKaUaPzNsfYl8765Nx7vEw/root')].index)
    
    
    
    
    # A4906 Series TrueAlert Addressable Multi-Candela Alert Strobe
    dataset['document_number'] = np.where(dataset['document_link'] == "/viewer/document/Zkmqgvq8p_JViZwGGW_xew", "579-828AC", dataset['document_number'])
    dataset['document_revision'] = np.where(dataset['document_link'] == "/viewer/document/Zkmqgvq8p_JViZwGGW_xew", "F", dataset['document_revision'])
    
    dataset['document_number'] = np.where(dataset['document_link'] == "/viewer/document/Q5AGlnGuLZWH1vBqUDEIsA", "579-847AC", dataset['document_number'])
    dataset['document_revision'] = np.where(dataset['document_link'] == "/viewer/document/Q5AGlnGuLZWH1vBqUDEIsA", "D", dataset['document_revision'])
    
    dataset['document_number'] = np.where(dataset['document_link'] == "/viewer/document/jnfuKop56jBfpPAiMjDVmg", "579-848AC", dataset['document_number'])
    dataset['document_revision'] = np.where(dataset['document_link'] == "/viewer/document/jnfuKop56jBfpPAiMjDVmg", "C", dataset['document_revision'])
    
    dataset['document_number'] = np.where(dataset['document_link'] == "/viewer/document/dYj~IYUNNTCdZJNFwhc7cA", "579-808AC", dataset['document_number'])
    dataset['document_revision'] = np.where(dataset['document_link'] == "/viewer/document/dYj~IYUNNTCdZJNFwhc7cA", "G", dataset['document_revision'])
    
    
    
    
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
    
    
    # CE Declaration of Conformity
    dataset['document_title'] = np.where(dataset['document_link'] == "/viewer/document/s2IGEmEL9vCGp9fP3lvWBA", "CE Declaration of Conformity F2A Series", dataset['document_title'])
    dataset['document_title'] = np.where(dataset['document_link'] == "/viewer/document/bwUUDHUbXA_~0lkiQx3p7g", "CE Declaration of Conformity R2A Series", dataset['document_title'])
    dataset['document_title'] = np.where(dataset['document_link'] == "/viewer/document/GoyDRD5OlVlRDiXBZWJoRA", "CE Declaration of Conformity C-Series 32 Stream", dataset['document_title'])
    dataset['document_title'] = np.where(dataset['document_link'] == "/viewer/document/bwUUDHUbXA_~0lkiQx3p7g", "CE Declaration of Conformity C-Series 16 Stream", dataset['document_title'])
    dataset['document_title'] = np.where(dataset['document_link'] == "/viewer/document/2ALlbYsit1fwbNS~rI2KkA", "CE Declaration of Conformity C-Series 16 Stream", dataset['document_title'])

    dataset['topic_title'] = np.where(dataset['document_link'] == "/viewer/document/s2IGEmEL9vCGp9fP3lvWBA", "CE Declaration of Conformity F2A Series", dataset['topic_title'])
    dataset['topic_title'] = np.where(dataset['document_link'] == "/viewer/document/bwUUDHUbXA_~0lkiQx3p7g", "CE Declaration of Conformity R2A Series", dataset['topic_title'])
    dataset['topic_title'] = np.where(dataset['document_link'] == "/viewer/document/GoyDRD5OlVlRDiXBZWJoRA", "CE Declaration of Conformity C-Series 32 Stream", dataset['topic_title'])
    dataset['topic_title'] = np.where(dataset['document_link'] == "/viewer/document/bwUUDHUbXA_~0lkiQx3p7g", "CE Declaration of Conformity C-Series 16 Stream", dataset['topic_title'])
    dataset['topic_title'] = np.where(dataset['document_link'] == "/viewer/document/2ALlbYsit1fwbNS~rI2KkA", "CE Declaration of Conformity C-Series 16 Stream", dataset['topic_title'])   
    
    
    # Commercial Comfort System (CCS) Variable Air Volume (VAV) Zone - Pressure Independent Controller Installation Instructions
    dataset['document_number'] = np.where(dataset['document_link'] == "/viewer/document/I52yrJGUVoC0oJyITn8ITg", "LIT-12011998-utb-c-0119", dataset['document_number'])
    dataset['document_number'] = np.where(dataset['document_link'] == "/viewer/document/TnXGRHL9B774U1M0cX~upQ", "5127912-usd-a-0515", dataset['document_number'])
    dataset['document_number'] = np.where(dataset['document_link'] == "/viewer/document/t5za~Zl2OkU_DWzFJEyXOA", "5127914-utg-b-1116", dataset['document_number'])
    dataset['document_number'] = np.where(dataset['document_link'] == "/viewer/document/x9Al8Hf_kT8egdIENAw_VQ", "1154578-utg-a-0515", dataset['document_number'])
    dataset['document_number'] = np.where(dataset['document_link'] == "/viewer/document/13k0muux3Egoovg94MrhGw", "5127910-usd-a-0515", dataset['document_number'])
    dataset['document_number'] = np.where(dataset['document_link'] == "/viewer/document/D4CjC6pfMWgXnB9P6nV0Cw", "1154576-uim-b-0615.pdf", dataset['document_number'])
    dataset['document_number'] = np.where(dataset['document_link'] == "/viewer/document/hFNjk1kdFwYBASnWORrPoQ", "LIT-12011998-utb-b-0418", dataset['document_number'])
    dataset['document_number'] = np.where(dataset['document_link'] == "/viewer/document/8hYs9r5eZh3D3my9b2l1QA", "5127911-usd-a-0515", dataset['document_number'])
    
    
    # Controller Tool Help
    dataset['document_number'] = np.where(dataset['document_link'] == "/viewer/document/3vU~yz9aMbRGka0dz6UgRw", "LIT-12011147", dataset['document_number'])
    dataset['document_revision'] = np.where(dataset['document_link'] == "/viewer/document/3vU~yz9aMbRGka0dz6UgRw", "13.0", dataset['document_revision'])
    
    dataset['document_number'] = np.where(dataset['document_link'] == "/viewer/document/lGAyVRovyBLjhD9ZOCeYQQ", "LIT-12011147", dataset['document_number'])
    dataset['document_revision'] = np.where(dataset['document_link'] == "/viewer/document/lGAyVRovyBLjhD9ZOCeYQQ", "10.2", dataset['document_revision'])
    
    
    
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
    
    
    
    # Johnson Controls® Enterprise Management duplicate with one missing topic
    dataset = dataset.drop(dataset[(dataset['document_link'] == '/reader/HolF8uBCOukfQ5PchZupIA/root')].index)
    
    
    # LCS85 Commissioning Guide and others
    dataset['document_number'] = np.where(dataset['document_link'] == "/viewer/document/I58466v90O48PHbuFhjfFw", "LIT-12011568", dataset['document_number'])
    dataset['document_revision'] = np.where(dataset['document_link'] == "/viewer/document/I58466v90O48PHbuFhjfFw", "9.0", dataset['document_revision'])
    
    dataset['document_number'] = np.where(dataset['document_link'] == "/viewer/document/dWRk1RH6QyT76TskOrtnPw", "LIT-12011568", dataset['document_number'])
    dataset['document_revision'] = np.where(dataset['document_link'] == "/viewer/document/dWRk1RH6QyT76TskOrtnPw", "10.0", dataset['document_revision'])
    
    dataset['document_number'] = np.where(dataset['document_link'] == "/viewer/document/VDYxdYHKO2e10z7G_nXN1w", "LIT-12011523", dataset['document_number'])
    dataset['document_revision'] = np.where(dataset['document_link'] == "/viewer/document/VDYxdYHKO2e10z7G_nXN1w", "9.0", dataset['document_revision'])
    
    dataset['document_number'] = np.where(dataset['document_link'] == "/viewer/document/zf5NyN74A10uzAsu3SMC5w", "LIT-12011523", dataset['document_number'])
    dataset['document_revision'] = np.where(dataset['document_link'] == "/viewer/document/zf5NyN74A10uzAsu3SMC5w", "10.0", dataset['document_revision'])
    
    
    # LX Series
    dataset['document_number'] = np.where(dataset['document_link'] == "/viewer/document/A9E~IrO2FizzOQTtM8NH1g", "LIT-12011548", dataset['document_number'])
    
    
    # LX Series Free Programmable Controllers Wizard User’s Guide
    dataset['document_number'] = np.where(dataset['document_link'] == "/viewer/document/DEpoZ6o2uqi7uM6KajWHnA", "LIT-120114836", dataset['document_number'])
    
    
    # LX Series Powered Fan Coil Unit (PFCU) ControllerProduct Bulletin
    dataset['document_number'] = np.where(dataset['document_link'] == "/viewer/document/jv9AqvA1UsLZipj1XoCPOQ", "LIT-12011496", dataset['document_number'])
    
    
    # Language Installation Program
    dataset['document_number'] = np.where(dataset['document_link'] == "/viewer/document/7nRDVXgEZmo49F9dSJjLOA", "LIT-12011349", dataset['document_number'])
    dataset['document_revision'] = np.where(dataset['document_link'] == "/viewer/document/7nRDVXgEZmo49F9dSJjLOA", "9.0", dataset['document_revision'])
    
    dataset['document_number'] = np.where(dataset['document_link'] == "/viewer/document/mHkTJEnmXoLBfxKqYHhcow", "LIT-12011349", dataset['document_number'])
    dataset['document_revision'] = np.where(dataset['document_link'] == "/viewer/document/mHkTJEnmXoLBfxKqYHhcow", "10.0", dataset['document_revision'])
    
    dataset['document_number'] = np.where(dataset['document_link'] == "/viewer/document/0W3FsVsgmad8h60bL1kQDw", "LIT-12011793", dataset['document_number'])
    dataset['document_revision'] = np.where(dataset['document_link'] == "/viewer/document/0W3FsVsgmad8h60bL1kQDw", "9.0", dataset['document_revision'])
    
    dataset['document_number'] = np.where(dataset['document_link'] == "/viewer/document/aPLJgWPhWe0Ss_LvuKuwfw", "LIT-12011349", dataset['document_number'])
    dataset['document_revision'] = np.where(dataset['document_link'] == "/viewer/document/aPLJgWPhWe0Ss_LvuKuwfw", "10.0", dataset['document_revision'])
    
    
    # LN Series Heat Pump Unit Controller Catalog Page
    dataset['document_number'] = np.where(dataset['document_link'] == "/viewer/document/S1WtRVpTosOG8IY9UpwLsQ", "LIT-1900286", dataset['document_number'])
    
    
    # Metasys
    dataset['document_number'] = np.where(dataset['document_link'] == "/viewer/document/XdIY4~ZfKYACS_rOLwIpDQ", "LIT-12012115", dataset['document_number'])
    dataset['document_revision'] = np.where(dataset['document_link'] == "/viewer/document/XdIY4~ZfKYACS_rOLwIpDQ", "9.0", dataset['document_revision'])
    
    dataset['document_number'] = np.where(dataset['document_link'] == "/viewer/document/~HnTZgckEl8JTbr82_32iw", "LIT-12012115", dataset['document_number'])
    dataset['document_revision'] = np.where(dataset['document_link'] == "/viewer/document/~HnTZgckEl8JTbr82_32iw", "10.0", dataset['document_revision'])
    
    dataset['document_number'] = np.where(dataset['document_link'] == "/viewer/document/Js_K8i5mi9Xq4fLcG2SPkA", "LIT-12012115", dataset['document_number'])
    dataset['document_revision'] = np.where(dataset['document_link'] == "/viewer/document/Js_K8i5mi9Xq4fLcG2SPkA", "9.0", dataset['document_revision'])
    
    dataset['document_number'] = np.where(dataset['document_link'] == "/viewer/document/WHaF5hHuqWLBnWVMNsDtSw", "LIT-12012115", dataset['document_number'])
    dataset['document_revision'] = np.where(dataset['document_link'] == "/viewer/document/WHaF5hHuqWLBnWVMNsDtSw", "10.0", dataset['document_revision'])
    
    
    # Metasys Server Installation and Upgrade Instructions
    dataset['document_number'] = np.where(dataset['document_link'] == "/viewer/document/cDfWNpzfihszyKsSPacjzQ", "LIT-12012162", dataset['document_number'])
    dataset['document_revision'] = np.where(dataset['document_link'] == "/viewer/document/cDfWNpzfihszyKsSPacjzQ", "9.0", dataset['document_revision'])
    
    dataset['document_number'] = np.where(dataset['document_link'] == "/viewer/document/B2uDXO7npoEBbT~bLI~XXA", "LIT-12012162", dataset['document_number'])
    dataset['document_revision'] = np.where(dataset['document_link'] == "/viewer/document/B2uDXO7npoEBbT~bLI~XXA", "10.0", dataset['document_revision'])
    
    
    
    
    # Mobile Access Portal Gateway Quick Start Guide
    dataset['document_number'] = np.where(dataset['document_link'] == "/viewer/document/JJDuiSfJlb5RLzKUpyroKw", "24-10737-148", dataset['document_number'])
    
    
    dataset['document_number'] = np.where(dataset['document_link'] == "/viewer/document/WIjgQPOzr9Sv8p0tg_05_g", "24-10737-16", dataset['document_number'])
    dataset['document_revision'] = np.where(dataset['document_link'] == "/viewer/document/WIjgQPOzr9Sv8p0tg_05_g", "E", dataset['document_revision'])
    
    
    
    # Model DPV-1 Dry Pipe Valve External Resetting
    dataset['document_number'] = np.where(dataset['document_link'] == "/viewer/document/eyZn0BKNVE50_QSJmvWDnQ", "160.82-EG1", dataset['document_number'])
    dataset['document_number'] = np.where(dataset['document_link'] == "/viewer/document/Vf08F179r9JoyZ9TDczCIA", "TFP1020", dataset['document_number'])
    
    # Model QRS Electronic Accelerator (Quick Opening Device) For Dry Pipe or Preaction systems
    dataset['document_number'] = np.where(dataset['document_link'] == "/viewer/document/lC8Nnzevg04yDafKL1uQag", "TFP1100_03_2019", dataset['document_number'])
    dataset['document_number'] = np.where(dataset['document_link'] == "/viewer/document/rqBtt1KAFrpENfnn0t42nA", "TFP1100_08_2018", dataset['document_number'])
    
    # NS SERIES
    dataset['document_number'] = np.where(dataset['document_link'] == "/viewer/document/asBq~7NQSHsPbRmCsUQ~8g", "LIT-1901099", dataset['document_number'])
    dataset['document_number'] = np.where(dataset['document_link'] == "/viewer/document/_XcNYLPuwnoz8VWgEVmfKg", "LIT-1900350", dataset['document_number'])
    
    
    
    # SCT Installation and Upgrade Instructions
    dataset['document_number'] = np.where(dataset['document_link'] == "/viewer/document/6MnwmW5AUMk6WwyCzKbu7Q", "LIT-12012067", dataset['document_number'])
    dataset['document_revision'] = np.where(dataset['document_link'] == "/viewer/document/6MnwmW5AUMk6WwyCzKbu7Q", "13.0", dataset['document_revision'])
    
    dataset['document_number'] = np.where(dataset['document_link'] == "/viewer/document/E~6N4t7P89Tl6nRMPFz1Hg", "LIT-12012067", dataset['document_number'])
    dataset['document_revision'] = np.where(dataset['document_link'] == "/viewer/document/E~6N4t7P89Tl6nRMPFz1Hg", "12.0", dataset['document_revision'])
    
    
    # Security Administrator System Technical Bulletin
    dataset['document_number'] = np.where(dataset['document_link'] == "/viewer/document/K9NSKL5Nbylcp1oY9Qn18g", "LIT-1201528", dataset['document_number'])
    dataset['document_revision'] = np.where(dataset['document_link'] == "/viewer/document/K9NSKL5Nbylcp1oY9Qn18g", "9.0", dataset['document_revision'])
    
    dataset['document_number'] = np.where(dataset['document_link'] == "/viewer/document/MCPkAZzvOKmWrL32E_bu6Q", "LIT-1201528", dataset['document_number'])
    dataset['document_revision'] = np.where(dataset['document_link'] == "/viewer/document/MCPkAZzvOKmWrL32E_bu6Q", "10.0", dataset['document_revision'])
    
    
    
    
    
    # Smart Equipment Controls Sequence of Operation Overview
    dataset['document_number'] = np.where(dataset['document_link'] == "/viewer/document/f8b0~P0Q5RbHNQ4yS4zUsA", "LIT-12011950-D-0119", dataset['document_number'])
    dataset['document_number'] = np.where(dataset['document_link'] == "/viewer/document/fPrqEO58V0BkpnW3p3NQCQ", "LIT-12011950-C-0318", dataset['document_number'])
    
    
    # Trend Studies
    dataset = dataset.drop(dataset[(dataset['document_link'] == '/reader/yg_m1gVmpr1Bz~C29fArww/root')].index)
    dataset = dataset.drop(dataset[(dataset['document_link'] == '/reader/yg_m1gVmpr1Bz~C29fArww/kZlirwl63T3dy_ykeszUVA')  & (dataset['document_created_at'] == "2018-07-01")].index)
    
    
    
    
    # VIZOR Electronic Dry Pipe Accelerator (EDPA) Quick-Opening Device for Dry Pipe Systems
    dataset['document_number'] = np.where(dataset['document_link'] == "/viewer/document/j~Btnaw_OF7XXJbuxXdb~w", "TFP1105_08_2018", dataset['document_number'])
    dataset['document_number'] = np.where(dataset['document_link'] == "/viewer/document/j~Btnaw_OF7XXJbuxXdb~w", "TFP1105_06_2019", dataset['document_number'])
    
    
    # WRZ-7860-0 Receiver for One-to-One 
    dataset['document_number'] = np.where(dataset['document_link'] == "/viewer/document/5cZwpMiJ_2gvtUACDL09MA", "LIT-1900663", dataset['document_number'])
    dataset['document_number'] = np.where(dataset['document_link'] == "/viewer/document/QqZxEGl7p4tcE14SS2mP8w", "LIT-12011640", dataset['document_number'])
    
    
#    dataset = dataset[['topic_title','document_title', 'document_number', 'document_part_number', 
#                       'document_version', 'document_revision', 'document_type', 'document_created_at', 
#                       'document_last_edition', 'document_last_publication', 'document_revised_modified', 
#                       'document_link', 'maps_link', 'brand', 'product_identifier']]
    
    
    """
    IF DOCUMENT PART NUMBER PRESENT AND NO DOCUMENT NUMBER THEN DOCPART BECOMES DOCNUM
    IF DOC NUM PRESENT BUT NO DOC PART NUMBER THEN DOCNUM BECOMES DOCPART
    """
    
    
    
    dataset['document_number'] = np.where(dataset['document_number'] == "Not Specified", dataset['document_part_number'], dataset['document_number'])
    dataset['document_part_number'] = np.where(dataset['document_part_number'] == "Not Specified", dataset['document_number'], dataset['document_part_number'])
    
    
    
    """
    DOCUMENT UNIQUE IDENTIFIER
    NUMBER OF UNIQUE ID SHOULD BE EQAUL TO NUMBER OF DOCUMENTS
    document_title(shortened) + document_number + document_revision + brand_shortened
    """


    
    dataset['document_identifier'] = dataset['document_title'] + "-" + dataset['document_number'] + "-" + dataset['document_part_number'] + "-" + dataset['document_version'] + "-" + dataset['document_revision'] + "-" + dataset['document_type'] + "-" + dataset['document_created_at'] + "-" + dataset['product_identifier'] 

    
    
    """
    For specific cases, if one instruction is for mulitple products
    """
    
    dataset['document_identifier'] = np.where(dataset['product_identifier'] == "M9000-Joh-_VWG060NB2935HGC-XX-BC", "M9000_and-10009000-L32-XXXX-XX-XX-Joh-v", dataset['document_identifier'])
    dataset['document_identifier'] = np.where(dataset['product_identifier'] == "T-4000_Pneumatic_Room_Thermostat-Joh-_TE-1800-9600-XX-Bs", "T-4000_Sub-4003-L51-XXXX-XX-B-Joh-v", dataset['document_identifier'])
    dataset['document_identifier'] = np.where(dataset['product_identifier'] == "VAF-B-Joh-XX-XX-BC", "VAF-8000-L24-XXXX-XX-XX-Joh-v", dataset['document_identifier'])
    
    dataset['document_identifier'] = np.where((dataset['product_identifier'] == "Z-Series_IPS_2U-Exa-XX-ZZ-Nd") & (dataset['document_link'] == "/viewer/document/LEotDy~o83LS0~EjUQtIfg"), "Z-Series_IPS_2-2-L40-XXXX-XX-C-Exa-v", dataset['document_identifier'])
    dataset['document_identifier'] = dataset['document_identifier'].apply(lambda x: hashlib.sha1(str.encode(x)).hexdigest())
    
    ## COMPARISON CHECK
    #document_id_unique = list(dataset['document_identifier'].unique())
    #docs = dataset[dataset['topic_title'] == dataset['document_title']]
    #docs = docs.drop_duplicates()
    ##docs = list(dataset['document_identifier'].unique())
    #docs = docs.drop(['topic_title'], axis=1)
    #erratic = docs[docs['document_number'] == "Not Specified"]
    #erratic = erratic[erratic['document_part_number'] == "Not Specified"]
    #erratic['duplicate'] = erratic.duplicated(subset=['document_identifier'])
    #erratic_true = erratic[erratic['duplicate'] == True]
    
    
    dataset.to_csv('documents_unique_document_id.csv',  encoding='utf-8-sig', index=False)
        
    
    return dataset




dataset = unique_document_id('documents_unique_product_id.csv')
    

# COMPARISON CHECK
document_id_unique = list(dataset['document_identifier'].unique())
docs = dataset[dataset['topic_title'] == dataset['document_title']]
docs = docs.drop_duplicates()
docs_unique = list(dataset['document_identifier'].unique())
#docs = docs.drop(['topic_title'], axis=1)
#
#docs['duplicate'] = docs.duplicated(subset=['document_identifier'])
#docs_true = docs[docs['duplicate'] == True]



#dataset = pd.read_csv("documents_unique_document_id.csv", encoding='utf-8-sig')




#dataset_z = dataset[dataset['document_title'].str.contains( "Matrix")]













