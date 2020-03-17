# -*- coding: utf-8 -*-
"""
Created on Thu Mar 12 18:23:41 2020

@author: LukaszMalucha
"""

import pandas as pd
import numpy as np


def erratic_document_remover(dataset):
    
    # Remove erratic documents
    dataset = dataset[~dataset['document_title'].str.contains('miramo')]
    dataset = dataset[~dataset['document_title'].str.contains('.fm')]
    dataset = dataset[~dataset['document_title'].str.contains('.pdf')]
    dataset = dataset[~dataset['document_title'].str.contains('.html')]
    dataset = dataset[~dataset['document_title'].str.contains('yki')]
    dataset = dataset[~dataset['document_title'].str.contains('.indd')]
    dataset = dataset[~dataset['document_title'].str.contains('.book')]
    dataset = dataset[~dataset['document_title'].str.contains('untitled')]
    dataset = dataset[~dataset['document_title'].str.contains('Untitled')]
    dataset = dataset[~dataset['document_title'].str.contains('Microsoft Word - ')]
    dataset = dataset[~dataset['document_title'].str.contains('Heading1')]
    dataset = dataset[~dataset['document_title'].str.contains('JCI Data Sheet Template Letter Rev. 06')]
    
    # REMOVE ANSUL TEMPLATE SHEETS
    
    dataset = dataset[~dataset['document_title'].str.contains('ANSUL Instruction Sheet Template__A4_Rev-00')]
    dataset = dataset[~dataset['document_title'].str.contains('JCI Data Sheet A4 Template Rev')]
    dataset = dataset[~dataset['document_title'].str.contains('JCI datablad A4 mal Rev. 02')]
    dataset = dataset[~dataset['document_title'].str.contains('JCI-datablad A4 rev. av mal 02')]
    dataset = dataset[~dataset['document_title'].str.contains('05791229AC_B')]
    dataset = dataset[~dataset['document_title'].str.contains('05791328')]
    dataset = dataset[dataset['document_title'].str[:] != "Rev. 01"]
    
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
    
    
    
    # Duplicate ROOT of related links
    dataset = dataset.drop(dataset[(dataset['document_link'] == '/reader/iNhXVoRZ8gU~FccRXbZiSg/root')].index)
    dataset = dataset.drop(dataset[(dataset['document_link'] == '/reader/rKaUaPzNsfYl8765Nx7vEw/root')].index)
    
    
    # LN SERIES duplicates
    dataset = dataset.drop(dataset[(dataset['document_link'] == '/viewer/document/ae0NdKdEkDRsxJ7Lqcv6Kw')].index)
    dataset = dataset.drop(dataset[(dataset['document_link'] == '/viewer/document/posLIKe0MRJ1ycidLc0Gwg')].index)
    dataset = dataset.drop(dataset[(dataset['document_link'] == '/viewer/document/aGPFAcZtizylqo_vz84NIg')].index)
    dataset = dataset.drop(dataset[(dataset['document_link'] == '/viewer/document/ZPVYTOVVv7Ab7uEtgfhSZw')].index)
    
    
    
    # Johnson Controls® Enterprise Management duplicate with one missing topic
    dataset = dataset.drop(dataset[(dataset['document_link'] == '/reader/HolF8uBCOukfQ5PchZupIA/root')].index)
    
    
    return dataset
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    