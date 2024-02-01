# -*- coding: utf-8 -*-
"""
Created on Thu Dec 21 15:16:17 2023

@author: 33603
"""

import pandas as pd

path = r"C:\Users\sacha\Downloads\datamart_country_EU_green_Models_v4.xlsx"

sheet1 = "F_Europe_by_brand"
data1 = pd.read_excel(path, sheet_name=sheet1,header=0)
df1 = pd.melt(data1, id_vars=['Group', 'Brand'], var_name='Year', value_name='Sales')
df1.sort_values(by=['Group', 'Brand','Year'], inplace=True)
df1['Year'] = df1['Year'].astype(int)
df1['Year'] = pd.to_datetime(df1['Year'].astype(str)).dt.year
df1.set_index('Group', inplace=True)

sheet2 = "F_Sales_EUR_country_green"
data2 = pd.read_excel(path, sheet_name=sheet2,header=0)
df2 = pd.melt(data2, id_vars=['EU Country', 'Powersource'], var_name='Year', value_name='Sales')
df2.sort_values(by=['EU Country', 'Powersource','Year'], inplace=True)
df2['Year'] = df2['Year'].astype(int)
df2['Year'] = pd.to_datetime(df2['Year'].astype(str)).dt.year
df2.set_index('EU Country', inplace=True)

sheet3="F_Sales_model_country"
data3=pd.read_excel(path, sheet_name=sheet3,header=0)
df3 = pd.melt(data3, id_vars=['Country', 'Group/Manufacturer', 'Brand', 'Division', 'Model'], var_name='Year', value_name='Sales')
df3.sort_values(by=['Country','Group/Manufacturer','Brand','Division','Model','Year'], inplace=True)
df3['Year'] = df3['Year'].astype(int)
df3['Year'] = pd.to_datetime(df3['Year'].astype(str)).dt.year
df3.set_index('Country', inplace=True)

df1.to_excel('F_Europe_by_brand.xlsx')
df2.to_excel('F_Sales_EUR_country_green.xlsx')
df3.to_excel('F_Sales_model_country.xlsx')