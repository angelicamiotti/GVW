# GVW

Ce projet a été réalisé en groupe dans le cadre de la fin de formation en tant que Data Analyst de 400 h proposée par Global Knowledge. Nous avons disposé de 9 jours pour réaliser ce projet qui consiste en l'analyse des données de vente du Groupe Volkswagen (GVW).


# Resumé du projet

L'objectif de ce projet était d'effectuer une analyse des données de vente des différentes marques du GVW sur la période de 2017 à 2022 afin d'évaluer :

- Les différences entre les différentes marques du GVW ; 
- Les impacts du COVID sur chacune des marques GVW ; 
- La présence du GVW dans différents pays ;
- Les tendances générales des voitures BEV et si le Groupe Volkswagen suit ces tendances.

# Méthodologie de travail
Nous avons établi un diagramme de Gantt dès le début du projet afin d'identifier les risques de chaque tâche, de désigner les responsables pour chaque tâche et de bien planifier toutes les étapes dès le début.
La méthodologie que nous avons suivie est la CRISP-DM (Cross Industry Standard Process for Data Mining) qui consiste en 5 étapes : business understanding, data understanding, data preparation, modeling, evaluation et deployement. 

# Sources de données
### GVW
Les données que nous avons extraites du GVW étaient toutes sous forme de tableaux Excel, comme le suivant :

https://annualreport2022.volkswagenag.com/divisions/brands-and-business-fields.html 

Ces données concernent uniquement la performance du Groupe à l'échelle mondiale.

### Sources externes
Les autres données que nous avons extraites provenaient de différentes sources, telles que des tableaux dans des PDF et des tableaux en ligne.

- https://www.abcbourse.com/analyses/chiffres/VOW3f
- https://www.best-selling-cars.com/electric/2022-full-year-germany-best-selling-electric-cars-by-brand-and-model/
- https://www.best-selling-cars.com/germany/2022-full-year-germany-best-selling-car-brands/ 
- https://www.best-selling-cars.com/france/2022-full-year-france-top-20-best-selling-car-models/ 

https://www.best-selling-cars.com/europe/2022-full-year-europe-car-sales-per-eu-uk-and-efta-country/

# ETL
Pour réaliser l'extraction des données, nous avons utilisé du web scraping avec Python et avons également utilisé Python pour extraire des tableaux de documents PDF.

*Exemple de feuilles de source du GVW et de sources externes*

<img src="https://github.com/angelicamiotti/GVW/assets/8940755/36868bd6-6a71-4df1-9061-1465cd1a4f75" height="250">
&nbsp;
<img src="https://github.com/angelicamiotti/GVW/assets/8940755/771a1d62-156b-4832-900a-cc96aaae0404" height="250">



Pour effectuer la transformation et le nettoyage des données, nous avons également utilisé Python. Les premiers tableaux donnent une idée générale du groupe.

Ainsi, nous avons réalisé les étapes suivantes avec Python  :
- Extraction de données de différentes sources (xlsx, site internet, pdf) en utilisant Pandas ;
- Dépivotage des colonnes ; 
- Suppression des colonnes et lignes non nécessaires ;

À la fin de ce processus, nous avons obtenu des flat tables pour les données du GVW et pour les données externes.

*Exemple de flat table obtenue pour les sources du groupe VW*
<img src="https://github.com/angelicamiotti/GVW/assets/8940755/42739ff4-7e5e-4ac6-a4c4-e3bd69c8c8cd" height="250">


Entre l'extraction des données et le dépivotage, nous avons realisé une partie de nettoyage des données avec Excel car nous avions des données en notation anglo-saxonne (avec des virgules pour les milliers) et nous devions les convertir en notation française.

Ensuite, nous sommes passés à Power BI, où nous avons réalisé une dernière partie de nettoyage de données. Nous avons également modélisé un entrepôt de données (Data Warehouse) pour les données internes du GVW ainsi qu'un autre pour les données extraites d'autres sources, incluant tous les concurrents de manière consolidée.


# Analyse de données
Pour réaliser l'analyse des données, nous avons principalement utilisé Python et Power BI.

Tout d'abord, nous voulions répondre à la question : "Quelle marque se vend le mieux ?"

C'est pourquoi nous avons confectionné un premier tableau de bord pour répondre à cette question selon plusieurs paramètres : ventes de véhicules, bénéfices, chiffre d'affaires.

<img src="https://github.com/angelicamiotti/GVW/assets/8940755/0614ad4e-ec58-42d2-b4b5-ce5d541c2991" height="300">


Ensuite, pour évaluer le profil de chaque marque sur la période 2017-2022, notamment les changements de stratégies en fonction du COVID, nous avons opté pour, avant de faire les tableaux de bord, réaliser des matrices de corrélation pour chaque marque avec Python afin d'avoir des premières pistes sur les variables numériques qui ont une dépendance linéaire.


<img src="https://github.com/angelicamiotti/GVW/assets/8940755/c2b51598-ea40-492f-8ee7-7eb77878aae9" height="300">
<img src="https://github.com/angelicamiotti/GVW/assets/8940755/f95ad710-78e3-4cb3-b658-7208ce0449ef" height="300">

Ensuite, nous sommes passés à la construction des tableaux de bord sur Power BI.


<img src="https://github.com/angelicamiotti/GVW/assets/8940755/68194466-3a42-4a35-a36b-72c60acc4361" height="300">

<img src="https://github.com/angelicamiotti/GVW/assets/8940755/343266cf-9b6f-4a13-8e89-5b547ca35161" height="300">



<img src="https://github.com/angelicamiotti/GVW/assets/8940755/f53a2f32-5f6d-4aca-bffd-21f364620f32" height="300">

<img src="https://github.com/angelicamiotti/GVW/assets/8940755/ffc06928-a31b-4d9a-99a1-497a0d3beb15" height="300">


