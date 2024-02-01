# -*- coding: utf-8 -*-
"""
Created on Thu Dec 21 15:16:17 2023

@author: 33603
"""

import pandas as pd
import numpy as np

def table(path,cheet_list): #fonction qui fait l'extraction des donnée d'un fichier excel contenant plusieurs feuilles
    data=pd.read_excel(path, sheet_name=cheet_list[0],header=None)
    d=data.iloc[4:,1:3] #prendre la partie du data frame contenant les données
    d.iloc[1]=data.iloc[2,0] #ça prend la valeur du brand
    d=d.transpose() #le transposé du tableau resultant
    cheet_list=cheet_list[1:]
    for i in cheet_list: #parcourir toutes le feuilles de du fichier excel en question
        data= pd.read_excel(path, sheet_name=i,header=None)
        d1=data.iloc[4:,1:3]
        d1.iloc[1]=data.iloc[2,0]
        d1=d1.transpose()
        d=pd.concat([d,d1],ignore_index=True) #Conacatenation du resultat du traitement d'une feuille avec celle de l'ensemble des feuilles precedentes
    return d

def to_percentage(value):
    if isinstance(value, float):
        return value / 100
    else:
        return value

#application de la fonction sur les données existantes
#column={'4':"Year",'5':"Brand",'6':"Deliveries (thousand units)",'7':"Vehicle sales(K)",'8':"Production(K)",
         #'9':"Sales revenue (€ million)",'10':"Operating result",'11':"Operating return on sales (%)"}
column=["Year","Brand","Deliveries (thousand units)","Vehicle sales(K)","Production(K)","Sales revenue (€ million)"
        ,"Operating result","Operating return on sales (%)"]

# path1=r"C:\Users\33603\Desktop\Data_VWG\1_divisions_vw_ar18.xlsx"
# path2=r"C:\Users\33603\Desktop\Data_VWG\2_divisions-vw-ar20.xls"
# path3=r"C:\Users\33603\Desktop\Data_VWG\3_div-divisions-vw-ar22.xlsx"

path1=r"C:\Users\sacha\OneDrive\Bureau\Ly16102023\1. Cours\231219 Mise en situation\V3\1_divisions_vw_ar18.xlsx"
path2=r"C:\Users\sacha\OneDrive\Bureau\Ly16102023\1. Cours\231219 Mise en situation\V3\2_divisions-vw-ar20.xls"
path3=r"C:\Users\sacha\OneDrive\Bureau\Ly16102023\1. Cours\231219 Mise en situation\V3\3_div-divisions-vw-ar22.xlsx"

# path1=r"/content/1_divisions_vw_ar18.xlsx"
# path2=r"/content/2_divisions-vw-ar20.xls"
# path3=r"/content/3_div-divisions-vw-ar22.xlsx"


l=[path2,path3]
cheet_list=["vw_pc_key_figures","audi_key_figures","skoda_key_figures","seat_key_figures","bentley_key_figures",
        "porsche_key_figures","vehicles_key_figures","scania_key_figures","traton_deliveries","man_key_figures"]
d=table(path1,cheet_list)
for i in l: #parcourir touts les fichiers en appliquant la fonction table + concaténation
    a=table(i,cheet_list)
    d=pd.concat([d,a],ignore_index=True)
d.columns = column
d.reset_index(drop=True, inplace=True)

#extraire le nom correcte du Brand (Elimination de la partie Key Figures)
#pattern= r'^(.*?)\s*–\s*Key\s*Figures'
pattern= r'^(.*?)\s*–'
d['Brand'] = d['Brand'].str.extract(pattern).astype(str)
d['Brand'] = d['Brand'].str.strip('1')

# marques_a_garder = ['Audi', 'Škoda', 'SEAT', 'Bentley', 'Porsche', 'Scania', 'TRATON', 'MAN']
# # Filtrer le DataFrame
# d = d[d['Brand'].str.extract(f"({'|'.join(marques_a_garder)})", expand=False).notna()]

#Ajouter la colonne Division_type
Passenger_cars=['Volkswagen Passenger Cars','Audi','Škoda','SEAT','Bentley','Porsche']
Commercial_Cars=['Volkswagen Commercial Vehicles','Scania','TRATON','MAN']
d["Division_Type"] = np.where(d['Brand'].isin(Passenger_cars), "Passenger_car",
                     np.where(d['Brand'].isin(Commercial_Cars), "Commercial_car", None))

#Mettre en ordre les colonnes de latable resultantes
nouvel_ordre =["Year","Division_Type","Brand","Deliveries (thousand units)","Vehicle sales(K)","Production(K)","Sales revenue (€ million)"
        ,"Operating result","Operating return on sales (%)"]
d= d[nouvel_ordre]

#d['Year'] = d['Year'].apply(lambda year: str(year))
#Convertir la colonne de timestamp en datetime
#d['Year'] = pd.to_datetime(d['Year'], unit='y')
# d['Year'] = pd.to_datetime(d['Year'].str(), format='%Y')
d['Year'] = d['Year'].astype(int)
d['Year'] = pd.to_datetime(d['Year'].astype(str)).dt.year # + '-01-01')
d['Operating return on sales (%)'] = d['Operating return on sales (%)'].apply(to_percentage)
d.to_excel('flat_table.xlsx')