# -*- coding: utf-8 -*-
"""
Created on Fri Mar  6 10:03:50 2020

@author: jmalucl
"""

import pandas as pd

data = pd.read_csv("documents.csv", encoding='utf-8-sig')


miramo = data[data['title'].str.contains('miramo')]
miramo['link'] = "https://johnsoncontrols.fluidtopics.net" + miramo['link']
miramo.to_csv('miramo.csv',  encoding='utf-8-sig', index=False)



fm = data[data['title'].str.contains('.fm')]
fm['link'] = "https://johnsoncontrols.fluidtopics.net" + fm['link']
fm.to_csv('fm.csv',  encoding='utf-8-sig', index=False)



pdf = data[data['title'].str.contains('.pdf')]
pdf['link'] = "https://johnsoncontrols.fluidtopics.net" + pdf['link']
pdf.to_csv('pdf.csv',  encoding='utf-8-sig', index=False)



untitled = data[data['title'].str.contains('untitled')]
untitled['link'] = "https://johnsoncontrols.fluidtopics.net" + untitled['link']
untitled.to_csv('untitled.csv',  encoding='utf-8-sig', index=False)




yki = data[data['title'].str.contains('yki')]
yki['link'] = "https://johnsoncontrols.fluidtopics.net" + yki['link']
yki.to_csv('yki.csv',  encoding='utf-8-sig', index=False)
