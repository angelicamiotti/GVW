# GVW

Ce projet a été realisé en groupe dans le cadre de la fin de la formation Data Analyst de 400 h proposé par Global Knowledge. Nous avons eu 9 jours pour realiser ce projet qui consiste dans l'analyse des données de vente du Groupe Volkswagen (GVW)


# Resumé du projet
L'objectif de ce projet était de faire une analyse des données de vente des différentes marques du GVW dans la période de 2017-2022 afin d'évaluer : 
Les différences entre les différentes marques du GVW ; 
Les impacts du COVID dans chacune des marques GVW ; 
La présence du GVW en différent pays ; 
Les tendances générales de voitures BEV et si le Groupe Volkswagen suit ces tendances.

# Méthodologie de travail
Nous avons établi un Diagramme de Gantt dès le début du projet afin d'établir les risques de chaque tâche, de designer les responsables pour chaque tache et de bien planifier toutes les étapes dès le principe.
La méthodologie que nous avons suivi est la CRISP-DM (Cross Industry Standard Process for Data Mining) (https://www.datascience-pm.com/crisp-dm-2/)

# Sources de données
### GVW
Les données que nous avons extrait du GVW ont été tous sous forme de tableau excel, comme le suivant
https://annualreport2022.volkswagenag.com/divisions/brands-and-business-fields.html 
Ces données ne concernent que la performance du Groupe à niveau mondial.
### Sources externes
Les autres données que nous avons extrait étaient de différentes sources, telles que tableau dans pdf et tableau en ligne.
https://www.abcbourse.com/analyses/chiffres/VOW3f

https://www.best-selling-cars.com/electric/2022-full-year-germany-best-selling-electric-cars-by-brand-and-model/

https://www.best-selling-cars.com/germany/2022-full-year-germany-best-selling-car-brands/ 

https://www.best-selling-cars.com/france/2022-full-year-france-top-20-best-selling-car-models/ 

https://www.best-selling-cars.com/europe/2022-full-year-europe-car-sales-per-eu-uk-and-efta-country/

# ETL
Pour realiser l'extraction de données, nous avons fait du webscrapping avec du python et nous avons également utilisé python pour extraire des tableaux des documents pdf.


<img src="https://github.com/angelicamiotti/GVW/assets/8940755/36868bd6-6a71-4df1-9061-1465cd1a4f75" height="400">
&nbsp;
<img src="https://github.com/angelicamiotti/GVW/assets/8940755/771a1d62-156b-4832-900a-cc96aaae0404" height="400">



Pour réaliser la transformation et nettoyage de données, nous avons également utilisé Python. 

Ainsi, nous avons réalisé les étapes suivantes avec Python  :
- Extraction de données de différentes sources (xlsx, site internet, pdf) en utilisant Pandas ;  
- Dépivotage des colonnes ; 
- Suppression des colonnes et lignes non nécessaires ;
À la fin de ce processus, nous avions les Flat Tables.

Entre l'extraction des données et le dépivotage, nous avons realisé une partie de nettoyage des données avec Excel car nous avions des données em escrita inglesa (com , na casa dos milhares) et precisamos passar para a escrita francesa

Ensuite, nous sommes passés au Power BI, où nous avons modelisé un Data Warehouse des données internes du GVW et un pour les données que nous avons extrait d'autres sources avec tous les concurrents confondus.
Nous avons realisé une derniere partie de nettoyage de données 
