# -*- coding: utf-8 -*-
"""
Created on Fri Mar 13 07:56:27 2020

@author: LukaszMalucha
"""

import pandas as pd
import dateutil.parser


def unify_date_format(date):
    """Helper function that turns dates into correct format"""
    if type(date) == str:
        try:
            date = dateutil.parser.parse(date)   
        except:
            pass
    return str(date)[:10] 



dataset = pd.read_csv("SL team.txt", sep="\t", encoding="utf-8-sig")

#dataset.to_excel("TimesheetReport_20200312_1246.xlsx", encoding="utf-8-sig", index=False)


colums = dataset.columns.tolist()


dataset = dataset[["User", "Date", "Project", "RP/Task", "Time Type", "Bill Type", "Comment", "Hours"]]


dataset = dataset[~dataset["User"].isna()]



# USER
dataset["User"] = dataset["User"].str.replace("Clair, Jacinta", "Jacinta Clair")
dataset["User"] = dataset["User"].str.replace("Lenora O Sullivan", "Lenora O'Sullivan")
dataset["User"] = dataset["User"].str.replace("MCNAMARA, SAMANTHA", "Samantha McNamara")
dataset["User"] = dataset["User"].str.replace("Hayes, Diarmuid", "Diarmud Hayes")
dataset["User"] = dataset["User"].str.replace("Myers, Pamela", "Pamela Myers")
dataset["User"] = dataset["User"].str.replace("O'Regan, Edel", "Edel O'Regan")
dataset["User"] = dataset["User"].str.replace("Bannon, Niall", "Niall Bannon")
dataset["User"] = dataset["User"].str.replace("Burke, Aisling", "Aisling Burke")
dataset["User"] = dataset["User"].str.replace("Kelleher, David", "David Kelleher")
dataset["User"] = dataset["User"].str.replace("Kenneally, Karen", "Karen Kenneally")
dataset["User"] = dataset["User"].str.replace("Murphy, Maura", "Maura Murphy")


# DATE
dataset['Date'] = dataset['Date'].apply(lambda x: unify_date_format(x) )




# PROJECT
dataset["Project"] = dataset["Project"].str.replace("EAS-Tools / Process DEv & Maint", "EAS-Tools/Process DEV & Maintanace")
dataset["Project"] = dataset["Project"].str.replace("TSP-VAC-Tools/Process Dev& Maint", "TSP-VAC-Tools/Process DEV & Maintanance")



# RP/Task

dataset["RP/Task"] = dataset["RP/Task"].fillna('N/A')







dataset.to_excel("SL_team.xlsx", encoding="utf-8-sig", index=False)














